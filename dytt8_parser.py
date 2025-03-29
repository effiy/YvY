from typing import List, Optional
import os
from pydantic import BaseModel, Field

# 定义数据模型
class Seed(BaseModel):
    name: str  # 种子名称
    url: str   # 种子链接

class Seeds(BaseModel):
    seeds: List[Seed]

class Movie(BaseModel):
    translated_name: str    # 译名
    original_name: str      # 片名
    year: int               # 年份
    country: str            # 产地
    category: str           # 类别
    language: str           # 语言
    subtitle: str           # 字幕
    release_date: str       # 上映日期
    imdb_score: Optional[float] = None  # IMDb评分
    douban_score: Optional[float] = None  # 豆瓣评分
    duration: str           # 时长
    director: str           # 导演
    writer: Optional[str] = None  # 编剧
    actors: List[str] = Field(default_factory=list)  # 演员
    cover_url: Optional[str] = None  # 封面图片链接
    description: Optional[str] = None  # 简介
    download_url: Optional[str] = None  # 下载链接
    magnet_url: Optional[str] = None  # 磁力链接
    torrent_url: Optional[str] = None  # 种子链接

class Movies(BaseModel):
    movies: List[Movie]

from haystack import Pipeline
from datasets import load_dataset  # type: ignore

from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage

from haystack_integrations.components.generators.ollama import OllamaChatGenerator

def parse_dytt8_data(file_paths=None):
    """解析电影天堂数据并返回结构化信息"""
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")
    if file_paths is None:
        # 使用当前日期构建文件路径
        file_paths = [f"./docs/dytt8/seeds/{current_date}.md"]
    
    print(f"开始解析电影天堂数据，使用文件：{file_paths}")
    
    # 加载文档
    dataset = load_dataset("text", data_files={"train": file_paths}, split="train")
    print(f"成功加载数据集，共有 {len(dataset)} 条记录")
    
    # 创建提示模板
    prompt_template = [
        ChatMessage.from_user(
            """
从这段文字中创建一个JSON对象：{{passage}}。
只使用文本中存在的信息。请按照以下JSON模式进行格式化，但只返回实际的实例，不要包含任何额外的模式定义：
{{schema}}
确保你的响应是一个字典而不是列表。
{% if invalid_replies and error_message %}
你在之前的尝试中已经创建了以下输出：{{invalid_replies}}
然而，这不符合上述格式要求，并触发了以下Python异常：{{error_message}}
请修正输出并重试。只需返回修正后的输出，无需任何额外解释。
{% endif %}
            """
        )
    ]
    
    print("创建处理管道...")
    # 构建处理管道
    pipeline = Pipeline(max_runs_per_component=5)
    pipeline.add_component("prompt_builder", ChatPromptBuilder(template=prompt_template))
    pipeline.add_component("generator", OllamaChatGenerator(
        generation_kwargs={
            "num_predict": 20000,  # 设置最大输出令牌数
            "temperature": 0.6,   # 降低温度以获得更确定性的输出
        }
    ))
    
    # 设置组件连接
    pipeline.connect("prompt_builder.prompt", "generator.messages")
    
    # 准备JSON模式
    json_schema = Seeds.schema_json(indent=2)
    results = []
    
    # 确保输出目录存在
    os.makedirs("docs/dytt8/seeds", exist_ok=True)
    print("已创建输出目录：docs/dytt8/seeds")
    
    for i, doc in enumerate(dataset):
        print(f"正在处理第 {i+1}/{len(dataset)} 条记录...")
        passage = doc['text'] # type: ignore
        # 运行管道
        print("调用LLM进行解析...")
        result = pipeline.run(
            {
                "prompt_builder": {
                    "passage": passage, 
                    "schema": json_schema
                }
            }
        )
        
        text_result = result["generator"]["replies"][0].text
        results.append(text_result)
        output_file = f"docs/dytt8/seeds/items_{current_date}.md"
        
        # 检查文件是否存在，如果存在则追加内容而不是覆盖
        if os.path.exists(output_file):
            with open(output_file, "a", encoding="utf-8") as f:
                f.write("\n" + text_result)
            print(f"解析结果已追加到：{output_file}")
        else:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text_result)
            print(f"解析结果已保存到：{output_file}")

    print(f"所有数据处理完成，共处理 {len(results)} 条记录")
    return results

if __name__ == "__main__":
    print("开始执行电影天堂数据解析程序...")
    parse_dytt8_data()
    print("程序执行完毕！")
