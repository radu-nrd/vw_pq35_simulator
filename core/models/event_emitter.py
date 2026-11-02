from .event import Event
from .event import T

class EventEmitter(Event[T]):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def emit(self,param:T) -> None:
        for callback in self._subscribers:
            callback(param)