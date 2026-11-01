from core import Endianness
from core import BitOrder
from core import Signedness
from services import compute_physical_bits_mapping

class SignalInfo:
    def __init__(self,
                 name:str,
                 start_bit:int,
                 length_bits:int,
                 factor:int,
                 offset:int,
                 endianness: Endianness,
                 bit_order:BitOrder,
                 signedness:Signedness,
                 tx_ecu: str,
                 rx_ecus: list[str],
                 unit:str = "") -> None:
        self._name = name
        self._start_bit = start_bit
        self._length_bits = length_bits
        self._factor = factor
        self._offset = offset
        self._endianness = endianness
        self._bit_order = bit_order
        self._signedness = signedness
        self._tx_ecu = tx_ecu
        self._rx_ecus = rx_ecus
        self._unit = unit
        self._bit_positions = compute_physical_bits_mapping(self._start_bit,self._length_bits,self._endianness,self._bit_order)

    @property
    def name(self):
        return self._name

    @property
    def start_bit(self):
        return self._start_bit

    @property
    def length_bits(self):
        return self._length_bits

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
    def bit_order(self):
        return self._bit_order

    @property
    def signedness(self):
        return self._signedness

    @property
    def tx_ecu(self):
        return self._tx_ecu

    @property
    def rx_ecus(self):
        return self._rx_ecus

    @property
    def unit(self):
        return self._unit

    @property
    def bit_positions(self) -> list[int]:
        return self._bit_positions