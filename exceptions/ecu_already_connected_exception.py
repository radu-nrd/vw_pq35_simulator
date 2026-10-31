from core.models.ecu import Ecu
from core.models.canbus import CanBus

class EcuAlreadyConnectedException(Exception):
    def __init__(self,ecu:Ecu,bus:CanBus):
        super().__init__(f'Ecu {ecu.id}({ecu.name}) is already connected on bus {bus.id}({bus.channel_name})')