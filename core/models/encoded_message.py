
class EncodedMessage:
    def __init__(self,frame_id:int,data:bytes) -> None:
        self._frame_id = frame_id
        self._data = data

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def data(self):
        return self._data