from abc import ABC,abstractmethod
from core import Ecu
from core import BusStatus
from cantools.database.can import Database
from exceptions import EcuAlreadyConnectedException

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


    @property
    def id(self):
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
        return [ecu.id for ecu in self._connected_ecus]

    @property
    def bus_load(self):
        return self._bus_load

    @property
    def bus_status(self):
        return self._bus_status

    @abstractmethod
    def attach_ecu(self,ecu:Ecu):
        if self._connected_ecus.get(ecu.id,None) == None:
            self._connected_ecus[ecu.id] = ecu
        raise EcuAlreadyConnectedException(ecu,self)