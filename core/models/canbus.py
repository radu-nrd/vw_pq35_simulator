from abc import ABC,abstractmethod
from core import Ecu
from core import BusStatus
from core import Event
from core import EventEmitter
from core import Message
from cantools.database.can import Database
from exceptions import EcuAlreadyConnectedException
from exceptions import EcuNotConnectedException

class CanBus(ABC):
    def __init__(self,
                 id:str,
                 channel_name: str,
                 interface_name: str,
                 baudrate: int | None = 500_000,
                 is_fd: bool | None = False
                 ):
        self._id = id
        self._channel_name:str = channel_name
        self._interface_name:str = interface_name
        self._baudrate = baudrate
        self._is_fd = is_fd
        self._connected_ecus : dict[str,Ecu]  = {}
        self._bus_load : float = 0.0
        self._bus_status : BusStatus = BusStatus.NOT_INIT
        self._frame_broadcasted : EventEmitter[Message] = EventEmitter("frame_broadcasted") 

    @property
    def id(self) -> str:
        return self._id
    @property
    def channel_name(self):
        return self._channel_name

    @property
    def interface_name(self):
        return self._interface_name

    @property
    def baudrate(self):
        return self._baudrate

    @property
    def is_fd(self):
        return self._is_fd

    @property
    def connected_ecus(self) -> list[str]:
        return [ecu_id for ecu_id in self._connected_ecus.keys()]

    @property
    def bus_load(self):
        return self._bus_load

    @property  
    def bus_status(self):
        return self._bus_status

    def frame_broadcasted(self) -> Event[Message]:
        return self._frame_broadcasted

    @abstractmethod
    def attach_ecu(self,ecu:Ecu):
        if self._connected_ecus.get(ecu.id,None) == None:
            self._connected_ecus[ecu.id] = ecu
        raise EcuAlreadyConnectedException(ecu,self)

    @abstractmethod
    def detach_ecu(self,ecu:Ecu):
        if self._connected_ecus.get(ecu.id,None) == None:
            raise EcuNotConnectedException(ecu,self)
        del self._connected_ecus[ecu.id]

    @abstractmethod
    def open(self):
        self._bus_status = BusStatus.ACTIVE

    @abstractmethod
    def close(self):
        self._bus_status = BusStatus.OFF

    @abstractmethod
    def send(self,frame:Message):
        #do something
        self._frame_broadcasted.emit(frame)