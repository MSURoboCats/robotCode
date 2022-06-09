import numpy as np
import random as rd
import os
import errno
MAX_OBJECTS = 6
CLASS_PRIORITY = [1, 3 , 4 ,5 ,2 ,6]
def list_A(tot_objects, num_file):
    #Note: To meet the specification set in Verification Plan the total number of objects must be greater than or equal to 4
    highest_priority_obj = 999
    highest_index = 999
    assert tot_objects >= 4, "Error: Total number of objects must be greater than or equal to 4"
    rows = rd.randint(4,tot_objects)
    current_view = np.empty([rows,5])
    classes = [*range(1,tot_objects+1)]
    for i in range(rows):
        current_view[i,0] = rd.randint(0,1280)
        current_view[i,1] = rd.randint(0,720)
        current_view[i,2] = rd.randint(0,1280)
        current_view[i,3] = rd.randint(0,720)
        obj_type = rd.choice(classes)
        for j in range(len(CLASS_PRIORITY)):
            if obj_type == CLASS_PRIORITY[j]:
                if j < highest_index:
                    highest_priority = CLASS_PRIORITY[j]
                    highest_index = j
        current_view[i,4] = obj_type
        classes.remove(obj_type)
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/ListA_ans.txt", "a") 
    L = str(highest_priority) + "\n"
    file1.writelines(L) 
    file1.close()

def list_B(num_file):
    centroid = np.array([rd.randint(0,1280), rd.randint(0,720)])
    if int(centroid[0]) >= 615 and int(centroid[0]) <= 665:
        directionX = "Centered, "
    elif int(centroid[0]) < 615:
        directionX = "Left, "
    else:
        directionX = "Right, "
    if int(centroid[1]) >= 335 and int(centroid[1]) <= 385:
        directionY = "Centered"
    elif int(centroid[1]) < 335:
        directionY = "Descend"
    else:
        directionY = "Ascend"
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/CurrentFile" + str(num_file) +".csv",centroid,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/ListB_ans.txt", "a") 
    L = directionX + directionY + "\n"
    file1.writelines(L) 
    file1.close()  

def list_C(tot_objects,num_file): 
    x = rd.randint(3,tot_objects)
    y = rd.randint(1,x)
    highest_priority_obj = 999
    highest_index = 999
    classes = [*range(1,tot_objects+1)]
    current_view = np.zeros([x,2])
    for i in range(x):
        obj_type = rd.choice(classes)
        current_view[i,0] = obj_type
        classes.remove(obj_type)
    classes = [*range(1,tot_objects+1)]
    for j in range(y):
        obj_type = rd.choice(classes)
        current_view[j,1] = obj_type
        classes.remove(obj_type)
    seen_list = current_view[0:y,1].tolist()
    in_view_list = current_view[:,0].tolist()
    relevant_obj = CLASS_PRIORITY.copy()
    relevant_obj = [float(x) for x in relevant_obj if x not in seen_list]
    # print(in_view_list)
    # print(relevant_obj)
    for a in range(len(in_view_list)):
        if (in_view_list[a] in relevant_obj) and (relevant_obj.index(in_view_list[a]) < highest_index):
            highest_priority_obj = in_view_list[a]
            highest_index = relevant_obj.index(in_view_list[a])
    if highest_priority_obj == 999:
        highest_priority_obj = "Search"
    # print(highest_priority_obj)
    # print(highest_index)
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/ListC_ans.txt", "a") 
    L = str(highest_priority_obj) + "\n"
    file1.writelines(L) 
    file1.close() 
    ### ASSUMING BOTTOM LEFT IS 0,0 ###
### OBJECT OVERLAP NOT ACCOUNTED FOR ###

