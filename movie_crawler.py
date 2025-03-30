import asyncio
import re
import json
import os
from datetime import datetime
from dataclasses import dataclass
from typing import List
from crawl4ai import AsyncWebCrawler

@dataclass
class MarkdownLink:
    text: str
    url: str
    line_number: int

class MovieCrawler:
    def __init__(self):
        self.base_url = "https://www.dytt8.com"
        self.output_dir = "docs/dytt8/seeds"
        
    def extract_links_from_md(self, content: str) -> List[MarkdownLink]:
        """从 Markdown 内容中提取所有电影链接"""
        links = []
        unique_links = set()
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for line_number, line in enumerate(content.split('\n'), 1):
            matches = re.finditer(link_pattern, line)
            for match in matches:
                text = match.group(1)
                url = match.group(2)
                
                # 只保留电影详情页链接
                if not url.startswith("https://www.dytt8.com/html/gndy") or url.endswith("index.html"):
                    continue
                
                link_identifier = f"{text}|{url}"
                if link_identifier not in unique_links:
                    unique_links.add(link_identifier)
                    links.append(MarkdownLink(text=text, url=url, line_number=line_number))
        
        return links
    
    def save_links_to_json(self, links: List[MarkdownLink], output_file: str):
        """将链接信息保存为 JSON 文件"""
        links_data = [
            {"line_number": link.line_number, "text": link.text, "url": link.url}
            for link in links
        ]
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(links_data, f, ensure_ascii=False, indent=2)
            print(f"链接信息已保存到 {output_file}")
        except Exception as e:
            print(f"保存文件时发生错误：{str(e)}")
    
    def print_links(self, links: List[MarkdownLink]):
        """打印提取到的链接信息"""
        if not links:
            print("未找到任何链接")
            return
            
        print(f"\n找到 {len(links)} 个链接：")
        print("-" * 50)
        for link in links:
            print(f"lineNum: {link.line_number}")
            print(f"name: {link.text}")
            print(f"URL: {link.url}")
            print("-" * 50)
    
    async def crawl(self):
        """执行爬虫任务"""
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)
        
        # 爬取网页内容
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=self.base_url)
            passage = result.markdown
            
            # 提取链接
            links = self.extract_links_from_md(passage)
            
            # 保存原始 Markdown 内容
            current_time = datetime.now().strftime("%Y-%m-%d")
            md_filename = f"{self.output_dir}/{current_time}.md"
            json_filename = f"{self.output_dir}/{current_time}.json"
            
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(passage)
            
            print(f"原始内容已保存到 {md_filename}")
            
            # 保存链接信息
            self.save_links_to_json(links, json_filename)
            self.print_links(links)

async def main():
    crawler = MovieCrawler()
    await crawler.crawl()

if __name__ == "__main__":
    asyncio.run(main()) 