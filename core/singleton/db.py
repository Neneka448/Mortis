from abc import ABC, abstractmethod


class IDBInstance(ABC):
    @abstractmethod
    async def search(self, message):
        pass

    @abstractmethod
    async def save(self, message):
        pass

    @abstractmethod
    def check(self) -> bool:
        pass


class DB:
    def __init__(self, ins: IDBInstance):
        self._ins = ins

    async def check(self):
        return self._ins.check()

    async def search(self, message):
        message = await self._ins.search(message)
        return message

    async def save(self, message):
        message = await self._ins.save(message)
        return message
