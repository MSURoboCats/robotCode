import serial
import time


class SensorArduino:
    """
    This class provides methods to interface with the Metro Mini v2 that is used to run a variety of sensors.
    Methods return dictionaries with the requested values. Current measurements include control (gyro/accel) and
    hull (temp/pressure/humidity).
    """

    def __init__(self, com_port: str, br: int = 115200, timeout: int = 5):
        """
        Initialize the Metro Mini v2 that is connected to a suite of sensors. Takes ~5s for sensors to get set up

        @param com_port: name of serial port that the Metro Mini v2 is on
        @param br: baud rate that matches the baud rate specified on the Metro Mini v2 (115,200Hz)
        """

        self.port = serial.Serial(com_port, baudrate=br, timeout=timeout)
        self.__clear_buffer__()

        self.orientation_x = 0
        self.orientation_y = 0
        self.orientation_z = 0

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

        time.sleep(5)

        # get initial values (read hull twice since first reading is bad)
        self.get_control_data()
        self.get_hull_data()
        self.get_hull_data()

    def get_control_data(self) -> dict:
        """
        Get the control data: orientation, gyroscope, accelerometer, depth

        @rtype: dict
        @return: dictionary with the control data
        """

        self.__clear_buffer__()
        self.port.write("<C>".encode("utf-8"))
        self.__read_message__()

        out = {"orientation": {"x": self.orientation_x, "y": self.orientation_y, "z": self.orientation_z, "w": self.orientation_w},
               "angular_velocity": {"x": self.gyro_x, "y": self.gyro_y, "z": self.gyro_z},
               "linear_acceleration": {"x": self.accelerometer_x, "y": self.accelerometer_y, "z": self.accelerometer_z},
               "depth": self.depth}

        return out

    def get_hull_data(self) -> dict:
        """
        Get the hull data: temperature, pressure, and humidity

        @rtype: dict
        @return: dictionary with the hull data
        """

        self.__clear_buffer__()
        self.port.write("<H>".encode("utf-8"))
        self.__read_message__()

        out = {"temperature": self.temp,
               "pressure": self.pressure,
               "humidity": self.humidity}

        return out

    def print_control_data(self) -> None:
        """
        Print out the current control data
        """

        print("Value\t\tx\ty\tz\nOrientation\t%.2f\t%.2f\t%.2f\t%.2f\n(deg)\nGyroscope\t%.2f\t%.2f\t%.2f\n(rad/s)\nAccel.\t\t%.2f\t%.2f\t%.2f\n(m/s^2)\n\nDepth: %.2f m" %
              (self.orientation_x,
               self.orientation_y,
               self.orientation_z,
               self.orientation_w,
               self.gyro_x,
               self.gyro_y,
               self.gyro_z,
               self.accelerometer_x,
               self.accelerometer_y,
               self.accelerometer_z,
               self.depth))
        return

    def print_hull_data(self) -> None:
        """
        Print out the current hull data
        """
        print("Temp:\t\t%.2f C\nPressure:\t%.2f hPa\nHumidity:\t%.2f%%\n" %
              (self.temp,
               self.pressure,
               self.humidity))
        return

    def __read_message__(self) -> None:

        line = self.port.readline().decode("utf-8").removesuffix("\n").split(" ")

        # error message
        if line[0] == "!":
            print("Error!")

        # control message
        elif line[0] == "C":
            values = [float(x) for x in line[1:]]
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

        # hull message
        elif line[0] == "H":
            values = [float(x) for x in line[1:]]
            self.temp = values[0]
            self.pressure = values[1]
            self.humidity = values[2]

        else:
            pass

    def __clear_buffer__(self):
        """
        Clear the write buffer by reading all bytes currently in it
        """
        while self.port.inWaiting() != 0:
            self.port.read()