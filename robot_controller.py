from typing import List
import multiprocessing
from multiprocessing import Process, Queue

from Actuators.arduino_controller import ArduinoController
from Sensors.imu import ImuAhrsSparton
from Sensors.vision import Vision
from Sensors.hydrophone import Hydrophone
from gui import GUI
from static_utilities import StaticUtilities


class RobotController:

    def __init__(self, no_gui: bool = False) -> None:
        self.imu: ImuAhrsSparton = ImuAhrsSparton(port="COM5", baud_rate=115200)
        self.arduino: ArduinoController = ArduinoController(arduino_port="/dev/ttyACM0")
        self.vision: Vision = Vision()
        self.gui: GUI = GUI() if no_gui is False else None
        self.number_hydrophones: int = 3
        self.hydrophones: List[Hydrophone] = []
        for i in range(self.number_hydrophones):
            self.hydrophones.append(Hydrophone(name=f"Hydrophone {i}"))
        self._process_pool: List[Process] = []
        self._process_queue: Queue = Queue()
        self._process_lock: multiprocessing.Lock = multiprocessing.Lock()
        self._available_threads: int = multiprocessing.cpu_count()
        StaticUtilities.logger.info(f"{RobotController.__name__} initialized")

    def autonomous(self) -> None:
        pass

    def test(self) -> None:
        pass
