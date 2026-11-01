from typing import Generic,TypeVar
from abc import ABC,abstractmethod

TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


class Decoder(ABC,Generic[TInput,TOutput]):

    @abstractmethod
    def decode(self,data:TInput) -> TOutput:
        pass