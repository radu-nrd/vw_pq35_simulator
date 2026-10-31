from typing import Generic,TypeVar
from abc import ABC,abstractmethod

TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')

class Encoder(ABC,Generic[TInput,TOutput]):
    @abstractmethod
    def encode(self,data:TInput) -> TOutput:
        pass