from typing import Generic, TypeVar, Callable
import uuid

T = TypeVar("T")

class Event(Generic[T]):
    def __init__(self,name:str) -> None:
        self._id = uuid.uuid4().hex[:8]
        self._name = name
        self._subscribers : list[Callable[[T],None]] = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def subscribe(self,callback:Callable[[T],None]):
        self._subscribers.append(callback)

    def unsubscribe(self,callback:Callable[[T],None]):
        self._subscribers.remove(callback)

class EventEmitter(Event[T]):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def emit(self,param:T) -> None:
        for callback in self._subscribers:
            callback(param)
    