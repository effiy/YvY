import asyncio
import os
import logging
import re
from datetime import datetime
from crawl4ai import AsyncWebCrawler
from urllib.parse import urlparse, urljoin
from typing import List, Set, Dict, Any
import aiofiles # type: ignore
from functools import lru_cache

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
        self.max_concurrent_tasks = 10  # 增加并发任务数
        self.visited_urls = set()
        self.existing_files = set()  # 用于存储已经存在的文件路径
        self._file_existence_cache = {}  # 缓存文件存在检查结果
        
    @staticmethod
    @lru_cache(maxsize=1000)
    def sanitize_filename(filename: str) -> str:
        """清理文件名，移除非法字符"""
        # 移除非法字符
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 移除多余空格
        filename = re.sub(r'\s+', ' ', filename).strip()
        # 限制文件名长度
        return filename[:80] if filename else "index"
        
    @staticmethod
    @lru_cache(maxsize=1000)
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
    @lru_cache(maxsize=1000)
    def get_url_path(url: str) -> str:
        """从URL中提取完整路径"""
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        return path
        
    @lru_cache(maxsize=1000)
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
        base_domain = self.extract_domain(base_url)
        
        for match in re.finditer(link_pattern, content):
            url = match.group(2)
            
            # 忽略锚点链接
            if url.startswith('#'):
                continue
                
            # 处理相对链接
            if not url.startswith(('http://', 'https://')):
                url = urljoin(base_url, url)
                
            # 确保链接在同一域名下
            if self.extract_domain(url) == base_domain:
                if url not in unique_links:
                    unique_links.add(url)
                    links.append(url)
        
        return links
    
    def check_file_exists(self, url: str) -> bool:
        """检查URL对应的文件是否已经存在"""
        # 使用缓存避免重复检查
        if url in self._file_existence_cache:
            return self._file_existence_cache[url]
            
        domain = self.extract_domain(url)
        url_path = self.get_url_path(url)
        full_dir_path, filename_part = self.get_file_path(url, domain, url_path)
        safe_filename = self.sanitize_filename(filename_part)
        filepath = f'{full_dir_path}/{safe_filename}.md'
        
        # 检查文件是否存在
        exists = os.path.exists(filepath)
        self._file_existence_cache[url] = exists
        return exists
        
    async def crawl_url(self, crawler: AsyncWebCrawler, url: str, depth: int = 0, max_depth: int = 1) -> List[str]:
        """抓取单个URL并保存内容，返回提取的链接"""
        if url in self.visited_urls:
            logger.info(f'🔄 已访问过此URL，跳过: {url}')
            return []
            
        self.visited_urls.add(url)
        extracted_links = []
        
        # 检查文件是否已存在
        if self.check_file_exists(url):
            logger.info(f'📁 文件已存在，跳过抓取: {url}')
            # 如果需要继续抓取下一层，则从已存在的文件中提取链接
            if depth < max_depth:
                domain = self.extract_domain(url)
                url_path = self.get_url_path(url)
                full_dir_path, filename_part = self.get_file_path(url, domain, url_path)
                safe_filename = self.sanitize_filename(filename_part)
                filepath = f'{full_dir_path}/{safe_filename}.md'
                
                try:
                    async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
                        content = await f.read()
                    extracted_links = self.extract_links_from_md(content, url)
                    logger.info(f'🔗 从已存在文件 {url} 提取了 {len(extracted_links)} 个链接')
                except Exception as e:
                    logger.error(f'❌ 读取已存在文件失败 {filepath}: {str(e)}')
            return extracted_links
        
        try:
            # 抓取内容
            logger.info(f'🕸️ 正在抓取: {url}')
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
            file_content = f"# 原始URL: {url}\n\n"
            file_content += f"# 抓取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            file_content += content
            
            async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
                await f.write(file_content)
            
            logger.info(f'✅ 成功保存: {url} -> {filepath}')
            
            # 如果需要继续抓取下一层，则提取链接
            if depth < max_depth:
                extracted_links = self.extract_links_from_md(content, url)
                logger.info(f'🔍 从 {url} 提取了 {len(extracted_links)} 个链接')
            
        except Exception as e:
            logger.error(f'❌ 抓取失败 {url}: {str(e)}')
            
        return extracted_links
    
    async def crawl(self, urls: list, max_depth: int = 1) -> None:
        """批量抓取URL列表及其链接的内容，抓取深度由max_depth控制"""
        # 确保输出目录存在
        os.makedirs(self.items_dir, exist_ok=True)
        os.makedirs(self.seeds_dir, exist_ok=True)
        
        start_time = datetime.now()
        logger.info(f'🚀 开始抓取 {len(urls)} 个种子URL，最大深度: {max_depth}')
        
        # 预先创建一个共享的爬虫实例
        async with AsyncWebCrawler() as crawler:
            # 使用信号量控制并发数量
            semaphore = asyncio.Semaphore(self.max_concurrent_tasks)
            
            # 按层次抓取
            current_depth = 0
            current_layer_urls = urls
            
            while current_depth <= max_depth and current_layer_urls:
                logger.info(f'📊 开始抓取第 {current_depth} 层，共 {len(current_layer_urls)} 个URL')
                
                # 当前层的任务
                layer_tasks = []
                for url in current_layer_urls:
                    async def process_url(url=url):
                        async with semaphore:
                            return await self.crawl_url(crawler, url, depth=current_depth, max_depth=max_depth)
                    
                    layer_tasks.append(asyncio.create_task(process_url()))
                
                # 等待当前层任务完成并收集下一层URL
                next_layer_urls = []
                batch_results = await asyncio.gather(*layer_tasks)
                for links in batch_results:
                    next_layer_urls.extend(links)
                
                logger.info(f'✅ 第 {current_depth} 层抓取完成，发现 {len(next_layer_urls)} 个下一层链接')
                
                # 准备抓取下一层
                current_depth += 1
                current_layer_urls = next_layer_urls
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f'🎉 抓取完成，共处理 {len(self.visited_urls)} 个URL，保存到 {self.items_dir}，耗时: {duration:.2f} 秒')

async def main():
    # 示例URL列表
    urls = [
        "https://hub.baai.ac.cn/",
        "https://aibard123.com/digest/",
    ]
    
    crawler = BlogCrawler()
    # 设置最大抓取深度为2（种子URL为第0层，下面还有2层）
    await crawler.crawl(urls, max_depth=1)

if __name__ == "__main__":
    asyncio.run(main())
