from decoder import Decoder
from core import Message
from core import EncodedMessage
from core import MessageInfo
from core import Signal
from core import SignalInfo
from core import Signedness
from core import PhysicalValueTypes


class CanMessageDecoder(Decoder[EncodedMessage,Message]):
    def __init__(self,registry:dict[int,MessageInfo] | None = None) -> None:
        super().__init__()
        self._registry = registry if registry is not None else {}

    def decode(self, data: EncodedMessage) -> Message | None:
        template = self._registry.get(data.frame_id,None)

        if template is None:
            return None

        decoded_message : Message = self.__build_decoded_message(template)

        for sig_def in template.signals.values():
            raw_value = 0
            for logical_bit_idx, physical_can_bit in enumerate(sig_def.bit_positions):
                byte_pos = physical_can_bit // 8
                bit_pos = physical_can_bit % 8

                if byte_pos < len(data.data):
                    bit_value = (data.data[byte_pos] >> bit_pos) & 1
                    raw_value |= (bit_value << logical_bit_idx)

            if sig_def.signedness == Signedness.SIGNED:
                raw_value = self.__to_signed(raw_value,sig_def.length_bits)

            physical_value = (raw_value * sig_def.factor) + sig_def.offset
            sig = self.__build_signal(physical_value,sig_def)          
            decoded_message.add_signal(sig)

        return decoded_message

    def __build_decoded_message(self,message_info:MessageInfo):
        return Message(
            frame_id=message_info.frame_id,
            length_dlc=message_info.length_dlc,
            is_extended_id=message_info.is_extended_id,
            cycle_time_ms=message_info.cycle_time_ms,
            tx_ecu=message_info.tx_ecu,
            rx_ecus=list(message_info.rx_ecus)
        )

    def __build_signal(self,physical_value:PhysicalValueTypes,signal_info:SignalInfo):
        return Signal(
                name=signal_info.name,
                start_bit=signal_info.start_bit,
                length_bits=signal_info.length_bits,
                factor=signal_info.factor,
                offset=signal_info.offset,
                unit=signal_info.unit,
                physical_value=physical_value,
                endianness=signal_info.endianness,
                bit_order=signal_info.bit_order,
                signedness=signal_info.signedness,
                tx_ecu=signal_info.tx_ecu,
                rx_ecus=list(signal_info.rx_ecus)
            )

    def __to_signed(self,val: int, length_bits: int) -> int:
        sign_bit = 1 << (length_bits - 1)
        if val & sign_bit:
            return val - (1 << length_bits)
        return val


    

