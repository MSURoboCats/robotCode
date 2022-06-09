import csv
import os
import math
from pytictoc import TicToc

t = TicToc()
t.tic()

det = []
with open("result_bins.txt") as f:
    c = csv.reader(f, delimiter=' ', skipinitialspace=True)
    for line in c:
        if line != []:
            if line[0] == 'Bins:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])
            elif line[0] == 'Green_Buoy:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])
            elif line[0] == 'Gate:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])
            elif line[0] == 'Red_Buoy:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])
            elif line[0] == 'Blue_Buoy:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])
            if line[0] == 'Torpedo:':
                det.append([round(float(line[2])+float(line[6])/2), round(float(line[4])-float(line[8].split(')')[0])/2), int(line[6]), int(line[8].split(')')[0]), line[0].split(':')[0]])

with open('converted_r.txt', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(det)

t.toc()
