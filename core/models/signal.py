from .endianness import Endianness
from .bit_order import BitOrder
from .signedness import Signedness

class Signal:
    def __init__(self,
                 name:str,
                 start_bit:int = 0,
                 length_bits:int = 8,
                 physical_value:int|float|bool = 0,
                 factor: float = 1.0,
                 offset: float = 0.0,
                 unit:str = "",
                 endianness: Endianness = Endianness.LITTLE_ENDIAN,
                 bit_order:BitOrder = BitOrder.LSB,
                 signedness:Signedness = Signedness.UNSIGNED,
                 tx_ecu: str = "",
                 rx_ecus: list[str] = []):
        self._name = name
        self._unit = unit
        self._start_bit = start_bit
        self._length_bits = length_bits
        self._physical_value = physical_value
        self._bit_order = bit_order
        self._signedness = signedness
        self._factor = factor
        self._offset = offset
        self._endianness = endianness
        self._tx_ecu = tx_ecu
        self._rx_ecus = rx_ecus

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
    def physical_value(self):
        return self._physical_value

    @property
    def bit_order(self):
        return self._bit_order

    @property
    def signedness(self):
        return self._signedness

    @property
    def raw_value(self):
        return round((self._physical_value - self._offset) / self._factor)

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
