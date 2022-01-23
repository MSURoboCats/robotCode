from typing import List
import multiprocessing
from multiprocessing import Process, Queue

from Actuators.arduino_controller import ArduinoController
from Sensors.depth_pressure import DepthPressure
from Sensors.imu import ImuAhrsSparton
from Sensors.vision import Vision
from Sensors.hydrophone import Hydrophone
from gui import GUI
from static_utilities import StaticUtilities


class RobotController:

    def __init__(self, no_gui: bool = False, number_of_processes: int = (multiprocessing.cpu_count() - 1)) -> None:
        self.imu: ImuAhrsSparton = ImuAhrsSparton(port="COM5", baud_rate=115200)
        self.arduino: ArduinoController = ArduinoController(arduino_port="/dev/ttyACM0")
        self.vision: Vision = Vision()
        self.gui: GUI = GUI() if no_gui is False else None
        self.depth_pressure: DepthPressure = DepthPressure()
        self.number_hydrophones: int = 3
        self.hydrophones: List[Hydrophone] = []
        for i in range(self.number_hydrophones):
            self.hydrophones.append(Hydrophone(name=f"Hydrophone {i}"))

        self._process_pool: List[Process] = []  # use this to assign things that need to get updated constantly. Ie: IMU, Vision and other sensor data

        self._process_queue: Queue = Queue()
        self._process_lock: multiprocessing.Lock = multiprocessing.Lock()
        self._available_threads: int = number_of_processes

        StaticUtilities.logger.info(f"{RobotController.__name__} initialized")

    def autonomous(self) -> None:
        pass

    def test(self) -> None:
        pass

    def control_with_heading(self):
        # Make this run on a process alongside main?
        self.arduino.send_imu_control([])
