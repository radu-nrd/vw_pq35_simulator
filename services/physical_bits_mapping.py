from core import Endianness
from core import BitOrder

def compute_physical_bits_mapping(
    start_bit:int,
    length_bits:int,
    byte_order:Endianness,
    bit_order:BitOrder
) -> list[int]:
    
    match byte_order:
        case Endianness.LITTLE_ENDIAN:
            return __compute_physical_bits_little_endian(start_bit,length_bits,bit_order)
        case Endianness.BIG_ENDIAN:
            return __compute_physical_bits_big_endian(start_bit,length_bits,bit_order)


def __compute_physical_bits_little_endian(
    start_bit:int,
    length_bits:int,
    bit_order:BitOrder
) -> list[int]:
    
    match bit_order:
        case BitOrder.LSB:
            return __compute_physical_bits_little_endian_lsb(start_bit,length_bits)
        case BitOrder.MSB:
            return __compute_physical_bits_little_endian_msb(start_bit,length_bits)

    raise Exception('Invalid bit order')

def __compute_physical_bits_big_endian(
    start_bit:int,
    length_bits:int,
    bit_order:BitOrder
) -> list[int]:

    match bit_order:
        case BitOrder.LSB:
            return __compute_physical_bits_big_endian_lsb(start_bit,length_bits)
        case BitOrder.MSB:
            return __compute_physical_bits_big_endian_msb(start_bit,length_bits)
    raise Exception('Invalid bit order')

def __compute_physical_bits_little_endian_lsb(
    start_bit:int,
    length_bits:int
) -> list[int]:
    return [start_bit + i for i in range(length_bits)]

def __compute_physical_bits_little_endian_msb(
    start_bit:int,
    length_bits:int
) -> list[int]:
    bits : list[int] = []
    for i in range(length_bits):
        bits.append(start_bit-i)
    return bits

def __compute_physical_bits_big_endian_msb(
    start_bit:int,
    length_bits:int
) -> list[int]:

    msb_to_lsb : list[int] = []
    byte_idx = start_bit // 8
    bit_idx = start_bit % 8
    for _ in range(length_bits):
        msb_to_lsb.append(byte_idx * 8 + bit_idx)
        bit_idx -= 1
        if bit_idx < 0:
            bit_idx = 7
            byte_idx += 1
    return list(reversed(msb_to_lsb))

def __compute_physical_bits_big_endian_lsb(
    start_bit:int,
    length_bits:int
) -> list[int]:

    lsb_to_msb : list[int] = []
    byte_idx = start_bit // 8
    bit_idx = start_bit % 8
    for _ in range(length_bits):
        lsb_to_msb.append(byte_idx * 8 + start_bit)
        bit_idx += 1
        if bit_idx > 7:
            bit_idx = 0
            byte_idx -= 1

    return lsb_to_msb