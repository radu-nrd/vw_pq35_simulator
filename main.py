from core import MessageInfo
from core import SignalInfo
from core import Endianness
from core import BitOrder
from core import Signedness
from core import Signal
from core import Message
from core import EncodedMessage
from encoder import CanMessageEncoder
from decoder import CanMessageDecoder

motor_rpm_signal_info = SignalInfo(
    name='motor_rpm',
    start_bit=16,
    length_bits=16,
    factor=0.25,
    offset=0.0,
    unit='RPM',
    endianness = Endianness.LITTLE_ENDIAN,
    bit_order= BitOrder.LSB,
    signedness= Signedness.UNSIGNED,
    tx_ecu='ECU_A',
    rx_ecus=['ECU_B']
)

motor_frame_info = MessageInfo(
    frame_id=0x280,
    name='motor_1',
    length_dlc=8,
    is_extended_id=False,
    cycle_time_ms=50,
    tx_ecu='ECU_A',
    rx_ecus=['ECU_B'],
    signals={"motor_rpm" : motor_rpm_signal_info}
)

motor_rpm_signal = Signal(
    name='motor_rpm',
    start_bit=16,
    length_bits=16,
    factor=0.25,
    offset=0.0,
    unit='RPM',
    endianness=Endianness.LITTLE_ENDIAN,
    bit_order=BitOrder.LSB,
    signedness=Signedness.UNSIGNED,
    tx_ecu='ECU_A',
    rx_ecus=['ECU_B'],
    physical_value=820.5
)

motor_frame = Message(
    frame_id=0x280,
    name='motor_1',
    length_dlc=8,
    is_extended_id=False,
    cycle_time_ms=50,
    tx_ecu='ECU_A',
    rx_ecus=['ECU_B'],
    signals={'motor_rpm' : motor_rpm_signal}
)

registry : dict[int,MessageInfo] = { 0x280:motor_frame_info }
encoder = CanMessageEncoder()
decoder = CanMessageDecoder(registry)


encoded_bytes = encoder.encode(motor_frame)
print(f'Motor_1 encoded bytes: {encoded_bytes.hex(' ')}')


rx_package = EncodedMessage(0x280,encoded_bytes)

decoded_msg = decoder.decode(rx_package)
if decoded_msg:
    print('Motor_1 decoded successfully')
    print(f'Motor_1 physical value: {decoded_msg.signals['motor_rpm'].physical_value}')




