from pathlib import Path
from typing import cast, Dict, Any
import cantools
from cantools.database.can.database import Database

# 1. Încărcarea bazei de date DBC
BASE_DIR = Path(__file__).resolve().parent
DBC_PATH = BASE_DIR / "config" / "vw_pq_v2.dbc"
dbc = cast(Database, cantools.database.load_file(str(DBC_PATH)))

# -------------------------------------------------------------
# PARTEA 1: Transmisia (Engine ECM J623)
# -------------------------------------------------------------
# Definiția mesajului extrasă din DBC
motor_1_def = dbc.get_message_by_name("Motor_1")
frame_id = motor_1_def.frame_id  # 640 (sau 0x280)

# Semnalele fizice generate intern de motor
signals_to_send: Dict[str, Any] = {
    "Motordrehzahl": 2450.0,                    # Turație (RPM)
    "Fahrpedalwert_oder_Drosselklapp": 35.0,    # Apăsare pedală (%)
    "inneres_Motor_Moment": 85.0,              # Cuplu indicat (Nm)
    "Fahrerwunschmoment": 75.0,
    "mechanisches_Motor_Verlustmomen": 8.0,
    "inneres_Motor_Moment_ohne_exter": 85.0,
    "Kupplungsschalter": 0,                     # Ambreiaj eliberat
    "Kickdownschalter": 0,
    "Leergasinformation": 0,
    "Momentenangaben_ungenau": 0,
    "Fehlerstatus_Getriebe_Momentene": 0,
    "Fehlerstatus_Brems_Momenteneing": 0,
    "Time_Out_Bremsen_Botschaft": 0,
    "Fahrpedalwert_ungenau__Motor_1_": 0
}

# Funcția cheie de ENCODARE: transformă valorile în 8 octeți conform DBC
raw_payload: bytes = motor_1_def.encode(signals_to_send)

print(f"[TX - Engine ECM] Trimis frame {hex(frame_id)}:")
print(f"  Payload binar (8 bytes): {raw_payload.hex(' ')}")


# -------------------------------------------------------------
# PARTEA 2: Tranzitul pe magistrală (Simulare sârmă / CAN Bus)
# -------------------------------------------------------------
# Pe magistrală circulă doar două informații elementare:
wire_arbitration_id = frame_id
wire_data = raw_payload


# -------------------------------------------------------------
# PARTEA 3: Recepția și Decodificarea (Cluster Bord J285)
# -------------------------------------------------------------
# 1. Când sosește cadrul, Clusterul caută definiția mesajului după ID
rx_msg_def = dbc.get_message_by_frame_id(wire_arbitration_id)

# 2. Funcția cheie de DECODIFICARE:
#    rx_msg_def.decode(data) aplică factor, offset și mască pe biți
decoded_signals: Dict[str, Any] = cast(dict[str,Any],rx_msg_def.decode(wire_data))

print(f"\n[RX - Cluster J285] Recepționat mesaj '{rx_msg_def.name}':")
# 3. Clusterul extrage direct semnalele de care are nevoie pentru afișaj
rpm = decoded_signals.get("Motordrehzahl")
pedal = decoded_signals.get("Fahrpedalwert_oder_Drosselklapp")
torque = decoded_signals.get("inneres_Motor_Moment")

print(f"  -> Turometru actualizat: {rpm} RPM")
print(f"  -> Pedală accelerație:   {pedal} %")
print(f"  -> Cuplu motor afișat:   {torque} Nm")