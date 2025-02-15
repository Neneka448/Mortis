from typing import *
from abc import ABC, abstractmethod

class IActivateContext:
    def __init__(self):
        self.context = {}

class IActivatable(ABC):
    @abstractmethod
    def activate(self, ctx: IActivateContext):
        pass

class IPersistable(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class Atom(IActivatable,IPersistable,ABC):
    pass

class AtomContext:
    def __init__(self):
        self.messages: List[str] = []