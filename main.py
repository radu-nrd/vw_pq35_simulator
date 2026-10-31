import cantools
from cantools.database.can.database import Database
from cantools.database.can.message import Message
from typing import cast

dbc : Database = cast(Database, cantools.database.load_file("config/vw_pq.dbc"))

motor_1_msg : Message = dbc.get_message_by_frame_id(frame_id=640)
print('stop')

