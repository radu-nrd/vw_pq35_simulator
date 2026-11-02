from .signal_info import SignalInfo


class MessageInfo:
    def __init__(self,
                name:str,
                frame_id:int,
                length_dlc:int,
                is_extended_id:bool,
                cycle_time_ms:int,
                tx_ecu:str,
                rx_ecus:list[str],
                signals : dict[str,SignalInfo] | None = None) -> None:

        self._name = name
        self._frame_id = frame_id
        self._length_dlc = length_dlc
        self._is_extended_id = is_extended_id
        self._cycle_time_ms = cycle_time_ms
        self._tx_ecu = tx_ecu
        self._rx_ecus = rx_ecus
        self._signals = signals if signals is not None else {}


    @property
    def name(self):
        return self._name

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def length_dlc(self):
        return self._length_dlc

    @property
    def is_extended_id(self):
        return self._is_extended_id

    @property
    def cycle_time_ms(self):
        return self._cycle_time_ms

    @property
    def tx_ecu(self):
        return self._tx_ecu

    @property
    def rx_ecus(self):
        return self._rx_ecus

    @property
    def signals(self):
        return self._signals