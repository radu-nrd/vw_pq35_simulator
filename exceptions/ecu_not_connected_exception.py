from core import Ecu
from core import CanBus


class EcuNotConnectedException(Exception):
    def __init__(self,ecu:Ecu,bus:CanBus) -> None:
        super().__init__(f'Ecu {ecu.id}({ecu.name}) cannot be detached because it is not connected to the {bus.id}({bus.channel_name}) bus')