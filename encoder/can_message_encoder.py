
from encoder import Encoder
from core import Message
import can
from cantools.database import Database
import time


class CanMessageEncoder(Encoder[Message,can.Message]):
    def __init__(self,dbc:Database) -> None:
        super().__init__()
        self._dbc = dbc

    def encode(self, data: Message) -> can.Message:
        msg_def = self._dbc.get_message_by_frame_id(frame_id=data.frame_id)
        raw_payload : bytes = msg_def.encode(data.to_dict())

        return can.Message(
            arbitration_id=data.frame_id,
            is_extended_id=data.is_extended_id,
            timestamp=time.time(),
            data=raw_payload)
        