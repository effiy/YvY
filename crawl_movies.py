import json
import os
import asyncio
from crawl4ai import AsyncWebCrawler
import re
from typing import List, Dict, Any
from datetime import datetime

def sanitize_filename(filename: str) -> str:
    """清理文件名，移除非法字符并限制长度"""
    # 移除非法字符
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # 限制长度
    return filename[:100]

def extract_movie_name(text: str) -> str:
    """从电影条目文本中提取电影名称"""
    # 尝试匹配格式：年份+类型+《电影名》+其他信息
    match = re.search(r'^\d{4}年.*?《(.*?)》.*$', text)
    if match:
        return match.group(1)
    
    # 尝试匹配简单的《电影名》格式
    match = re.search(r'《(.*?)》', text)
    if match:
        return match.group(1)
    
    # 如果都没匹配到，返回原文本
    return text

async def crawl_movie_detail(crawler: AsyncWebCrawler, item: Dict[str, Any], output_dir: str) -> None:
    """抓取单个电影详情并保存"""
    # 提取电影名称
    movie_name = extract_movie_name(item['text'])
    safe_filename = sanitize_filename(movie_name)
    filepath = f'{output_dir}/{safe_filename}.md'
    
    # 如果文件已存在，跳过
    if os.path.exists(filepath):
        print(f'文件已存在，跳过: {safe_filename}')
        return
    
    try:
        # 抓取内容
        result = await crawler.arun(url=item['url'])
        content = result.markdown
        
        # 提取关键内容
        start_marker = "**搜索:**"
        end_marker = "●本栏目本周最新资源列表"
        
        if start_marker not in content or end_marker not in content:
            print(f'内容中缺少必要标记: {safe_filename}')
            return
            
        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        
        if start_index == -1 or end_index == -1 or start_index >= end_index:
            print(f'无法找到有效的内容范围: {safe_filename}')
            return
            
        extracted_content = content[start_index:end_index].strip()
        
        # 保存内容
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(extracted_content)
        
        print(f'成功保存: {safe_filename}')
        
    except Exception as e:
        print(f'抓取失败 {safe_filename}: {str(e)}')

async def main() -> None:
    # 配置
    seed_file = 'docs/dytt8/seeds/2025-03-30.json'
    output_dir = 'docs/dytt8/items'
    
    # 读取JSON文件
    try:
        with open(seed_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'读取种子文件失败: {str(e)}')
        return
    
    # 确保目标目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 创建crawler实例并处理每个电影条目
    start_time = datetime.now()
    print(f'开始抓取 {len(data)} 个电影详情...')
    
    async with AsyncWebCrawler() as crawler:
        # 使用有限并发抓取，避免请求过多
        tasks = []
        for item in data:
            task = asyncio.create_task(crawl_movie_detail(crawler, item, output_dir))
            tasks.append(task)
            # 控制并发数，每10个任务等待完成
            if len(tasks) >= 10:
                await asyncio.gather(*tasks)
                tasks = []
        
        # 等待剩余任务完成
        if tasks:
            await asyncio.gather(*tasks)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f'抓取完成，耗时: {duration:.2f} 秒')

if __name__ == '__main__':
    asyncio.run(main())