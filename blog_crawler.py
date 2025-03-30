import asyncio
import os
import logging
import re
from datetime import datetime
from crawl4ai import AsyncWebCrawler
from urllib.parse import urlparse

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BlogCrawler:
    def __init__(self, output_dir: str = "docs/blog"):
        self.output_dir = output_dir
        self.items_dir = f"{self.output_dir}/items"
        self.max_concurrent_tasks = 5
        
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """清理文件名，移除非法字符"""
        # 移除非法字符
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 移除多余空格
        filename = re.sub(r'\s+', ' ', filename).strip()
        # 限制文件名长度
        return filename[:80]
        
    @staticmethod
    def extract_domain(url: str) -> str:
        """从URL中提取域名"""
        domain_match = re.search(r'https?://(?:www\.)?([^/]+)', url)
        if domain_match:
            return domain_match.group(1)
        return "unknown-domain"
        
    @staticmethod
    def get_url_path(url: str) -> str:
        """从URL中提取完整路径"""
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        return path
        
    async def crawl_url(self, crawler: AsyncWebCrawler, url: str) -> None:
        """抓取单个URL并保存内容"""
        try:
            # 抓取内容
            result = await crawler.arun(url=url)
            content = result.markdown
            
            # 获取域名
            domain = self.extract_domain(url)
            
            # 获取URL的完整路径
            url_path = self.get_url_path(url)
            
            # 构建与URL结构完全一致的目录路径
            if url_path:
                # 获取URL路径的所有部分
                path_parts = url_path.split('/')
                # 最后一部分将作为文件名
                filename_part = path_parts[-1] if path_parts else "index"
                # 其余部分作为目录路径
                if len(path_parts) > 1:
                    dir_path = '/'.join(path_parts[:-1])
                    full_dir_path = f'{self.items_dir}/{domain}/{dir_path}'
                else:
                    full_dir_path = f'{self.items_dir}/{domain}'
            else:
                full_dir_path = f'{self.items_dir}/{domain}'
                filename_part = "index"
            
            # 确保目录存在
            os.makedirs(full_dir_path, exist_ok=True)
            
            # 清理文件名部分
            safe_filename = self.sanitize_filename(filename_part)
            if not safe_filename:
                safe_filename = "index"
            
            # 构建文件名
            filepath = f'{full_dir_path}/{safe_filename}.md'
            
            # 如果文件已存在，添加时间戳
            if os.path.exists(filepath):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filepath = f'{full_dir_path}/{safe_filename}_{timestamp}.md'
            
            # 保存内容
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# 原始URL: {url}\n\n")
                f.write(f"# 抓取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(content)
            
            logger.info(f'成功保存: {url} -> {filepath}')
            
        except Exception as e:
            logger.error(f'抓取失败 {url}: {str(e)}')
    
    async def crawl(self, urls: list) -> None:
        """批量抓取URL列表"""
        # 确保输出目录存在
        os.makedirs(self.items_dir, exist_ok=True)
        
        start_time = datetime.now()
        logger.info(f'开始抓取 {len(urls)} 个URL')
        
        async with AsyncWebCrawler() as crawler:
            tasks = []
            for url in urls:
                task = asyncio.create_task(self.crawl_url(crawler, url))
                tasks.append(task)
                
                if len(tasks) >= self.max_concurrent_tasks:
                    await asyncio.gather(*tasks)
                    tasks = []
            
            if tasks:
                await asyncio.gather(*tasks)
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f'抓取完成，保存到 {self.items_dir}，耗时: {duration:.2f} 秒')

async def main():
    # 示例URL列表
    urls = [
        "https://excalidraw-obsidian.online/Zsolt's+Blog/The+Case+for+Visual+Thinking",
    ]
    
    crawler = BlogCrawler()
    await crawler.crawl(urls)

if __name__ == "__main__":
    asyncio.run(main())
