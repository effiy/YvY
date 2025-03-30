import os
import json
import re
import logging
from haystack import Pipeline

from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.ollama import OllamaChatGenerator

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


template = [
    ChatMessage.from_system(
"""
# Role
电影信息提取器

## Skills
- 精通中文
- 能够理解文本
- 精通JSON数据格式

## Action
- 根据提供的电影描述，提取出对应的 封面图片、译名、片名、年代、产地、类别、语言、字幕、上映日期、IMDb评分、豆瓣评分、片长、导演、编剧、主演、简介、获奖情况 等信息，并以JSON格式输出

## Constrains
- 忽略无关内容
- 必须保证你的结果只包含一个合法的JSON格式
- 如果某些信息不存在，对应的字段值设为null
- 提取下载链接时，优先提取磁力链接

## Format
- 对应JSON的key为：
  - "cover_image": 封面图片
  - "translated_name": 译名
  - "original_name": 片名
  - "year": 年代
  - "country": 产地
  - "genre": 类别
  - "language": 语言
  - "subtitle": 字幕
  - "release_date": 上映日期
  - "imdb_rating": IMDb评分
  - "douban_rating": 豆瓣评分
  - "duration": 片长
  - "director": 导演
  - "screenwriter": 编剧
  - "actors": 主演
  - "synopsis": 简介
  - "awards": 获奖情况
  - "download_links": 下载链接
"""
    ),
    ChatMessage.from_user(
"""
内容：{{ content }}
"""
    )
]


def extract_movie_info(content):
    """创建并运行电影信息提取管道"""
    logger.info("开始提取电影信息")
    
    # 创建提取管道
    prompt_builder = ChatPromptBuilder(template=template)
    llm = OllamaChatGenerator()
    
    pipeline = Pipeline()
    pipeline.add_component("prompt_builder", prompt_builder)
    pipeline.add_component("llm", llm)
    pipeline.connect("prompt_builder.prompt", "llm.messages")
    
    # 运行管道，处理文件内容
    logger.debug("运行LLM提取管道")
    result = pipeline.run(data={"prompt_builder": {"content": content}})
    logger.info("电影信息提取完成")
    return result["llm"]["replies"][0].text


def clean_json_text(json_text):
    """清理JSON文本，处理常见的格式问题"""
    logger.info("开始清理JSON文本")
    
    # 提取JSON部分（如果LLM输出了额外的文本）
    json_match = re.search(r'({[\s\S]*})', json_text)
    if json_match:
        json_text = json_match.group(1)
        logger.debug("从文本中提取了JSON部分")
    
    # 修复常见的JSON格式错误
    json_text = json_text.replace('，', ',')
    json_text = json_text.replace('：', ':')
    json_text = json_text.replace('`', '')
    json_text = json_text.replace('```json', '').replace('```', '')
    
    logger.info("JSON文本清理完成")
    return json_text.strip()


def process_files(directory):
    """处理目录中的所有Markdown文件并提取电影信息"""
    logger.info(f"开始处理目录: {directory}")
    results = []
    processed_count = 0
    error_count = 0
    skipped_count = 0
    
    # 确保目录存在
    if not os.path.exists(directory):
        logger.error(f"错误：目录 {directory} 不存在")
        return results
    
    # 获取所有Markdown文件
    md_files = [f for f in os.listdir(directory) if f.endswith(".md")]
    total_files = len(md_files)
    
    logger.info(f"找到 {total_files} 个Markdown文件待处理")
    print(f"开始处理 {total_files} 个文件...")
    
    # 确保结果目录存在
    results_dir = "docs/dytt8/results"
    os.makedirs(results_dir, exist_ok=True)
    
    for idx, filename in enumerate(md_files, 1):
        file_path = os.path.join(directory, filename)
        logger.info(f"开始处理文件 [{idx}/{total_files}]: {filename}")
        
        try:
            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            logger.debug(f"成功读取文件内容: {filename}")
            
            # 使用文件名检查是否已处理过
            # 先检查是否已有同名文件存在，避免重复处理
            existing_files = [f for f in os.listdir(results_dir) if f.endswith(".json")]
            base_filename = os.path.splitext(filename)[0]
            matching_files = [f for f in existing_files if base_filename in f]
            
            if matching_files:
                logger.info(f"文件可能已处理过，跳过: {filename}")
                print(f"跳过可能已处理的文件 [{idx}/{total_files}]: {filename}")
                skipped_count += 1
                continue
            
            # 提取电影信息
            json_result = extract_movie_info(content)
            
            # 清理和解析JSON
            cleaned_json = clean_json_text(json_result)
            logger.debug("尝试解析JSON")
            parsed_json = json.loads(cleaned_json)
            
            # 添加文件名信息
            parsed_json["source_file"] = filename
            
            # 使用译名作为文件名保存单个电影信息
            movie_name = parsed_json.get("translated_name") or parsed_json.get("original_name")
            if not movie_name:
                movie_name = base_filename  # 如果没有提取到电影名，使用原文件名
                
            # 替换文件名中的非法字符
            safe_name = re.sub(r'[\\/:*?"<>|]', '_', movie_name)
            movie_file = os.path.join(results_dir, f"{safe_name}.json")
            
            # 检查结果文件是否已存在
            if os.path.exists(movie_file):
                logger.info(f"文件已存在，跳过处理: {movie_file}")
                print(f"跳过已存在的文件 [{idx}/{total_files}]: {filename}")
                skipped_count += 1
                continue
            
            # 保存结果到文件
            with open(movie_file, "w", encoding="utf-8") as f:
                json.dump(parsed_json, f, ensure_ascii=False, indent=2)
            logger.info(f"已将电影《{movie_name}》的信息保存到 {movie_file}")
            
            # 添加到结果列表
            results.append(parsed_json)
            
            processed_count += 1
            logger.info(f"成功处理文件 [{idx}/{total_files}]: {filename}")
            print(f"成功处理文件 [{idx}/{total_files}]: {filename}")
            
        except json.JSONDecodeError as e:
            error_count += 1
            error_msg = f"处理文件 {filename} 时出现JSON解析错误: {str(e)}"
            logger.error(error_msg)
            print(error_msg)
        except Exception as e:
            error_count += 1
            error_msg = f"处理文件 {filename} 时出现未知错误: {str(e)}"
            logger.error(error_msg)
            print(error_msg)
    
    summary_msg = f"处理完成: 成功 {processed_count} 个, 跳过 {skipped_count} 个, 失败 {error_count} 个"
    logger.info(summary_msg)
    print(summary_msg)
    return results


# 主程序
if __name__ == "__main__":
    logger.info("程序开始执行")
    items_dir = "docs/dytt8/items"
    results = process_files(items_dir)
    
    # 确保结果目录存在
    results_dir = "docs/dytt8/results"
    os.makedirs(results_dir, exist_ok=True)
    
    # 将所有结果保存到结果目录中的汇总JSON文件
    if results:
        output_file = os.path.join(results_dir, "movie_info_results.json")
        logger.info(f"正在将所有结果保存到汇总文件: {output_file}")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        logger.info(f"所有结果已保存到 {output_file}")
        print(f"所有结果已保存到 {output_file}，共 {len(results)} 部电影")
    else:
        logger.warning("没有新的电影信息被提取")
        print("没有新的电影信息被提取")