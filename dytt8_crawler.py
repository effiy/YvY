import asyncio

from crawl4ai import AsyncWebCrawler

# 爬取 dytt8.com 的最新电影
async def main():
    # 爬取网页内容
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.dytt8.com/")
        passage = result.markdown
        
        # 确保 docs/dytt8 目录存在
        import os
        os.makedirs("docs/dytt8/seeds", exist_ok=True)
        
        # 将结果写入 docs/dytt8 文件夹下的文件
        # 添加时间到文件名
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d")
        filename = f"docs/dytt8/seeds/{current_time}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(passage)
            
        print(f"爬取结果已保存到 {filename}")
        
if __name__ == "__main__":
    asyncio.run(main())