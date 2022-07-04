import threading
from typing import Tuple, List

import serial
import numpy as np
import re
import time

from IMUPositionTrackingMaster.tracker_main import IMUTracker

from static_utilities import StaticUtilities


class ImuAhrsSpartan:

    def __init__(self, *, port: str = "COM5", baud_rate: int = 115200, name: str = "AHRS Sparton IMU"):
        self.name: str = name
        self.port: str = port  # COM5 on Josh PC
        self.baud_rate: int = baud_rate
        self.fs_sample_rate: float = 100.0  # in Hz
        self.T_period: float = 1 / self.fs_sample_rate
        self.cutoff_frequency: float = self.fs_sample_rate / 2  # Desired cutoff frequency of the filter, Hz, Sightly higher than actual 1.2 Hznyq = 0.5 * fs
        self.nyq_nyquist_frequency: float = 0.5 * self.fs_sample_rate  # Nyquist frequency order = 2, Sin wave can be approx represented as quadratic ##JG-?
        self.n_number_of_samples: int = int(self.T_period * self.fs_sample_rate)  # Total number of samples
        self.position = None
        self.data: List[List[float]] = []
        self.serial_object = None
        self.serial_connection_established: bool = False
        self.initialize_serial_connection(self.port)
        if not self.serial_connection_established:
            available_serial_devices = StaticUtilities.serial_devices()
            for device in available_serial_devices:
                if "ahrs" not in device[1].lower():
                    StaticUtilities.logger.debug(f"No IMU on {device[0]}")
                    continue
                StaticUtilities.logger.info(f"Found {device[1]} on {device[0]}. Attempting connection.")
                self.initialize_serial_connection(device[0])
                if self.serial_connection_established:
                    break

        self.running: bool = True
        self.lock = threading.Lock()

    def initialize_serial_connection(self, port: str) -> None:
        try:
            self.serial_object = serial.Serial(port, self.baud_rate)
            self.serial_object.flush()
        except serial.serialutil.SerialException:
            StaticUtilities.logger.error(f"Failed to initialize {self.name} on {port} at {self.baud_rate}")
            self.serial_connection_established = False
        else:
            StaticUtilities.logger.info(f"{self.name} initialized on {port} at {self.baud_rate}")
            self.serial_connection_established = True

    def update_position(self):
        tracker = IMUTracker(sampling=100)
        for i in range(0, 30):
            time.sleep(0.1)
            gyro = self.angular_velocity_vector()
            accel = self.acceleration_vector()
            mag = self.magnetic_vector()
            self.data.append([gyro[0], gyro[1], gyro[2], accel[0], accel[1], accel[2], mag[0], mag[1], mag[2]])
        init_list = tracker.initialize(self.data[5:30])
        while self.running:
            time.sleep(0.1)
            gyro = self.angular_velocity_vector()
            accel = self.acceleration_vector()
            mag = self.magnetic_vector()
            self.data.append([gyro[0], gyro[1], gyro[2], accel[0], accel[1], accel[2], mag[0], mag[1], mag[2]])
            # EKF step
            a_nav, orix, oriy, oriz = tracker.attitudeTrack(self.data[30:], init_list)

            # Acceleration correction step
            a_nav_filtered = tracker.removeAccErr(a_nav, filter=False)
            # plot3([a_nav, a_nav_filtered])

            # ZUPT step
            v = tracker.zupt(a_nav_filtered, threshold=0.2)
            # plot3([v])

            # Integration Step
            self.lock.acquire(timeout=.5)
            self.position = tracker.positionTrack(a_nav_filtered, v)
            self.lock.release()

        # update gyro
        # update accel
        # update mag
        # update data list
        # computations
        # update stored position


    def imu_data(self, command):
        self.serial_object.write(command.encode())
        data = self.serial_object.readline().decode('utf-8')
        values = np.array(re.findall('([-\d.]+)', data)).astype(float)
        return values

    def get_dist_north(self):
        StaticUtilities.logger.info("Getting the heading away from north")
        # Call the get data func at data point $PSPA,QUAT\r\n
        # See manual for locations of data
        # This will return a float from -1 to 1
        magnetometer = self.imu_data("$PSPA,QUAT\r\n")
        # Make it the true hedding by multiplying by 180
        heading = ((magnetometer[0]) * 180)
        StaticUtilities.logger.info(f"{magnetometer[0]}")
        # Returns deg off of north
        return heading

    def pitch(self):
        StaticUtilities.logger.info("Getting the pitch!")
        # Call the get data func at data point $PSPA,PR
        # This will return a pitch from -90 to 90
        pitch = self.imu_data("$PSPA,PR\n")[0]
        StaticUtilities.logger.info(f"{pitch}")
        # Returns deg off of level
        return pitch

    def roll(self):
        StaticUtilities.logger.info("Getting the roll!")
        # Call the get data func at data point $PSPA,PR
        # See manual for locations of data
        # This will return a roll from -180 to 180
        roll = self.imu_data("$PSPA,PR\n")[1]
        StaticUtilities.logger.info(f"{roll}")
        # Returns deg of roll
        return roll

    def yaw(self):
        StaticUtilities.logger.info("Getting the yaw!")
        # Call the get data func at data point $PSPA,QUAT
        # This will return a float from -1 to 1
        magnetometer = self.imu_data("$PSPA,QUAT\r\n")
        # Make it the true heading by multiplying by 180
        yaw = ((magnetometer[0] + 1) * 180)[0]
        StaticUtilities.logger.info(f"{magnetometer}")
        # Returns a heading from 0-360 aka a "yaw"
        return yaw

    def temperature(self):
        # NOT TESTED YET
        StaticUtilities.logger.info("Getting the temperature in celsius!")
        # Call the get data func at data point $PSPA,TEMP
        # This will return the temperature in celsius from the IMU
        temperature = self.imu_data("$PSPA,TEMP\r\n")
        StaticUtilities.logger.info(f"{temperature}")
        # Returns the temperature in celsius
        return temperature

    def angular_velocity_vector(self):
        return self.imu_data("$PSPA,G")

    def acceleration_vector(self):
        # NOT TESTED YET
        # We might want three different functions for x, y, and z. Just let me know! -JG
        StaticUtilities.logger.info("Getting acceleration data!")
        # Call the get data func at point $PSPA,A
        # This will return the accelerometer data without quaternions
        # Data will be in the form of [X,Y,Z]
        accelerometers = self.imu_data("$PSPA,A")
        StaticUtilities.logger.info(f"{accelerometers}")
        # Returns all the gyro data for all three directions
        return accelerometers

    def magnetic_vector(self):
        return self.imu_data("$PSPA,M")

    def calibrate_gyro(self):
        # NOT TESTED YET## Really need to test this/ do more research on this. -JG
        StaticUtilities.logger.info("Please wait while I calibrate!")
        self.imu_data("$PSPA,GYROCAL")
        StaticUtilities.logger.info("All done! Thank you!")

    def test_pitch(self) -> None:
        """
        Gets the pitch according to the TyphoonII IMU for testing sensor
        """
        StaticUtilities.logger.info(f"Running test_pitch\n{self.pitch()}")
        time.sleep(5)
        StaticUtilities.logger.info(f"{self.pitch()}")
        time.sleep(5)
        StaticUtilities.logger.info(f"{self.pitch()}")
        time.sleep(5)
        StaticUtilities.logger.info(f"{self.pitch()}\ntest_pitch Done")


if __name__ == "__main__":
    imu: ImuAhrsSpartan = ImuAhrsSpartan()
    imu.test_pitch()
