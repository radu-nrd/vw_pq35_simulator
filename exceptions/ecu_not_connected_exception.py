from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.models.ecu import Ecu
    from core.models.canbus import CanBus


class EcuNotConnectedException(Exception):
    def __init__(self,ecu_id:str,ecu_name:str,bus_id:str,bus_name:str) -> None:
        super().__init__(f'Ecu {ecu_id}({ecu_name}) cannot be detached because it is not connected to the {bus_id}({bus_name}) bus')