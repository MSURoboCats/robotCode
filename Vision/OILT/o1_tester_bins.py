# import packages
import csv
import os
import math
from statistics import mean

det = []
img = []
with open("result_bins.txt") as f: # import the one txt file that contains all the predicted bounding box information, etc.
    c = csv.reader(f, delimiter=' ', skipinitialspace=True)
    for line in c:
        if line != []:
            if line[-1] == 'milli-seconds.': # check if we have seen a new image
                det.append(['new_image']) # mark we are looking at a new image
                img.append(line)
            if line[0] == 'Bins:':
                line[1] = line[1].split('\t')[0]
                line[8] = line[8].split(')')[0]
                line[2] = float(line[2])/float(640) # reformat the coordinates, widths, heights into ratio of the image
                line[4] = float(line[4])/float(480) # reformat the coordinates, widths, heights into ratio of the image
                line[6] = float(line[6])/float(640) # reformat the coordinates, widths, heights into ratio of the image
                line[8] = float(line[8])/float(480) # reformat the coordinates, widths, heights into ratio of the image
                det.append(line)
# up till here, we have line[2] as top left corner's x coordinate,
# line[4] as the top left corner's y coordinate,
# line[6] as the width,
# line[8] as the height,
# all in ratio numbers

for line in det: # for each object detected
    if line[0] == 'Bins:':
        line[2] = line[2]+line[6]/2 # reformat the information into the same as the ground truth information
        line[4] = line[4]+line[8]/2
        line.remove(line[0])
        line.remove(line[0])
        line.remove(line[1])
        line.remove(line[2])
        line.remove(line[3])


gro = []
for file in os.listdir("C:/Users/xingz/OneDrive/Desktop/test_bin"): # read in each txt file containing bounding box information for one image
    if file.endswith(".txt"):
        gro.append(['new_image']) # mark when we see a new image
        with open(os.path.join("C:\\Users\\xingz\\OneDrive\\Desktop\\test_bin",file)) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            for line in c:
                gro.append(line[1:]) # attach the new object information
# now we have both the ground truth and the detections, in the same format

gro_pro = []
while ['new_image'] in gro: # reformat the information, the each sublist is an image, each subsublist is an object in the image
    gro.remove(gro[gro.index(['new_image'])])
    if ['new_image'] in gro:
        gro_pro.append(gro[0:gro.index(['new_image'])])
        gro = gro[gro.index(['new_image']):]
    else:
        gro_pro.append(gro[0:])

det_pro = []
while ['new_image'] in det: # reformat the information, the each sublist is an image, each subsublist is an object in the image
    det.remove(det[det.index(['new_image'])])
    if ['new_image'] in det:
        det_pro.append(det[0:det.index(['new_image'])])
        det = det[det.index(['new_image']):]
    else:
        det_pro.append(gro[0:])
# now we have detection and ground truth all in kind of a "cell array",
# det_pro[i] indicates detection results in i th image
# gro_pro[i] indicates ground truth in i th image
# det_pro[i][j] indicates the j th bounding box in i th image
# gro_pro[i][j] indicates the j th bounding box in i th image

xcoor_e = []
ycoor_e = []
width_e = []
height_e = []
temp_xe = []
temp_ye = []
temp_he = []
temp_we = []
for i in range(0,199): # loop through each image
    det_c = det_pro[i] # get each image's detected information
    gro_c = gro_pro[i] # get each image's ground truth information
    det_size = len(det_c) # number of objects in the prediction image
    for j in range(0,len(gro_c)): # loop through each object in the image
        gro_cc = gro_c[j]
#            e1 = math.sqrt((det_cc[0]-float(gro_cc[0]))**2+(det_cc[1]-float(gro_cc[1]))**2)/math.sqrt(1)
        for k in range(0,det_size): # for each objects in the prediction image
            temp_xe.append(abs(float(gro_cc[0])-det_c[k][0])) # calculate x coordinate error
            temp_ye.append(abs(float(gro_cc[1])-det_c[k][1])) # calculate y coordinate error
            temp_we.append(abs(float(gro_cc[2])-det_c[k][2])) # calculate width error
            temp_he.append(abs(float(gro_cc[3])-det_c[k][3])) # calculate height error
        e1 = abs(min(temp_xe))
        e4 = abs(max(temp_ye))
        e2 = abs(mean(temp_we))
        e3 = abs(mean(temp_he))
#        e2 = abs((det_cc[2]-float(gro_cc[2]))/1)
#        e3 = abs((det_cc[3]-float(gro_cc[3]))/1)
        xcoor_e.append([e1, i])
#        xcoor_e.append(e1)
        ycoor_e.append([e4, i])
        width_e.append([e2, i])
        height_e.append([e3, i])
        temp_xe = []
        temp_ye = []

#
with open('bin_xcoor.txt', 'w') as f: # save error result
    for item in xcoor_e:
        f.write("%s\n" % item)

with open('bin_ycoor.txt', 'w') as f: # save error result
    for item in ycoor_e:
        f.write("%s\n" % item)

with open('bin_width.txt', 'w') as f: # save error result
    for item in width_e:
        f.write("%s\n" % item)

with open('bin_height.txt', 'w') as f: # save error result
    for item in height_e:
        f.write("%s\n" % item)

with open('bin_obj.txt', 'w') as f: # save error result
    for item in img:
        f.write("%s\n" % item)

#        
e_cx_mean = mean(xcoor_e)*100 # calculate mean error
e_cy_mean = mean(ycoor_e)*100 # calculate mean error
e_w_mean = mean(width_e)*100 # calculate mean error
e_h_mean = mean(height_e)*100 # calculate mean error

e_cx_max = max(xcoor_e)*100 # calculate max error
e_cy_max = max(ycoor_e)*100 # calculate max error
e_w_max = max(width_e)*100 # calculate max error
e_h_max = max(height_e)*100 # calculate max error

e_cx_min = min(xcoor_e)*100 # calculate min error
e_cy_min = min(ycoor_e)*100 # calculate min error
e_w_min = min(width_e)*100 # calculate min error
e_h_min = min(height_e)*100 # calculate min error

print('The errors for bin detection:')

print('The average x coordinate error is:', e_cx_mean,'%') # display the errors
print('The average y coordinate error is:', e_cy_mean,'%')
print('The average width error is:', e_w_mean,'%')
print('The average height error is:', e_h_mean,'%')

print('The max x coordinate error is:', e_cx_max,'%')
print('The max y coordinate error is:', e_cy_max,'%')
print('The max width error is:', e_w_max,'%')
print('The max height error is:', e_h_max,'%')

print('The min x coordinate error is:', e_cx_min,'%')
print('The min y coordinate error is:', e_cy_min,'%')
print('The min width error is:', e_w_min,'%')
print('The min height error is:', e_h_min,'%')

with open('bin_xcoor.txt', 'w') as f:
    for item in xcoor_e:
        f.write("%s\n" % item)

with open('bin_ycoor.txt', 'w') as f:
    for item in ycoor_e:
        f.write("%s\n" % item)

with open('bin_width.txt', 'w') as f:
    for item in width_e:
        f.write("%s\n" % item)

with open('bin_height.txt', 'w') as f:
    for item in height_e:
        f.write("%s\n" % item)

with open('bin_obj.txt', 'w') as f:
    for item in img:
        f.write("%s\n" % item)
