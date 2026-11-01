
from encoder import Encoder
from core import Message
from core import Signedness
from services import compute_physical_bits_mapping


class CanMessageEncoder(Encoder[Message,bytes]):
    def __init__(self) -> None:
        super().__init__()

    def encode(self, frame: Message) -> bytes:
        buffer = bytearray(frame.length_dlc)
        for sig in frame.signals.values():
            raw_value = sig.raw_value

            if sig.signedness == Signedness.SIGNED and raw_value < 0:
                raw_value = self.__compute_signed_value(raw_value,sig.length_bits)

            raw_value = self.__trunk_value(raw_value,sig.length_bits)
            bit_positions = compute_physical_bits_mapping(sig.start_bit,sig.length_bits,sig.endianness,sig.bit_order)

            for logical_bit_idx, physical_can_bit in enumerate(bit_positions):
                bit_value = (raw_value >> logical_bit_idx) & 1
                byte_pos = physical_can_bit // 8
                bit_pos = physical_can_bit % 8

                if byte_pos < len(buffer):
                    if bit_value:
                        buffer[byte_pos] |= (1 << bit_pos)
                    else:
                        buffer[byte_pos] &= ~(1 << bit_pos) & 0xFF

        return bytes(buffer)


    def __compute_signed_value(self,raw_value:int,length_bits:int):
        return (1 << length_bits) + raw_value

    def __trunk_value(self,raw_value:int,length_bits:int):
        return raw_value & ((1 << length_bits) - 1)

        
    # def encode(self, data: Message) -> can.Message:
    #     msg_def = self._dbc.get_message_by_frame_id(frame_id=data.frame_id)
    #     raw_payload : bytes = msg_def.encode(data.to_dict())

    #     return can.Message(
    #         arbitration_id=data.frame_id,
    #         is_extended_id=data.is_extended_id,
    #         timestamp=time.time(),
    #         data=raw_payload)
        