import asyncio
import re
import json
import os
from datetime import datetime
from dataclasses import dataclass
from typing import List, Set, Dict, Any, Optional
from crawl4ai import AsyncWebCrawler
import logging
import aiofiles
from functools import lru_cache

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class MovieLink:
    text: str
    url: str
    line_number: int

class MovieCrawler:
    def __init__(self, base_url: str = "https://www.dytt8.com", output_dir: str = "docs/dytt8"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.seeds_dir = f"{self.output_dir}/seeds"
        self.items_dir = f"{self.output_dir}/items"
        self.max_concurrent_tasks = 20  # 增加并发任务数
        self.semaphore = asyncio.Semaphore(self.max_concurrent_tasks)  # 添加信号量控制并发
        self._link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        self._movie_name_patterns = [
            re.compile(r'^\d{4}年.*?《(.*?)》.*$'),
            re.compile(r'《(.*?)》')
        ]
        
    def extract_links_from_md(self, content: str) -> List[MovieLink]:
        """从 Markdown 内容中提取所有电影链接"""
        links = []
        unique_links: Set[str] = set()
        
        for line_number, line in enumerate(content.split('\n'), 1):
            for match in self._link_pattern.finditer(line):
                text = match.group(1)
                url = match.group(2)
                
                if not url.startswith(self.base_url) or url.endswith("index.html"):
                    continue
                
                link_identifier = f"{text}|{url}"
                if link_identifier not in unique_links:
                    unique_links.add(link_identifier)
                    links.append(MovieLink(text=text, url=url, line_number=line_number))
        
        return links
    
    async def save_links_to_json(self, links: List[MovieLink], output_file: str) -> None:
        """将链接信息保存为 JSON 文件"""
        links_data = [
            {"line_number": link.line_number, "text": link.text, "url": link.url}
            for link in links
        ]
        
        try:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            async with aiofiles.open(output_file, 'w', encoding='utf-8') as f:
                await f.write(json.dumps(links_data, ensure_ascii=False, indent=2))
            logger.info(f"链接信息已保存到 {output_file}")
        except Exception as e:
            logger.error(f"保存文件时发生错误：{str(e)}")
            raise
    
    @staticmethod
    @lru_cache(maxsize=1000)  # 缓存文件名清理结果
    def sanitize_filename(filename: str) -> str:
        """清理文件名，移除非法字符并限制长度"""
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        return filename[:100]
    
    def extract_movie_name(self, text: str) -> str:
        """从电影条目文本中提取电影名称"""
        for pattern in self._movie_name_patterns:
            match = pattern.search(text)
            if match:
                return match.group(1)
        
        return text
    
    async def crawl_movie_detail(self, crawler: AsyncWebCrawler, item: Dict[str, Any]) -> None:
        """抓取单个电影详情并保存"""
        async with self.semaphore:  # 使用信号量控制并发
            movie_name = self.extract_movie_name(item['text'])
            safe_filename = self.sanitize_filename(movie_name)
            filepath = f'{self.items_dir}/{safe_filename}.md'
            
            if os.path.exists(filepath):
                logger.info(f'文件已存在，跳过: {safe_filename}')
                return
            
            try:
                result = await crawler.arun(url=item['url'])
                content = result.markdown
                
                start_marker = "**搜索:**"
                end_marker = "●本栏目本周最新资源列表"
                
                if start_marker not in content or end_marker not in content:
                    logger.warning(f'内容中缺少必要标记: {safe_filename}')
                    return
                    
                start_index = content.find(start_marker)
                end_index = content.find(end_marker)
                
                if start_index == -1 or end_index == -1 or start_index >= end_index:
                    logger.warning(f'无法找到有效的内容范围: {safe_filename}')
                    return
                    
                extracted_content = content[start_index:end_index].strip()
                
                async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
                    await f.write(extracted_content)
                
                logger.info(f'成功保存: {safe_filename}')
                
            except Exception as e:
                logger.error(f'抓取失败 {safe_filename}: {str(e)}')
    
    async def crawl_movie_details(self, seed_file: str) -> None:
        """批量抓取电影详情"""
        try:
            async with aiofiles.open(seed_file, 'r', encoding='utf-8') as f:
                content = await f.read()
                data = json.loads(content)
        except Exception as e:
            logger.error(f'读取种子文件失败: {str(e)}')
            return
        
        os.makedirs(self.items_dir, exist_ok=True)
        
        start_time = datetime.now()
        logger.info(f'开始抓取 {len(data)} 个电影详情，来源: {self.base_url}')
        
        async with AsyncWebCrawler(max_concurrent=self.max_concurrent_tasks) as crawler:
            tasks = []
            for item in data:
                task = asyncio.create_task(self.crawl_movie_detail(crawler, item))
                tasks.append(task)
            
            # 一次性创建所有任务，让asyncio调度器管理
            await asyncio.gather(*tasks)
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f'抓取完成，保存到 {self.items_dir}，耗时: {duration:.2f} 秒')
    
    async def crawl(self) -> None:
        """执行爬虫任务"""
        os.makedirs(self.seeds_dir, exist_ok=True)
        
        current_time = datetime.now().strftime("%Y-%m-%d")
        md_filename = f"{self.seeds_dir}/index_{current_time}.md"
        json_filename = f"{self.seeds_dir}/links_{current_time}.json"
        
        logger.info(f"开始从 {self.base_url} 抓取电影信息")
        
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=self.base_url)
            passage = result.markdown
            
            # 并行执行保存操作
            save_md_task = asyncio.create_task(self._save_markdown(md_filename, passage))
            links = self.extract_links_from_md(passage)
            save_json_task = asyncio.create_task(self.save_links_to_json(links, json_filename))
            
            # 等待保存操作完成
            await asyncio.gather(save_md_task, save_json_task)
            
            # 立即开始抓取详情
            await self.crawl_movie_details(json_filename)
    
    async def _save_markdown(self, filename: str, content: str) -> None:
        """异步保存Markdown内容"""
        async with aiofiles.open(filename, "w", encoding="utf-8") as f:
            await f.write(content)
        logger.info(f"电影内容已保存到 {filename}")

async def main():
    crawler = MovieCrawler(
        base_url="https://www.dytt8.com",
        output_dir="docs/dytt8"
    )
    await crawler.crawl()

if __name__ == "__main__":
    asyncio.run(main())