#---------------------------------------------------------------
# Shift All Objects Random Directions
#---------------------------------------------------------------
def list_D(num_tests):

    max_objects = 5
    min_object_dimension = 20

    #---------------------------------------------------------------
    # Make "ListD" folder to place data into
    #---------------------------------------------------------------
    filename = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListD/"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    #---------------------------------------------------------------
    # Make 2 Sequential CSVs
    #---------------------------------------------------------------
    for j in range(num_tests):
        oneTypeOfEach = []
        rows = rd.randint(0,max_objects) # Number of objects in CSV
        f = open(filename + "CurrentFrame" + str(j) + ".csv", "w")
        g = open(filename + "NextFrame" + str(j) + ".csv", "w")
        for i in range(rows):
            loop = 1
            #---------------------------------------------------------------
            # Calculate Original Variables
            #---------------------------------------------------------------
            #---------- Original Centroids ----------
            xc = rd.randint(min_object_dimension/2,(1280 - min_object_dimension/2))
            yc = rd.randint(min_object_dimension/2,(720 - min_object_dimension/2))

            #---------- Get xd ----------
            if (1280 - xc) <= xc:
                xd = rd.randint(min_object_dimension,2*(1280 - xc))
            else:
                xd = rd.randint(min_object_dimension,2*xc)
                
            #---------- Get yd ----------    
            if (720 - yc) <= yc:
                yd = rd.randint(min_object_dimension,2*(720 - yc))
            else:
                yd = rd.randint(min_object_dimension,2*yc)

            #---------------------------------------------------------------
            # Calculate Shifted Variables
            #---------------------------------------------------------------
            #---------- Shifted Centroids ----------
            xcs = xc + rd.randint(-50,50)
            ycs = yc + rd.randint(-50,50)

            #---------- Get xds ----------
            if xcs + xd/2 > 1280:  # If object is not entirely in frame (Off the RIGHT side of frame)
                xds = int(xd - ((xcs + xd/2) - 1280))  # Update xd with lost dimension removed.
                xcs = int(1280 - xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif xcs - xd/2 < 0:  # If object is not entirely in frame (Off the LEFT side of frame)
                xds = int(xd - abs(xcs - xd/2))  # Update xd with lost dimension removed.
                xcs = int(xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                xds = xd

            #---------- Get yds ----------
            if ycs + yd/2 > 720:  # If object is not entirely in frame (Off the TOP of frame)
                yds = int(yd - ((ycs + yd/2) - 720))  # Update xyd with lost dimension removed.
                ycs = int(720 - yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif ycs - yd/2 < 0:  # If object is not entirely in frame (Off the BOTTOM of frame)
                yds = int(yd - abs(ycs - yd/2))  # Update yd with lost dimension removed.
                ycs = int(yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                yds = yd
                
            #---------------------------------------------------------------
            # Create 2 CSV
            #---------------------------------------------------------------
            while loop == 1:
                type = rd.randint(1,max_objects)
                if oneTypeOfEach.count(type) == 0: # Only one of each object type
                    f.write(str(xc) + "," + str(yc) + "," + str(xd) + "," + str(yd) + "," + str(type) + "\r")  # First CSV
                    g.write(str(xcs) + "," + str(ycs) + "," + str(xds) + "," + str(yds) + "," + str(type) + "\r")  # Shifted CSV
                    oneTypeOfEach.append(type)
                    loop = 0
        f.close()
        g.close()

#---------------------------------------------------------------
# Shift All Objects The Same Direction
#---------------------------------------------------------------
def list_E(num_tests):

    max_objects = 5
    min_object_dimension = 20
    xshift = rd.randint(-50,50)
    yshift = rd.randint(-50,50)

    #---------------------------------------------------------------
    # Make "ListE" folder to place data into
    #---------------------------------------------------------------
    filename = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListE/"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    #---------------------------------------------------------------
    # Make 2 Sequential CSVs
    #---------------------------------------------------------------
    for j in range(num_tests):
        oneTypeOfEach = []
        rows = rd.randint(0,max_objects) # Number of objects in CSV
        f = open(filename + "CurrentFrame" + str(j) + ".csv", "w")
        g = open(filename + "NextFrame" + str(j) + ".csv", "w")
        for i in range(rows):
            loop = 1
            #---------------------------------------------------------------
            # Calculate Original Variables
            #---------------------------------------------------------------
            #---------- Original Centroids ----------
            xc = rd.randint(min_object_dimension/2,(1280 - min_object_dimension/2))
            yc = rd.randint(min_object_dimension/2,(720 - min_object_dimension/2))

            #---------- Get xd ----------
            if (1280 - xc) <= xc:
                xd = rd.randint(min_object_dimension,2*(1280 - xc))
            else:
                xd = rd.randint(min_object_dimension,2*xc)
                
            #---------- Get yd ----------    
            if (720 - yc) <= yc:
                yd = rd.randint(min_object_dimension,2*(720 - yc))
            else:
                yd = rd.randint(min_object_dimension,2*yc)

            #---------------------------------------------------------------
            # Calculate Shifted Variables
            #---------------------------------------------------------------
            #---------- Shifted Centroids ----------
            xcs = xc + xshift  # Move centroids toward center by half the distance.
            ycs = yc + yshift
                
            #---------- Get xds ----------
            if xcs + xd/2 > 1280:  # If object is not entirely in frame (Off the RIGHT side of frame)
                xds = int(xd - ((xcs + xd/2) - 1280))  # Update xd with lost dimension removed.
                xcs = int(1280 - xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif xcs - xd/2 < 0:  # If object is not entirely in frame (Off the LEFT side of frame)
                xds = int(xd - abs(xcs - xd/2))  # Update xd with lost dimension removed.
                xcs = int(xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                xds = xd

            #---------- Get yds ----------
            if ycs + yd/2 > 720:  # If object is not entirely in frame (Off the TOP of frame)
                yds = int(yd - ((ycs + yd/2) - 720))  # Update xyd with lost dimension removed.
                ycs = int(720 - yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif ycs - yd/2 < 0:  # If object is not entirely in frame (Off the BOTTOM of frame)
                yds = int(yd - abs(ycs - yd/2))  # Update yd with lost dimension removed.
                ycs = int(yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                yds = yd
                
            #---------------------------------------------------------------
            # Create 2 CSV
            #---------------------------------------------------------------
            while loop == 1:
                type = rd.randint(1,max_objects)
                if oneTypeOfEach.count(type) == 0: # Only one of each object type
                    f.write(str(xc) + "," + str(yc) + "," + str(xd) + "," + str(yd) + "," + str(type) + "\r")  # First CSV
                    g.write(str(xcs) + "," + str(ycs) + "," + str(xds) + "," + str(yds) + "," + str(type) + "\r")  # Shifted CSV
                    oneTypeOfEach.append(type)
                    loop = 0
        f.close()
        g.close()

def list_F(tot_objects, num_file):
    #Note: To meet the specification set in Verification Plan the total number of objects must be greater than or equal to 4
    highest_priority_obj = 999
    highest_index = 999
    assert tot_objects >= 1, "Error: Total number of objects must be greater than or equal to 4"
    rows = rd.randint(1,tot_objects)
    current_view = np.empty([rows,5])
    classes = [*range(1,tot_objects+1)]
    for i in range(rows):
        current_view[i,0] = rd.randint(0,1280)
        current_view[i,1] = rd.randint(0,720)
        current_view[i,2] = rd.randint(0,1280)
        current_view[i,3] = rd.randint(0,720)
        obj_type = rd.choice(classes)
        for j in range(len(CLASS_PRIORITY)):
            if obj_type == CLASS_PRIORITY[j]:
                if j < highest_index:
                    highest_priority = CLASS_PRIORITY[j]
                    highest_index = j
        current_view[i,4] = obj_type
        classes.remove(obj_type)
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List F/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List F/ListF_ans.txt", "a") 
    L = str(highest_priority) + "\n"
    file1.writelines(L) 
    file1.close()

if __name__ == "__main__":
    # for i in range(100):
    #     list_A(MAX_OBJECTS,i)
        # list_B(i)
        # list_C(MAX_OBJECTS,i)
    # list_D(50)
    # list_E(50)
    for i in range(1000):
        list_F(MAX_OBJECTS,i)