from abc import ABC,abstractmethod
from core.models.signal import Signal

class Message(ABC):
    def __init__(self,
                 frame_id:str,
                 length_dlc:int,
                 cycle_time_ms : int = 100,
                 signals : dict[str,Signal] | None = {},
                 tx_ecu:str="",
                 rx_ecus:list[str]=[]):
        self._frame_id = frame_id
        self._length_dlc = length_dlc
        self._cycle_time_ms = cycle_time_ms
        self._signals = signals
        self._rx_ecus = rx_ecus
        self._tx_ecu = tx_ecu
        self._paylaod = bytearray()

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def length_dlc(self):
        return self._length_dlc

    @property
    def cycle_time_ms(self):
        return self._cycle_time_ms

    @property
    def rx_ecus(self):
        return self._rx_ecus

    @property
    def tx_ecu(self):
        return self._tx_ecu

    @property
    def signals(self) -> list[str]:
        return [signal_name for signal_name in self._signals.keys()]