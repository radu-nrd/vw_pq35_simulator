class EcuAlreadyConnectedException(Exception):
    def __init__(self,ecu_id:str,ecu_name:str,bus_id:str,bus_name:str):
        super().__init__(f'Ecu {ecu_id}({ecu_name}) is already connected on bus {bus_id}({bus_name})')