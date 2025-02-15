from enum import Enum
from typing import *

from core.singleton.db import DB
from core.singleton.llm import LLM


class EnumLineStage(Enum):
    PRE_CHECK = 1
    PRE_PROCESS = 2
    CHAT_PROCESS = 3


class Line:
    def __init__(self,
                 llm: LLM,
                 db: DB = None):
        self.listener = {
            EnumLineStage.PRE_CHECK: [],
            EnumLineStage.CHAT_PROCESS: [],
            EnumLineStage.PRE_PROCESS: [],
        }
        self.llm = llm
        self.db = db
        self.options = {}
        self.merge_options()

    def merge_options(self):
        pass

    def pre_check(self):
        if not self.llm.check():
            raise Exception("[Fatal] LLM is not initialized")
        if self.db is not None and not self.db.check():
            raise Exception("[Fatal] DB is not initialized")

    def preprocess(self, messages: List[dict[str, str]]) -> List[dict[str, str]]:
        return messages

    async def chat_process(self, messages: List[dict[str, str]]) -> List[str]:
        return await self.llm.send_message(messages)

    async def executor(self, messages: List[dict[str, str]]):
        self.pre_check()

        next_messages = self.preprocess(messages)

        response = await self.chat_process(next_messages)

        return response
