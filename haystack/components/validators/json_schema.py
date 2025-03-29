# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Any, Dict, List, Optional

from jsonschema import ValidationError, validate

from haystack import component
from haystack.dataclasses import ChatMessage


def is_valid_json(s: str) -> bool:
    """
    检查提供的字符串是否为有效的JSON。

    :param s: 要检查的字符串。
    :returns: 如果字符串是有效的JSON则返回`True`；否则返回`False`。
    """
    try:
        json.loads(s)
    except ValueError:
        return False
    return True


@component
class JsonSchemaValidator:
    """
    根据指定的[JSON Schema](https://json-schema.org/)验证`ChatMessage`的JSON内容。

    如果消息的JSON内容符合提供的模式，则消息会通过"validated"输出传递。
    如果JSON内容不符合模式，则消息会通过"validation_error"输出传递。
    在后一种情况下，错误消息使用提供的`error_template`或默认模板构建。
    这些错误ChatMessages可以被Haystack 2.x恢复循环中的LLM使用。

    使用示例：

    ```python
    from typing import List

    from haystack import Pipeline
    from haystack.components.generators.chat import OpenAIChatGenerator
    from haystack.components.joiners import BranchJoiner
    from haystack.components.validators import JsonSchemaValidator
    from haystack import component
    from haystack.dataclasses import ChatMessage


    @component
    class MessageProducer:

        @component.output_types(messages=List[ChatMessage])
        def run(self, messages: List[ChatMessage]) -> dict:
            return {"messages": messages}


    p = Pipeline()
    p.add_component("llm", OpenAIChatGenerator(model="gpt-4-1106-preview",
                                               generation_kwargs={"response_format": {"type": "json_object"}}))
    p.add_component("schema_validator", JsonSchemaValidator())
    p.add_component("joiner_for_llm", BranchJoiner(List[ChatMessage]))
    p.add_component("message_producer", MessageProducer())

    p.connect("message_producer.messages", "joiner_for_llm")
    p.connect("joiner_for_llm", "llm")
    p.connect("llm.replies", "schema_validator.messages")
    p.connect("schema_validator.validation_error", "joiner_for_llm")

    result = p.run(data={
        "message_producer": {
            "messages":[ChatMessage.from_user("Generate JSON for person with name 'John' and age 30")]},
            "schema_validator": {
                "json_schema": {
                    "type": "object",
                    "properties": {"name": {"type": "string"},
                    "age": {"type": "integer"}
                }
            }
        }
    })
    print(result)
    >> {'schema_validator': {'validated': [ChatMessage(content='\\n{\\n  "name": "John",\\n  "age": 30\\n}',
    role=<ChatRole.ASSISTANT: 'assistant'>, name=None, meta={'model': 'gpt-4-1106-preview', 'index': 0,
    'finish_reason': 'stop', 'usage': {'completion_tokens': 17, 'prompt_tokens': 20, 'total_tokens': 37}})]}}
    ```
    """

    # 默认错误描述模板
    default_error_template = (
        "The following generated JSON does not conform to the provided schema.\n"
        "Generated JSON: {failing_json}\n"
        "Error details:\n- Message: {error_message}\n"
        "- Error Path in JSON: {error_path}\n"
        "- Schema Path: {error_schema_path}\n"
        "Please match the following schema:\n"
        "{json_schema}\n"
        "and provide the corrected JSON content ONLY. Please do not output anything else than the raw corrected "
        "JSON string, this is the most important part of the task. Don't use any markdown and don't add any comment."
    )

    def __init__(self, json_schema: Optional[Dict[str, Any]] = None, error_template: Optional[str] = None):
        """
        初始化JsonSchemaValidator组件。

        :param json_schema: 表示[JSON schema](https://json-schema.org/)的字典，用于验证消息内容。
        :param error_template: 验证失败时用于格式化错误消息的自定义模板字符串。
        """
        self.json_schema = json_schema
        self.error_template = error_template

    @component.output_types(validated=List[ChatMessage], validation_error=List[ChatMessage])
    def run(
        self,
        messages: List[ChatMessage],
        json_schema: Optional[Dict[str, Any]] = None,
        error_template: Optional[str] = None,
    ) -> Dict[str, List[ChatMessage]]:
        """
        验证提供的消息列表中的最后一条消息是否符合指定的JSON模式。

        如果符合，消息将通过"validated"输出传递。如果不符合，消息将通过"validation_error"输出传递。

        :param messages: 要验证的ChatMessage实例列表。验证的是列表中的最后一条消息。
        :param json_schema: 表示[JSON schema](https://json-schema.org/)的字典，用于验证消息内容。
                           如果未提供，则使用组件初始化时的模式。
        :param error_template: 验证失败时用于格式化错误消息的自定义模板字符串。如果未提供，
                              则使用组件初始化时的`error_template`。
        :return: 包含以下键的字典：
                - "validated": 如果最后一条消息有效，则为消息列表。
                - "validation_error": 如果最后一条消息无效，则为消息列表。
        :raises ValueError: 如果未提供JSON模式，或者消息内容不是字典或字典列表。
        """
        last_message = messages[-1]
        if last_message.text is None:
            raise ValueError(f"The provided ChatMessage has no text. ChatMessage: {last_message}")
        if not is_valid_json(last_message.text):
            return {
                "validation_error": [
                    ChatMessage.from_user(
                        f"The message '{last_message.text}' is not a valid JSON object. "
                        f"Please provide only a valid JSON object in string format."
                        f"Don't use any markdown and don't add any comment."
                    )
                ]
            }

        last_message_content = json.loads(last_message.text)
        json_schema = json_schema or self.json_schema
        error_template = error_template or self.error_template or self.default_error_template

        if not json_schema:
            raise ValueError("Provide a JSON schema for validation either in the run method or in the component init.")
        # fc payload是json对象，但子树`parameters`是字符串 - 我们需要转换为json对象
        # 我们需要完整的json来根据模式进行验证
        last_message_json = self._recursive_json_to_object(last_message_content)
        using_openai_schema: bool = self._is_openai_function_calling_schema(json_schema)
        if using_openai_schema:
            validation_schema = json_schema["parameters"]
        else:
            validation_schema = json_schema
        try:
            last_message_json = [last_message_json] if not isinstance(last_message_json, list) else last_message_json
            for content in last_message_json:
                if using_openai_schema:
                    validate(instance=content["function"]["arguments"], schema=validation_schema)
                else:
                    validate(instance=content, schema=validation_schema)

            return {"validated": [last_message]}
        except ValidationError as e:
            error_path = " -> ".join(map(str, e.absolute_path)) if e.absolute_path else "N/A"
            error_schema_path = " -> ".join(map(str, e.absolute_schema_path)) if e.absolute_schema_path else "N/A"

            error_template = error_template or self.default_error_template

            recovery_prompt = self._construct_error_recovery_message(
                error_template, str(e), error_path, error_schema_path, validation_schema, failing_json=last_message.text
            )
            return {"validation_error": [ChatMessage.from_user(recovery_prompt)]}

    def _construct_error_recovery_message(  # pylint: disable=too-many-positional-arguments
        self,
        error_template: str,
        error_message: str,
        error_path: str,
        error_schema_path: str,
        json_schema: Dict[str, Any],
        failing_json: str,
    ) -> str:
        """
        使用指定的模板或默认模板（如果未提供）构建错误恢复消息。

        :param error_template: 验证失败时用于格式化错误消息的自定义模板字符串。
        :param error_message: JSON模式验证器返回的错误消息。
        :param error_path: JSON内容中发生错误的路径。
        :param error_schema_path: JSON模式中发生错误的路径。
        :param json_schema: 用于验证内容的JSON模式。
        :param failing_json: 生成的无效JSON字符串。
        """
        error_template = error_template or self.default_error_template

        return error_template.format(
            error_message=error_message,
            error_path=error_path,
            error_schema_path=error_schema_path,
            json_schema=json_schema,
            failing_json=failing_json,
        )

    def _is_openai_function_calling_schema(self, json_schema: Dict[str, Any]) -> bool:
        """
        检查提供的模式是否为有效的OpenAI函数调用模式。

        :param json_schema: 要检查的JSON模式
        :return: 如果模式是有效的OpenAI函数调用模式则返回`True`；否则返回`False`。
        """
        return all(key in json_schema for key in ["name", "description", "parameters"])

    def _recursive_json_to_object(self, data: Any) -> Any:
        """
        将任何有效的JSON对象字符串值转换为字典对象。

        返回一个新的数据结构。

        :param data: 要遍历的数据结构。
        :return: 一个新的数据结构，其中JSON字符串已转换为字典对象。
        """
        if isinstance(data, list):
            return [self._recursive_json_to_object(item) for item in data]

        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                if isinstance(value, str):
                    try:
                        json_value = json.loads(value)
                        if isinstance(json_value, (dict, list)):
                            new_dict[key] = self._recursive_json_to_object(json_value)
                        else:
                            new_dict[key] = value  # 保留原始字符串值
                    except json.JSONDecodeError:
                        new_dict[key] = value
                elif isinstance(value, dict):
                    new_dict[key] = self._recursive_json_to_object(value)
                else:
                    new_dict[key] = value
            return new_dict

        # 如果既不是列表也不是字典，则直接返回值
        raise ValueError("Input must be a dictionary or a list of dictionaries.")
