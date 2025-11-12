from core.chess_logic import ChessLogic, Stockfish


import serial
import time


def main_temp():
    # Stockfish()
    ser = serial.Serial("/dev/cu.usbmodem1101", 250000, timeout=2)

    commands = [
        "G90",
        "G0 X111 Y111 Z100 F3000",
        "G91",
        "G0 X0 Y0 Z-100 F3000",
        "G0 X0 Y-30 Z0 F3000",
        "G0 X0 Y0 Z100 F3000",
        "G0 X50 Y50 Z0 F3000",
        "G0 X0 Y0 Z-100 F3000",
        "G0 X0 Y50 Z0 F3000",
    ]

    for cmd in commands:
        ser.write(f"{cmd}\n".encode())
        time.sleep(1)  # wait a bit for the printer to execute
        print(ser.readline().decode())

    ser.close()

def main() -> None:
    # chess_logic = ChessLogic()
    Stockfish()





if __name__ == "__main__":
    main()
