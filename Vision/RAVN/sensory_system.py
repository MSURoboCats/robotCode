# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

import csv
from enum import Enum

import csv
import central_nervous_system as cns
#import motor_system as ms

INPUT_FILE = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFrame0.csv"
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720
FRAME_AREA = FRAME_PIXELS_X * FRAME_PIXELS_Y

def get_objects():
    objects_list = []
    with open(INPUT_FILE, 'r') as frame:
        frame_reader = csv.reader(frame)
        for row in frame_reader:
            objects_list.append(cns.VisualObject(row[0], row[1], row[2], row[3], row[4]))
    return objects_list