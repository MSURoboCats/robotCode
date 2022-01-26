"""
Collecting and returning data from the IMU
- Inertial Measurement Unit
"""
# This is the simplified IMU code. The main function shows how to send data requests. Built for the TyphoonII Spartion GEDC-8 IMU -JG
# Butter is the scipy package that allows most of the calculations to be done -ZW
import numpy as np
import re
import serial
import time

# port = '/dev/ttyUSB0' #Intel Nuc
port = 'COM5'  # Josh PC

baud = 115200
fs = 100.0  # Sample rate, Hz
T = 1 / fs
cutoff = fs / 2  # Desired cutoff frequency of the filter, Hz,
# Sightly higher than actual 1.2 Hznyq = 0.5 * fs
# Nyquist Frequencyorder = 2
# Sin wave can be approx represented as quadratic ##JG-?
nyq = 0.5 * fs
n = int(T * fs)  # Total number of samples

ser = serial.Serial(port, baud)
ser.flush()  # Flushes the store data from serial
print("Ready!")


def get_imu_data(command):
    global ser

    ser.write(command.encode())
    data = ser.readline().decode('utf-8')
    values = np.array(re.findall('([-\d.]+)', data)).astype(float)
    return values


def get_dist_north():
    print("Getting the heading away from north!")
    # Call the get data func at data point $PSPA,QUAT\r\n
    # See manual for locations of data
    # This will return a float from -1 to 1
    magnetometer = get_imu_data("$PSPA,QUAT\r\n")
    # Make it the true hedding by multiplying by 180
    hedding = ((magnetometer[0]) * 180)
    print(magnetometer[0])
    # Returns deg off of north
    return hedding


def get_hedding():
    print("Getting the true heading!")
    # Call the get data func at data point $PSPA,QUAT\r\n
    # See manual for locations of data
    # This will return a float from -1 to 1
    magnetometer = get_imu_data("$PSPA,QUAT\r\n")
    # Make it the true hedding by multiplying by 180
    hedding = ((magnetometer[0] + 1) * 180)
    print(magnetometer[0])
    # Returns deg off of north
    return hedding


def get_pitch():
    print("Getting the pitch!")
    # Call the get data func at data point $PSP
    # See manual for locations of data
    # This will return a pitch, roll,
    pitch = get_imu_data("$PSPA,PR\n")
    print(pitch[1])
    # Returns deg off of level
    return pitch


def get_roll():
    # TODO: Not currently implemented
    t = 0
    return t


def get_yaw():
    # TODO
    return


if __name__ == "__main__":
    # This code calls for the pitch according to the TyphoonII IMU for testing sensor
    print("Main run!")
    print(get_pitch())
    time.sleep(5)
    print(get_pitch())
    time.sleep(5)
    print(get_pitch())
    time.sleep(5)
    print("Done!")
