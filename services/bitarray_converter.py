from core.models.endianness import Endianness
from bitstring import Bits, BitArray


def to_bitarray(value:object,signed:bool,length_bits:int,endianness:Endianness):
    val_type = type(value)

    if val_type is bool:
        return BitArray(Bits(bool = value))
    elif val_type is int:
        bits_type = __build_bits_type("int",signed,endianness)
        return BitArray(Bits(f"{bits_type}:{length_bits} = {value}"))
    elif val_type is float:
        if length_bits not in [16,32,64]:
            raise ValueError(f'Cannot convert a float value with length_bits = {length_bits}. The float converter only accepts length_bits = [16,32,64]')
        bits_type = __build_bits_type("float",signed,endianness)
        return BitArray(Bits(f"{bits_type}:{length_bits} = {value}"))

    raise TypeError(f"Unsupported type: {type(value)}")


def __build_bits_type(value_type:str,signed:bool,endianness:Endianness):

    if value_type != "int" and value_type != "float":
        raise Exception(f'Cannot compute bits_type for the value type {value_type}')
    
    bits_type : str = value_type

    if bits_type == "int" and not signed:
        bits_type = "u" + bits_type

    match endianness:
        case Endianness.LITTLE_ENDIAN:
            bits_type += "le"
        case Endianness.BIG_ENDIAN:
            bits_type += "be"
        case _:
            raise Exception(f'Invalid endianness. Value: {endianness}')

    return bits_type
    