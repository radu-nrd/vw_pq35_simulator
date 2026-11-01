from decoder import Decoder
from core import Message
import can
from cantools.database import Database
from typing import cast, Any


class CanMessageDecoder(Decoder[can.Message,Message]):
    def __init__(self,dbc:Database) -> None:
        super().__init__()
        self._dbc = dbc

    def decode(self, data: can.Message) -> Message:
        msg_def = self._dbc.get_message_by_frame_id(frame_id=data.arbitration_id)
        raw_payload = cast(dict[str,Any],msg_def.decode(data=cast(bytes,data.data)))

