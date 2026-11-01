import socket
import struct

class RawSocketCanInterface:
    # Formatul binar al structurii can_frame din kernel-ul Linux
    CAN_FRAME_FMT = "=IB3x8s"

    def __init__(self, interface: str = "vcan0"):
        # Deschidere socket nativ SocketCAN
        self.sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.sock.bind((interface,))

    def send_frame(self, frame_id: int, payload: bytes) -> None:
        """Trimite direct octeții fără niciun can.Message."""
        dlc = len(payload)
        
        # Un cadru CAN clasic are un buffer de date de 8 bytes (completăm cu zerouri dacă are sub 8)
        data = payload.ljust(8, b'\x00')
        
        # Împachetăm structura de 16 octeți pentru kernel
        can_frame = struct.pack(self.CAN_FRAME_FMT, frame_id, dlc, data)
        
        # Trimitem direct prin socket-ul Linux
        self.sock.send(can_frame)

    def close(self):
        self.sock.close()