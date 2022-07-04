import platform
from threading import Thread
from typing import List
import multiprocessing
from multiprocessing import Process, Queue

from Actuators.arduino_serial_interface import ArduinoSerialInterfaceController, ArduinoAction
from Sensors.imu import ImuAhrsSpartan
from Sensors.vision import Vision
from Sensors.hydrophone import Hydrophone
from static_utilities import StaticUtilities


class RobotController:

    def __init__(self, number_of_processes: int = (multiprocessing.cpu_count() - 1)) -> None:
        StaticUtilities.logger.info(f"{RobotController.__name__} initializing components")

        self.imu: ImuAhrsSpartan = ImuAhrsSpartan(port=("COM5" if platform.system() == "Windows" else ("/dev/ttyACM1" if platform.system() == "Linux" else "")), baud_rate=115200)

        self.arduino: ArduinoSerialInterfaceController = ArduinoSerialInterfaceController(
            arduino_port="COM7" if platform.system() == "Windows" else ("/dev/ttyACM0" if platform.system() == "Linux" else ""),
            name="Arduino Serial Interface Controller")

        self.vision: Vision = Vision()

        self._process_pool: List[
            Process] = []  # use this to assign things that need to get updated constantly. Ie: IMU, Vision and other sensor data
        self._thread_pool: List[Thread] = []
        self._process_queue: Queue = Queue()
        self._process_lock: multiprocessing.Lock = multiprocessing.Lock()
        self._available_processes: int = multiprocessing.cpu_count()
        self._available_threads: int = number_of_processes*2

        self._process_pool.append(multiprocessing.Process(target=self.imu.update_position, args=(), name="IMU Position Update Process"))

        StaticUtilities.logger.info(f"{RobotController.__name__} initialized")

    def autonomous(self) -> None:

        for process in self._process_pool:
            process.start()
        for process in self._process_pool:
            process.join()
        # self.arduino_thruster_controller.send_imu_control("test_data")
        # StaticUtilities.logger.info(f"{self.arduino_thruster_controller.receive()}")
        # self.arduino_depth_pressure_controller.send(ArduinoAction.ALL_PRESSURE_DEPTH_MEASURES)
        # StaticUtilities.logger.info(f"{self.arduino_depth_pressure_controller.receive()}")

    def test(self) -> None:
        pass

    def control_with_heading(self):
        # Make this run on a process alongside main?
        self.arduino.send_imu_control("")
