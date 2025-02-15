import asyncio

from volcenginesdkarkruntime import Ark

from config import global_config
from core.lines.lines import Line
from core.singleton.llm import ILLMInstance, LLM

print(global_config)
client = Ark(
    api_key=global_config["ARK_API_KEY"],
    timeout=120,
    max_retries=2,
    ak=global_config["AK"],
    sk=global_config["SK"],
)

print("----- standard request -----")


class LLMInstance(ILLMInstance):

    def check(self) -> bool:
        return True

    async def send_message(self, messages):
        text = ''
        stream = client.chat.completions.create(
            model="ep-20250215194542-zf5fs",
            messages=messages,
            stream=True
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            text = text + chunk.choices[0].delta.content
        return text


async def main():
    line = Line(llm=LLM(ins=LLMInstance()))

    response = await line.executor([
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ])

    print(response)
    # stream = client.chat.completions.create(
    #     model="ep-20250215194542-zf5fs",
    #     messages=[
    #         {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
    #         {"role": "user", "content": "常见的十字花科植物有哪些？"},
    #     ],
    #     stream=True
    # )
    # text = ''
    # for chunk in stream:
    #     if not chunk.choices:
    #         continue
    #     print(chunk.choices[0].delta.content, end="")
    #     text = text + chunk.choices[0].delta.content


if __name__ == "__main__":
    asyncio.run(main())
