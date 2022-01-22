from enum import Enum

import serial
import time

from static_utilities import StaticUtilities


class ArduinoAction(Enum):
    """
    Enumerated representation of all of the possible actions for the Arduino.
    Allows conversion of useful names to string that the Arduino understands and can be sent to the Arduino over serial.
    For example: the value of ArduinoActions.DIVE is the str "dive".
    Sending this to the Arduino over serial with the method ArduinoController.send_arduino_command()
    """
    START = "start"
    FORWARD = "forward\n"
    REVERSE = "reverse"
    NEUTRAL = "neutral"
    DIVE = "dive"
    HOVER_FORWARD = "hoverForward"
    HOVER_REVERSE = "hoverSpin"
    KILL = "kill"
    TEST_ALL_THRUSTERS = "all"
    SEQUENTIALLY_TEST_ALL_THRUSTERS = "seqTest"


class ArduinoController:
    """
    Class that can be instantiated to control an Arduino and send it commands over serial.
    """

    def __init__(self, *, arduino_port: str = '/dev/ttyACM0', baud_rate: int = 115200, time_out: int = 1):
        """
        Initializes the Arduino and connection.
        Starts the Arduino.
        arduino_port, baud_rate, time_out default values can be overridden by passing values into the constructor on instantiation.
        """
        self.arduino_port: str = arduino_port
        self.baud_rate: int = baud_rate
        self.time_out: int = time_out
        self.arduino = serial.Serial(self.arduino_port, self.baud_rate, timeout=self.time_out)
        time.sleep(self.time_out)
        self.arduino.flush()
        self.send(ArduinoAction.START)
        self.receive(receipt="arduino ready")
        self.arduino.flush()

    def receive(self, *, receipt: str = "status: done") -> str:
        """
        Waits to receive a response from the Arduino via serial that matches the str receipt.
        If the str Keyword Arg receipt is not modified it defaults to the value "status: done".
        If the Arduino returns the str "killed" this method will return.

        Note: I'm realizing it may be beneficial to implement multiprocessing in the RobotController Class.
        If that happens all methods in this class should impose a lock until an ack is received.

        :param receipt: str to wait to receive from the Arduino via serial. Represents a TCP ACK.
        :return: str representation of the value received from the Arduino over serial.
        """
        s: str = ""
        while s != receipt:
            s = self.arduino.readline().decode('utf-8').rstrip()
            if s != "":
                StaticUtilities.logger.info(f"{s}")
            if s == "status: killed":
                return "killed"
            time.sleep(self.time_out * 0.01)
        return s

    def send(self, command: ArduinoAction) -> None:
        """
        Sends the string command to the Arduino over serial.
        :param command: str representation of a command to send to the Arduino.
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
        StaticUtilities.logger.info(f"Arduino on {self.arduino_port} killed. Restart Arduino to continue.")

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
        :return bool representation of the success of sending the command to the Arduino. If the Arduino was killed at any point return False. Otherwise True.
        """
        self.send(arduino_action)
        return False if self.receive(receipt=arduino_receipt) == "killed" else True


if __name__ == '__main__':
    arduino: ArduinoController = ArduinoController()
    time.sleep(arduino.time_out)
    arduino.send_arduino_command(ArduinoAction.KILL)
