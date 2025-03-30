import asyncio
import os
import logging
import re
from datetime import datetime
from crawl4ai import AsyncWebCrawler
from urllib.parse import urlparse, urljoin
from typing import List, Set, Dict, Any

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
        self.seeds_dir = f"{self.output_dir}/seeds"
        self.max_concurrent_tasks = 5
        self.visited_urls = set()
        
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """清理文件名，移除非法字符"""
        # 移除非法字符
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 移除多余空格
        filename = re.sub(r'\s+', ' ', filename).strip()
        # 限制文件名长度
        return filename[:80] if filename else "index"
        
    @staticmethod
    def extract_domain(url: str) -> str:
        """从URL中提取域名"""
        try:
            parsed_url = urlparse(url)
            return parsed_url.netloc.replace('www.', '')
        except:
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
        
    def get_file_path(self, url: str, domain: str, url_path: str) -> tuple:
        """获取文件保存路径和文件名"""
        if not url_path:
            return f'{self.items_dir}/{domain}', "index"
            
        path_parts = url_path.split('/')
        filename_part = path_parts[-1] if path_parts else "index"
        
        if len(path_parts) > 1:
            dir_path = '/'.join(path_parts[:-1])
            full_dir_path = f'{self.items_dir}/{domain}/{dir_path}'
        else:
            full_dir_path = f'{self.items_dir}/{domain}'
            
        return full_dir_path, filename_part
    
    def extract_links_from_md(self, content: str, base_url: str) -> List[str]:
        """从 Markdown 内容中提取所有链接"""
        links = []
        unique_links: Set[str] = set()
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for match in re.finditer(link_pattern, content):
            url = match.group(2)
            
            # 忽略锚点链接
            if url.startswith('#'):
                continue
                
            # 处理相对链接
            if not url.startswith(('http://', 'https://')):
                url = urljoin(base_url, url)
                
            # 确保链接在同一域名下
            if self.extract_domain(url) == self.extract_domain(base_url):
                if url not in unique_links:
                    unique_links.add(url)
                    links.append(url)
        
        return links
        
    async def crawl_url(self, crawler: AsyncWebCrawler, url: str, depth: int = 0) -> List[str]:
        """抓取单个URL并保存内容，返回提取的链接"""
        if url in self.visited_urls:
            return []
            
        self.visited_urls.add(url)
        extracted_links = []
        
        try:
            # 抓取内容
            result = await crawler.arun(url=url)
            content = result.markdown
            
            # 获取域名和路径
            domain = self.extract_domain(url)
            url_path = self.get_url_path(url)
            
            # 获取目录路径和文件名
            full_dir_path, filename_part = self.get_file_path(url, domain, url_path)
            
            # 确保目录存在
            os.makedirs(full_dir_path, exist_ok=True)
            
            # 清理文件名部分
            safe_filename = self.sanitize_filename(filename_part)
            
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
            
            # 如果需要继续抓取下一层，则提取链接
            if depth < 1:  # 只抓取两层（原始URL为第0层，下一层为第1层）
                extracted_links = self.extract_links_from_md(content, url)
                logger.info(f'从 {url} 提取了 {len(extracted_links)} 个链接')
            
        except Exception as e:
            logger.error(f'抓取失败 {url}: {str(e)}')
            
        return extracted_links
    
    async def crawl(self, urls: list) -> None:
        """批量抓取URL列表及其链接的内容（两层）"""
        # 确保输出目录存在
        os.makedirs(self.items_dir, exist_ok=True)
        os.makedirs(self.seeds_dir, exist_ok=True)
        
        start_time = datetime.now()
        logger.info(f'开始抓取 {len(urls)} 个种子URL')
        
        async with AsyncWebCrawler() as crawler:
            # 使用信号量控制并发数量
            semaphore = asyncio.Semaphore(self.max_concurrent_tasks)
            
            # 第一层：抓取种子URL
            first_layer_tasks = []
            for url in urls:
                async def process_url(url=url):
                    async with semaphore:
                        return url, await self.crawl_url(crawler, url, depth=0)
                
                first_layer_tasks.append(asyncio.create_task(process_url()))
            
            # 等待第一层任务完成并收集第二层URL
            second_layer_urls = []
            for task in asyncio.as_completed(first_layer_tasks):
                seed_url, links = await task
                second_layer_urls.extend(links)
            
            logger.info(f'第一层抓取完成，发现 {len(second_layer_urls)} 个第二层链接')
            
            # 第二层：抓取从第一层提取的URL
            second_layer_tasks = []
            for url in second_layer_urls:
                async def process_second_url(url=url):
                    async with semaphore:
                        return await self.crawl_url(crawler, url, depth=1)
                
                second_layer_tasks.append(asyncio.create_task(process_second_url()))
            
            # 等待第二层任务完成
            if second_layer_tasks:
                await asyncio.gather(*second_layer_tasks)
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f'抓取完成，共处理 {len(self.visited_urls)} 个URL，保存到 {self.items_dir}，耗时: {duration:.2f} 秒')

async def main():
    # 示例URL列表
    urls = [
        "https://excalidraw-obsidian.online/blog",
    ]
    
    crawler = BlogCrawler()
    await crawler.crawl(urls)

if __name__ == "__main__":
    asyncio.run(main())
