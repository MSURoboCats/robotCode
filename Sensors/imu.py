import serial
import numpy as np
import re
import time

from static_utilities import StaticUtilities


class ImuAhrsSparton:

    def __init__(self, *, port: str = "COM5", baud_rate: int = 115200, name: str = "AHRS Sparton IMU"):
        self.name: str = name
        self.port: str = port  # COM5 on Josh PC
        self.baud_rate: int = baud_rate
        self.fs_sample_rate: float = 100.0  # in Hz
        self.T_period: float = 1 / self.fs_sample_rate
        self.cutoff_frequency: float = self.fs_sample_rate / 2  # Desired cutoff frequency of the filter, Hz, Sightly higher than actual 1.2 Hznyq = 0.5 * fs
        self.nyq_nyquist_frequency: float = 0.5 * self.fs_sample_rate  # Nyquist Frequencyorder = 2, Sin wave can be approx represented as quadratic ##JG-?
        self.n_number_of_samples: int = int(self.T_period * self.fs_sample_rate)  # Total number of samples
        try:
            self.ser = serial.Serial(self.port, self.baud_rate)
            self.ser.flush()
        except serial.serialutil.SerialException:
            StaticUtilities.logger.error(f"Failed to initialize {self.name} on {self.port} at {self.baud_rate}")
        else:
            StaticUtilities.logger.info(f"{self.name} initialized on {self.port} at {self.baud_rate}")

    def get_imu_data(self, command):
        self.ser.write(command.encode())
        data = self.ser.readline().decode('utf-8')
        values = np.array(re.findall('([-\d.]+)', data)).astype(float)
        return values

    def get_dist_north(self):
        StaticUtilities.logger.info("Getting the heading away from north")
        # Call the get data func at data point $PSPA,QUAT\r\n
        # See manual for locations of data
        # This will return a float from -1 to 1
        magnetometer = self.get_imu_data("$PSPA,QUAT\r\n")
        # Make it the true hedding by multiplying by 180
        heading = ((magnetometer[0]) * 180)
        StaticUtilities.logger.info(f"{magnetometer[0]}")
        # Returns deg off of north
        return heading

    def heading(self):
        StaticUtilities.logger.info("Getting the true heading!")
        # Call the get data func at data point $PSPA,QUAT\r\n
        # See manual for locations of data
        # This will return a float from -1 to 1
        magnetometer = self.get_imu_data("$PSPA,QUAT\r\n")
        # Make it the true heading by multiplying by 180
        heading = ((magnetometer[0] + 1) * 180)
        StaticUtilities.logger.info(f"{magnetometer[0]}")
        # Returns deg off of north
        return heading

    def pitch(self):
        StaticUtilities.logger.info("Getting the pitch!")
        # Call the get data func at data point $PSP
        # See manual for locations of data
        # This will return a pitch, roll,
        pitch = self.get_imu_data("$PSPA,PR\n")
        StaticUtilities.logger.info(f"{pitch[1]}")
        # Returns deg off of level
        return pitch

    def roll(self):
        # TODO: Not currently implemented
        StaticUtilities.logger.warning("Getting the roll: Not Implemented")
        t = 0
        return t

    def yaw(self):
        # TODO
        return

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
    imu: ImuAhrsSparton = ImuAhrsSparton()
    imu.test_pitch()

