# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

# For now, all copied from ControlsSub3.py
import math
import numpy as np
import re
import serial
import sys
import time

import central_nervous_system as cns
import sensory_system as ss

ARDUINO_BAUD = 9600
ARDUINO_PORT = '/dev/ttyACM1'
ARDUINO = serial.Serial(ARDUINO_PORT, ARDUINO_BAUD, timeout=5)

NUC_BAUD = 115200
NUC_PORT = '/dev/ttyUSB0'
NUC = serial.Serial(NUC_PORT, NUC_BAUD)

#Initializes all the different manuver variables and defines a function to be used with them -ZW
pitch = 0
roll = 0
yaw = 0
pitchold = 0
rollold = 0
yawold = 0
depthold = 0
global depth
depth = 0

def quaternion_to_euler(data):
    yz2 = 1 - (2 * (data[1]**2 + data[2]**2))
    pitch_p = 2 * (data[0] * data[2] - data[3] * data[1])
    roll_p = (2 * (data[0] * data[1] + data[2] * data[3])) / yz2
    yaw_p = (2 * (data[0] * data[3] + data[1] * data[2]))
    
    pitch_p = 1 if pitch_p > 1 else pitch_p
    pitch_p = -1 if pitch_p < -1 else pitch_p

    roll = math.atan(roll_p)
    pitch = math.asin(pitch_p)  
    yaw = math.atan2(yaw_p,yz2) + math.pi 

    #print("Roll: %s" % roll)
    #print("Pitch: %s" % pitch)
    #print("Yaw: %s" % yaw)

    return [roll, pitch, yaw]



def get_imu_data(command):
    global ser

    ser.write(command)
    data = ser.readline()
    values = np.array(re.findall('([-\d.]+)', data)).astype(np.float)
    return values

yaw = 0

#This function gets the data from the sensors to calibrate the roll, pitch, and a yaw to keep the sub oriented -ZW

def updateSensors():
    mag = [] # w, x, y, z
    magnetometer = get_imu_data("$PSPA,QUAT\r\n")
    mag = [magnetometer[i] for i in range(4)]
    global pitch,roll,yaw,yawold,pitchold,rollold
    rollold = roll
    pitchold = pitch
    yawold = yaw
    roll, pitch, yaw = quaternion_to_euler(mag)
    return roll,pitch,yaw


    



yaw0 = updateSensors()[2]
yawin = yaw0 + (math.pi * (input("Enter your Yaw (Degrees): ")/180))



DELTA = input("Enter your DELTA: ")
DELTA = .8
depthin = input("Enter your Depth: ")
deptherrorold = depthin - depthold
deptherror = depthin - depth





#Looks to be a test to see what depth the sub is at -ZW


def depthFunc():
    result = (.25286*((deptherror - deptherrorold)/DELTA) + 1.178*deptherror)
    if(result > 1):
        result = 1
    elif(result < -1):
        result = -1
    else:
        result = result
    return result

print(depthFunc())

#Below are functions which allow pitch, roll yaw for navigation -ZW

def pitchFunc():
    pitcherrorold = 0 - pitchold
    pitcherror = 0 - pitch
    result = (.3309*pitcherror + .15406*((pitcherror - pitcherrorold)/DELTA))
    if(result > 1):
        result = 1
    elif(result < -1):
        result = -1
    else:
        result = result
    return result

print(pitchFunc())

rollerrorold = 0 - rollold
pitcherror = 0 - roll

def rollFunc():
    rollerrorold = 0 - rollold
    rollerror = 0 - roll
    result = (.3309*rollerror + .15406*((rollerror - rollerrorold)/DELTA))
    if(result > 1):
        result = 1
    elif(result < -1):
        result = -1
    else:
        result = result
    return result

print(rollFunc())



def yawFunc():
    global yaw
    if(yawin<=(math.pi/4)):
        if(yaw>=(5*math.pi/4)):
            yaw = yaw - 2*math.pi
        else:
            yaw = yaw
    if(yawin>=(3*math.pi/2)):
        if(yaw<=(3*math.pi/4)):
            yaw = yaw + 2*math.pi
        else:
            yaw = yaw

    print(yawin)
    print(yaw)
        
    yawerrorold = yawin - yawold
    yawerror = yawin - yaw
    result = (.25684*((yawerror - yawerrorold)/DELTA) + .58395*yawerror)
    if(result > 1):
        result = 1
    elif(result < -1):
        result = -1
    else:
        result = result
    return result

print(yawFunc())

#Here's the throttle control that uses what looks like 7 or 8 different speed settings, this might be useful to take a look at -ZW

#Rudimentary Throttle Control

def ThrottleOut():
    T6 = depthFunc() + rollFunc() + pitchFunc()
    T5 = -(depthFunc() + rollFunc() - pitchFunc())
    T8 = -(depthFunc() - rollFunc() + pitchFunc())
    T7 = depthFunc() - rollFunc() - pitchFunc()
    T4 = 1500 #-1*yawFunc()
    T3 = 1500 #yawFunc()
    T1 = 1500
    T2 = 1500
    if (T7 > 1):
        T7 = 1900
    elif(T7 < -1):
        T7 = 1100
    else:
        T7 = int(400*T7 + 1500)

    if (T8 > 1):
        T8 = 1900
    elif(T8 < -1):
        T8 = 1100
    else:
        T8 = int(400*T8 + 1500)

    if (T3 > 1):
        T3 = 1900
    elif(T3 < -1):
        T3 = 1100
    else:
        T3 = int(400*T3 + 1500)        

    if (T4 > 1):
        T4 = 1900
    elif(T4 < -1):
        T4 = 1100
    else:
        T4 = int(400*T4 + 1500)

    if (T5 > 1):
        T5 = 1900
    elif(T5 < -1):
        T5 = 1100
    else:
        T5 = int(400*T5 + 1500)
    
    if (T6 > 1):
        T6 = 1900
    elif(T6 < -1):
        T6 = 1100
    else:
        T6 = int(400*T6 + 1500)

    #print ("Values sent: ")
    #print(T1,T2,T3,T4,T5,T6,T7,T8)
    ard.write(str.encode(str(T1))+" "+str.encode(str(T2))+" "+str.encode(str(T3))+" "+str.encode(str(T4))+" "+str.encode(str(T5))+" "+str.encode(str(T6))+" "+str.encode(str(T7))+" "+str.encode(str(T8))+" ")
    time.sleep(.1)

    return T1,T2,T3,T4,T5,T6,T7,T8
