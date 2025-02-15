from abc import ABC, abstractmethod


class ILLMInstance(ABC):
    @abstractmethod
    async def send_message(self, message):
        pass

    @abstractmethod
    def check(self) -> bool:
        pass


class LLM:
    def __init__(self, ins: ILLMInstance):
        self._ins = ins

    async def send_message(self, message):
        message = await self._ins.send_message(message)
        return message

    def check(self) -> bool:
        return self._ins.check()
