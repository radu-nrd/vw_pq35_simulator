from abc import ABC
from .signal import Signal
from typing import Any

class Message(ABC):
    def __init__(self,
                 frame_id:int,
                 name:str,
                 length_dlc:int = 8,
                 is_extended_id:bool = False,
                 cycle_time_ms : int = 100,
                 signals : dict[str,Signal]|None = None,
                 tx_ecu:str="",
                 rx_ecus:list[str]|None=None):
        self._frame_id = frame_id
        self._name = name
        self._is_extended_id = is_extended_id
        self._length_dlc = length_dlc
        self._cycle_time_ms = cycle_time_ms
        self._signals = signals if signals is not None else {}
        self._rx_ecus = rx_ecus if rx_ecus is not None else []
        self._tx_ecu = tx_ecu

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def name(self):
        return self._name

    @property
    def is_extended_id(self):
        return self._is_extended_id

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
    def signals(self) -> dict[str,Signal]:
        return self._signals

    def to_dict(self) -> dict[str,Any]:
        cache_dict : dict[str,Any] = {}
        for sig in self._signals.values():
            cache_dict[sig.name] = sig.raw_value
        return cache_dict

    def add_signal(self,sig:Signal):
        if sig.name in self._signals.keys():
            raise Exception('Signal is already defined in the message')
        self._signals[sig.name] = sig