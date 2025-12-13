import serial
import time

from core.printer_commands import PrinterCommands

class PrinterCommunication:
    def __init__(self) -> None:
        self.commands = PrinterCommands
        self.serial = serial.Serial("/dev/cu.usbmodem1101", 250000, timeout=2)

    def __del__(self)->None:
        self.serial.close()

    def send_commands(self, commands:list[str])->None:
        for cmd in commands:
            self.serial.write(f"{cmd}\n".encode())
            time.sleep(1)
            print(self.serial.readline().decode())
