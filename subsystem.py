import time

import serial
from serial import Serial

from static_utilities import StaticUtilities


class Subsystem:

    def __init__(self, name: str, port: str, baud_rate: int, timeout: float = 5) -> None:
        self.running: bool = True
        self.name: str = name
        self.port: str = port
        self.baud_rate: int = baud_rate
        self.timeout: float = timeout
        self.serial_connection_established: bool = False

    def initialize_serial_connection(self, identification_string: str, startup_method=None):
        serial_object = self._initialize_serial_connection(startup_method=startup_method)
        if not self.serial_connection_established:
            available_serial_devices = StaticUtilities.serial_devices()
            for device in available_serial_devices:
                if identification_string not in device[1].lower():
                    StaticUtilities.logger.debug(f"No device matching '{identification_string}' on {device[0]}")
                    continue
                StaticUtilities.logger.info(f"Found {device[1]} on {device[0]}. Attempting connection.")
                serial_object = self._initialize_serial_connection(port=device[0], startup_method=startup_method)
                if self.serial_connection_established:
                    return serial_object
        else:
            return serial_object

    def _initialize_serial_connection(self, port=None, startup_method=None):
        if port is None:
            self.port = port
        try:
            serial_object = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            if startup_method is not None:
                startup_method()
            serial_object.flush()
        except serial.serialutil.SerialException:
            StaticUtilities.logger.error(f"Failed to initialize {self.name} on {self.port} at {self.baud_rate}")
            self.serial_connection_established = False
        else:
            StaticUtilities.logger.info(f"{self.name} initialized on {self.port} at {self.baud_rate}")
            self.serial_connection_established = True
            return serial_object
