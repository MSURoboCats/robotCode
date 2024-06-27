import serial
import time

class SensorArduino:
    """
    This class provides methods to interface with the Metro Mini v2 that is used to run a variety of sensors.
    Methods return dictionaries with the requested values. Current measurements include control (gyro/accel) and
    hull (temp/pressure/humidity).
    """

    def __init__(self, com_port: str, br: int = 115200, timeout: int = .2):
        """
        Initialize the Metro Mini v2 that is connected to a suite of sensors. Takes ~5s for sensors to get set up

        @param com_port: name of serial port that the Metro Mini v2 is on
        @param br: baud rate that matches the baud rate specified on the Metro Mini v2 (115,200Hz)
        """

        self.port = serial.Serial(com_port, baudrate=br, timeout=timeout)

        self.orientation_x = 0
        self.orientation_y = 0
        self.orientation_z = 0
        self.orientation_w = 0

        self.gyro_x = 0
        self.gyro_y = 0
        self.gyro_z = 0

        self.accelerometer_x = 0
        self.accelerometer_y = 0
        self.accelerometer_z = 0

        self.depth = 0

        self.temp = 0
        self.pressure = 0
        self.humidity = 0

        # allow time for microcontroller to initialize
        time.sleep(5)

        # get initial values (read hull twice since first reading is bad)
        self.get_data()
        self.get_data()

    def get_data(self) -> dict[str: float]:
        """
        Get all data: orientation, gyroscope, accelerometer, depth, temperature (degC), pressure (hPa), and humidity (%)

        @rtype: dict
        @return: dictionary with all the data
        """

        self.__clear_buffer__()
        self.__read_message__()

        out = {"orientation": {"x": self.orientation_x, "y": self.orientation_y, "z": self.orientation_z, "w": self.orientation_w},
               "angular_velocity": {"x": self.gyro_x, "y": self.gyro_y, "z": self.gyro_z},
               "linear_acceleration": {"x": self.accelerometer_x, "y": self.accelerometer_y, "z": self.accelerometer_z},
               "depth": self.depth,
               "temperature": self.temp,
               "pressure": self.pressure,
               "humidity": self.humidity}

        return out

    def __read_message__(self) -> None:


        line = self.port.read(154).decode("utf-8").split(" ")
        values = [float(x) for x in line[1:] if x != '']

        self.orientation_x = values[0]
        self.orientation_y = values[1]
        self.orientation_z = values[2]
        self.orientation_w = values[3]
        self.gyro_x = values[4]
        self.gyro_y = values[5]
        self.gyro_z = values[6]
        self.accelerometer_x = values[7]
        self.accelerometer_y = values[8]
        self.accelerometer_z = values[9]
        self.depth = values[10]
        self.temp = values[11]
        self.pressure = values[12]
        self.humidity = values[13]

    def __clear_buffer__(self) -> None:
        """
        Clear the write buffer by reading all bytes currently in it
        """
        while self.port.inWaiting() != 0:
            self.port.read()