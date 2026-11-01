class RawSocketCanReceiver:
    CAN_FRAME_FMT = "=IB3x8s"

    def __init__(self, interface: str = "vcan0"):
        self.sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.sock.bind((interface,))

    def receive_frame(self) -> tuple[int, bytes]:
        """Așteaptă un cadru și returnează (frame_id, bytes)."""
        frame = self.sock.recv(16)  # Dimensiunea exactă a structurii can_frame
        
        can_id, dlc, data = struct.unpack(self.CAN_FRAME_FMT, frame)
        
        # Curățăm flag-urile de kernel (EFF/RTR/ERR) pentru a păstra doar ID-ul de 11 biți
        clean_id = can_id & 0x7FF
        clean_payload = data[:dlc]

        return clean_id, clean_payload