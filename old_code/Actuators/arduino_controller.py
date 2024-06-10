from enum import Enum

import serial
import time

from static_utilities import StaticUtilities


class ArduinoAction(Enum):
    """
    Enumerated representation of all the possible actions for the Arduino.
    Allows conversion of useful names to string that the Arduino understands and can be sent to the Arduino over serial.
    For example: the value of ArduinoActions.DIVE is the str "dive".
    Sending this to the Arduino over serial with the method ArduinoController.send_arduino_command()
    """
    START = "start"
    FORWARD = "forward"
    REVERSE = "reverse"
    NEUTRAL = "neutral"
    DIVE = "dive"
    HOVER_FORWARD = "hoverForward"
    HOVER_SPIN = "hoverSpin"
    SURFACE = "surface"
    KILL = "kill"
    TEST_ALL_THRUSTERS = "all"
    SEQUENTIALLY_TEST_ALL_THRUSTERS = "seqTest"
    CONTROL_WITH_IMU = "imuControl"
    PRESSURE = "pressure"
    TEMPERATURE = "temperature"
    DEPTH = "depth"
    ALTITUDE = "altitude"
    ALL_PRESSURE_DEPTH_MEASURES = "measures"
    DRIVE_THRUSTER = "driveMotor"


class ArduinoController:
    """
    Class that can be instantiated to control an Arduino and send it commands over serial.
    """

    def __init__(self, *, arduino_port: str = '/dev/ttyACM0', baud_rate: int = 115200, time_out: int = 1,
                 name: str = "Arduino Controller", arduino_type: str = "Mega"):
        """
        Initializes the Arduino and connection.
        Starts the Arduino.
        arduino_port, baud_rate, time_out default values can be overridden by passing values into the constructor on instantiation.
        """
        self.name: str = name
        self.arduino_type: str = arduino_type
        self.arduino_port: str = arduino_port
        self.baud_rate: int = baud_rate
        self.time_out: int = time_out
        try:
            self.arduino = serial.Serial(self.arduino_port, self.baud_rate, timeout=self.time_out)
            self.receive(receipt="arduino starting...")
            time.sleep(self.time_out)
            self.arduino.flush()
            self.send(ArduinoAction.START)
            self.receive(receipt="arduino ready")
            self.arduino.flush()
        except serial.serialutil.SerialException:
            StaticUtilities.logger.error(f"Failed to initialize {self.name} Arduino {self.arduino_type} on {self.arduino_port} at {self.baud_rate}")
        else:
            StaticUtilities.logger.info(f"{self.name} Arduino {self.arduino_type} initialized on {self.arduino_port} at {self.baud_rate}")

    def receive(self, *, receipt: str = "status: done", receive_data: bool = False) -> str:
        """
        Waits to receive a response from the Arduino via serial that matches the str receipt.
        If the str Keyword Arg receipt is not modified it defaults to the value "status: done".
        If the Arduino returns the str "killed" this method will return.

        Note: I'm realizing it may be beneficial to implement multiprocessing in the RobotController Class.
        If that happens all methods in this class should impose a lock until an ack is received.

        :param: receipt: str to wait to receive from the Arduino via serial. Represents a TCP ACK.
        :return: str representation of the value received from the Arduino over serial.
        """
        data: str = ""
        s: str = ""
        while s != receipt:
            data = s
            s = self.arduino.readline().decode('utf-8').rstrip()
            if s != "":
                StaticUtilities.logger.debug(f"{self.name}: {s}")
            if s == "status: killed":
                return "killed"
            time.sleep(self.time_out * 0.01)
        return data if receive_data else s

    def send(self, command: ArduinoAction) -> None:
        """
        Sends the string command to the Arduino over serial.
        :param: command: str representation of a command to send to the Arduino.
        :return: None.
        """
        command: str = command.value
        command += "\n"
        self.arduino.write(command.encode('UTF-8'))
        return

    def kill(self) -> None:
        """
        Sends a kill command to the Arduino until a killed acknowledgement is received.
        Then closes the connection to the Arduino.
        Best chance of halting the Arduino as fast as possible with software without removing power.
        Designed as a safety measure. Basically a Software Level E-STOP.
        :return: None.
        """
        self.arduino.flush()
        s: str = ""
        while s != "status: killed":
            s = self.arduino.readline().decode('utf-8').rstrip()
            self.send(ArduinoAction.KILL.value)
            time.sleep(0.01)
        self.arduino.flush()
        self.arduino.close()
        StaticUtilities.logger.warning(f"Arduino {self.arduino_type} on {self.arduino_port} killed. Restart Arduino {self.arduino_type} to continue.")

    def legacy_send_arduino_command(self, entry: str):
        """
        Old version of send_arduino_command()
        :param entry: str representation of command to send to the Arduino.
        :return: None.
        """
        if entry == "fwd":
            self.arduino.write(b"forward\n")
        elif entry == "rvs":
            self.arduino.write(b"reverse\n")
        elif entry == "neut":
            self.arduino.write(b"neutral\n")
        elif entry == "dive":
            self.arduino.write(b"dive\n")
        elif entry == "hover_f":
            self.arduino.write(b"hoverForward\n")
        elif entry == "hover_s":
            self.arduino.write(b"hoverSpin\n")
        elif entry == "test_all":
            self.arduino.write(b"all\n")
        elif entry == "seq_test":
            self.arduino.write(b"seqTest\n")
        elif entry == "kill":
            self.arduino.write(b"kill\n")
        else:
            StaticUtilities.logger.info(f"command not recognized")
        self.receive()

    def send_arduino_command(self, arduino_action: ArduinoAction, arduino_receipt: str = "status: done") -> bool:
        """
        Poor man's implementation of TCP networking protocol over serial.
        Essentially, send a str to the Arduino via serial and wait for a response.
        :param: arduino_action: Value from ArduinoActions Enum Class. See Class doc for explanation and example.
        :param: arduino_receipt:
        :return bool representation of the success of sending the command to the Arduino. If the Arduino was killed at any point return False, otherwise True.
        """
        self.send(arduino_action)
        return False if self.receive(receipt=arduino_receipt) == "killed" else True

    # TODO: most of the following methods should probably be moved into a child class but is fine as long as there is only one arduino
    def drive_thruster(self, thruster_number: int, thruster_percentage: int):  # TODO
        if thruster_percentage > 100 or thruster_percentage < -100:
            return
        if thruster_number < 1 or thruster_number > 8:
            return
        self.arduino.write(f"{ArduinoAction.DRIVE_THRUSTER.value.encode('UTF-8')}:{thruster_number}>{thruster_percentage};")
        return

    def send_imu_control(self, data: str):  # TODO
        self.arduino.write(f"{ArduinoAction.CONTROL_WITH_IMU.value}::{data}\n".encode('UTF-8'))
        return

    def altitude(self) -> float:
        self.send(ArduinoAction.ALTITUDE)
        s: str = self.receive(receive_data=True)
        return float(s)

    def depth(self) -> float:
        self.send(ArduinoAction.DEPTH)
        s: str = self.receive(receive_data=True)
        return float(s)

    def temperature(self) -> float:
        self.send(ArduinoAction.TEMPERATURE)
        s: str = self.receive(receive_data=True)
        return float(s)

    def pressure(self) -> float:
        self.send(ArduinoAction.PRESSURE)
        s: str = self.receive(receive_data=True)
        return float(s)


if __name__ == '__main__':
    arduino: ArduinoController = ArduinoController()
    time.sleep(arduino.time_out)
    arduino.send_arduino_command(ArduinoAction.KILL)
