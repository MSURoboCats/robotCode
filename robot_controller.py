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

    def __init__(self) -> None:
        self.imu: ImuAhrsSparton = ImuAhrsSparton(port="COM5", baud_rate=115200)
        self.arduino: ArduinoController = ArduinoController(arduino_port="/dev/ttyACM0")
        self.vision: Vision = Vision()
        self.gui: GUI = GUI()
        self.hydrophones: List[Hydrophone] = []
        self._process_pool: List[Process] = []
        self._process_queue: Queue = Queue()
        self._process_lock: multiprocessing.Lock = multiprocessing.Lock()
        self._available_threads: int = multiprocessing.cpu_count()
        StaticUtilities.logger.info(f"RobotController Initialized")
