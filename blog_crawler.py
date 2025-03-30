import os
import json
import asyncio
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional

from crawl4ai import AsyncWebCrawler

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BlogCrawler:
    """博客爬虫类，用于抓取博客内容"""
    
    def __init__(self):
        self.base_url = "https://excalidraw-obsidian.online/blog"
        self.output_dir = "docs/blog"
        self.seeds_dir = f"{self.output_dir}/seeds"
        self.items_dir = f"{self.output_dir}/items"
        self.max_concurrent_tasks = 5
    
    def extract_links_from_md(self, markdown_content: str) -> List[Dict[str, str]]:
        """从Markdown内容中提取链接"""
        import re
        
        # 匹配Markdown链接格式 [文本](链接)
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(pattern, markdown_content)
        
        links = []
        for text, url in matches:
            # 确保URL是完整的
            if not url.startswith('http'):
                if url.startswith('/'):
                    url = f"https://excalidraw-obsidian.online{url}"
                else:
                    url = f"{self.base_url}/{url}"
            
            links.append({
                "title": text,
                "url": url
            })
        
        return links
    
    def save_links_to_json(self, links: List[Dict[str, str]], filename: str) -> None:
        """将链接保存到JSON文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(links, f, ensure_ascii=False, indent=2)
        
        logger.info(f"链接已保存到 {filename}")
    
    async def crawl_blog_post(self, crawler: AsyncWebCrawler, item: Dict[str, str]) -> None:
        """抓取单个博客文章"""
        title = item.get("title", "未知标题")
        url = item.get("url", "")
        
        if not url:
            logger.warning(f"跳过无URL的项目: {title}")
            return
        
        try:
            safe_filename = title.replace("/", "_").replace("\\", "_").replace(":", "_")
            safe_filename = f"{safe_filename}.md"
            filepath = os.path.join(self.items_dir, safe_filename)
            
            # 检查文件是否已存在
            if os.path.exists(filepath):
                logger.info(f"文件已存在，跳过: {safe_filename}")
                return
            
            result = await crawler.arun(url=url)
            content = result.markdown
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f'成功保存: {safe_filename}')
            
        except Exception as e:
            logger.error(f'抓取失败 {title}: {str(e)}')
    
    async def crawl_blog_posts(self, seed_file: str) -> None:
        """批量抓取博客文章"""
        try:
            with open(seed_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f'读取种子文件失败: {str(e)}')
            return
        
        os.makedirs(self.items_dir, exist_ok=True)
        
        start_time = datetime.now()
        logger.info(f'开始抓取 {len(data)} 个博客文章...')
        
        async with AsyncWebCrawler() as crawler:
            tasks = []
            for item in data:
                task = asyncio.create_task(self.crawl_blog_post(crawler, item))
                tasks.append(task)
                
                if len(tasks) >= self.max_concurrent_tasks:
                    await asyncio.gather(*tasks)
                    tasks = []
            
            if tasks:
                await asyncio.gather(*tasks)
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f'抓取完成，耗时: {duration:.2f} 秒')
    
    async def crawl(self) -> None:
        """执行爬虫任务"""
        os.makedirs(self.seeds_dir, exist_ok=True)
        os.makedirs(self.items_dir, exist_ok=True)
        
        current_time = datetime.now().strftime("%Y-%m-%d")
        md_filename = f"{self.seeds_dir}/index_{current_time}.md"
        json_filename = f"{self.seeds_dir}/links_{current_time}.json"
        
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=self.base_url)
            passage = result.markdown
            
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(passage)
            logger.info(f"博客索引已保存到 {md_filename}")
            
            links = self.extract_links_from_md(passage)
            self.save_links_to_json(links, json_filename)
            
            # 立即开始抓取详情
            await self.crawl_blog_posts(json_filename)

async def main():
    crawler = BlogCrawler()
    await crawler.crawl()

if __name__ == "__main__":
    asyncio.run(main())
