from abc import ABC
from core.models.message import Message

class Ecu(ABC):
    def __init__(self,
                 id:str,
                 name:str,
                 description:str,
                 tx_frames:dict[str,Message] = {},
                 rx_frames:dict[str,Message] = {}
                 ):
        self._id : str = id
        self._name:str = name
        self._description:str = description
        self._tx_frames = tx_frames
        self._rx_frames = rx_frames

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def tx_frames(self) -> list[str]:
        return [frame_id for frame_id in self._tx_frames.keys()]

    @property
    def rx_frames(self) -> list[str]:
        return [frame_id for frame_id in self._rx_frames.keys()]