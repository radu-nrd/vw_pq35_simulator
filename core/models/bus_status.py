from enum import Enum

class BusStatus(Enum):
    ACTIVE = 'ACTIVE'
    OFF = 'OFF'
    BUSY = 'BUSY'
    NOT_INIT = 'NOT_INIT'