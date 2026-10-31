from abc import ABC
from core import Endianness
from core import RawType

class Signal(ABC):
    def __init__(self,
                 name:str,
                 unit:str = "",
                 start_bit:int = 0,
                 length_bits:int = 8,
                 raw_value:RawType = 0,
                 factor: float = 1.0,
                 offset: float = 0.0,
                 endianness: Endianness = Endianness.LITTLE_ENDIAN,
                 tx_ecu: str = "",
                 rx_exus: list[str] = []):
        self._name = name
        self._unit = unit
        self._start_bit = start_bit
        self._length_bits = length_bits
        self._raw_value = raw_value
        self._factor = factor
        self._offset = offset
        self._endianness = endianness
        self._tx_ecu = tx_ecu
        self._rx_ecus = rx_exus

    @property
    def name(self):
        return self._name

    @property
    def unit(self):
        return self._unit

    @property
    def start_bit(self):
        return self._start_bit

    @property
    def length_bits(self):
        return self._length_bits

    @property
    def raw_value(self):
        return self._raw_value

    @property
    def factor(self):
        return self._factor

    @property
    def offset(self):
        return self._offset

    @property
    def endianness(self):
        return self._endianness

    @property
    def tx_ecu(self):
        return self._tx_ecu

    @property
    def rx_ecus(self):
        return self._rx_ecus
