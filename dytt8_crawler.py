import asyncio
from crawl4ai import *

# 爬取 dytt8.com 的最新电影
async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.dytt8.com/",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())