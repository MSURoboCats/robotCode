import sensory_system as ss
import central_nervous_system as cs
import csv
import time
import numpy as np

def test_1_1_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects()
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_1_1.txt", "a") 
        L = str(object_list) + "\n"
        file1.writelines(L) 
        file1.close() 

def test1_2_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects().copy()
        target = cs.search(object_list)
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_2_1.txt", "a") 
        L = str(target.type) + "\n"
        file1.writelines(L) 
        file1.close()
        print(i)

def test1():
    diff_priorities = [[1,2,3,4,5,6],[2,3,4,5,6,1],[3,4,5,6,1,2],[4,5,6,1,2,3],[5,6,1,2,3,4]]
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        if i % 20 == 0:
            obj_priority = diff_priorities[int(i/20)].copy()
        cs.relevant_types = obj_priority.copy()
        print(cs.relevant_types)
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects()
        target = cs.search(object_list)
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1.txt", "a") 
        L = str(target.type) + "\n"
        file1.writelines(L) 
        file1.close()
        print(i)
def test2_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/"
    for i in range(100):
        ss.INPUT_FILE = filepath + "CurrentFile" + str(i) + ".csv"
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        objects_list = cs.VisualObject(0,0,0,0,0)
        i = 0
        with open(ss.INPUT_FILE, 'r') as frame:
            frame_reader = csv.reader(frame)
            for column in frame_reader:
                if i == 0:
                    objects_list.cx = float(column[0])
                else:
                    objects_list.cy = float(column[0])
                i = i + 1
        [rotation_component, depth_component] = cs.get_movement_vector(objects_list)
        if rotation_component == 0:
            L = "CENTERED "
        elif rotation_component == 1:
            L = "RIGHT "
        elif rotation_component == -1:
            L = "LEFT "
        if depth_component == 0:
            L = L + "CENTERED" + "\n"
        elif depth_component == 1:
            L = L + "ASCEND" + "\n"
        elif depth_component == -1:
             L = L + "DESCEND" + "\n"   
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/Test2.txt", "a") 
        file1.writelines(L) 
        file1.close()

def test3_1_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/"
    for i in range(50):
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        ss.INPUT_FILE = filepath + "CurrentFile" + str(i) + ".csv"
        i = 0
        with open(ss.INPUT_FILE, 'r') as frame:
            frame_reader = csv.reader(frame)
            for column in frame_reader:
                if i == 0:
                    obj = cs.VisualObject(0,0,0,0,float(column[0]))
                    temp_view = [obj]
                    seen_objs = [float(column[1])]
                else:
                    obj = cs.VisualObject(0,0,0,0,float(column[0]))
                    temp_view.append(obj)
                    if float(column[1]) == 0:
                        pass
                    else:
                        seen_objs.append(float(column[1]))
                i = i + 1
        cs.relevant_types = [x for x in cs.relevant_types if x not in seen_objs]
        print(temp_view)
        target = cs.search(temp_view)
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/Test1.txt", "a") 
        L = str(target.type) + "\n"
        file1.writelines(L) 
        file1.close()


def test3_2_1():
    test_amount = 50
    filepath = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListD/"
    file1 = open(filepath + "ResultsD.txt", "w")
    tests_passed = 0
    for i in range(test_amount):
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        file1.writelines("#### Test " + str(i) + " ####\r")
        ss.INPUT_FILE = filepath + "CurrentFrame" + str(i) + ".csv"
        objects_in_frame = ss.get_objects().copy()
        while cs.relevant_types:
            objects_in_frame = ss.get_objects().copy()
            if cs.target_object:
                if cs.check_target_in_frame(objects_in_frame):
                    if cs.check_investigated():
                        cs.relevant_types.remove(cs.target_object.type)
                        L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None
                    else:
                        cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                        L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None #REMOVE IN ACTUAL OPERATION
                else:
                    L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                    file1.writelines(L)
                    cs.target_object = None
            else:
                cs.target_object = cs.acquire_target(objects_in_frame)
                if cs.target_object:
                    pass
                else:
                    L = "Searching...\r\r"
                    file1.writelines(L)
                    break

        if cs.relevant_types:
            ss.INPUT_FILE = filepath + "/NextFrame" + str(i) + ".csv"
            file1.writelines("# NextFrame" + str(i) + ".csv\r")

            while cs.relevant_types:
                cs.objects_in_frame = ss.get_objects().copy()
                if cs.target_object:
                    if cs.check_target_in_frame(objects_in_frame):
                        if cs.check_investigated():
                            cs.object_priority.remove(cs.target_object.type)
                            L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None
                        else:
                            cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                            L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None #REMOVE IN ACTUAL OPERATION
                    else:
                        L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                        file1.writelines(L)
                        cs.target_object = None
                else:
                    cs.target_object = cs.acquire_target(objects_in_frame)
                    if cs.target_object:
                        pass
                    else:
                        L = "Searching...\r\r"
                        tests_passed += 1
                        file1.writelines(L)
                        break

        else:
            tests_passed += 1
            file1.writelines("All objects are investigated. Program exited.\r")
            file1.writelines("\r")

    file1.writelines("------------------------------------------------------\r")
    file1.writelines(str(tests_passed) + " of " + str(test_amount) + " tests passed.\r")
    file1.close()
def test3():
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListE/ResultsE.txt", "w")
    tests_passed = 0
    test_amount = 50
    for i in range(test_amount):
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        file1.writelines("#### Test " + str(i) + " ####\r")
        ss.INPUT_FILE = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListE/CurrentFrame" + str(i) + ".csv"
        objects_in_frame = ss.get_objects().copy()
        cs.target_object = None
        
        file1.writelines("# CurrentFrame" + str(i) + ".csv\r")

        while cs.relevant_types:
            objects_in_frame = ss.get_objects().copy()
            if cs.target_object:
                if cs.check_target_in_frame(objects_in_frame):
                    if cs.check_investigated():
                        cs.relevant_types.remove(cs.target_object.type)
                        L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None
                    else:
                        cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                        L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None #REMOVE IN ACTUAL OPERATION
                else:
                    L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                    file1.writelines(L)
                    cs.target_object = None
            else:
                cs.target_object = cs.acquire_target(objects_in_frame)
                if cs.target_object:
                    pass
                else:
                    L = "Searching...\r\r"
                    file1.writelines(L)
                    break
                
        if cs.relevant_types:
            ss.INPUT_FILE = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListE/NextFrame" + str(i) + ".csv"
            file1.writelines("# NextFrame" + str(i) + ".csv\r")

            while cs.relevant_types:
                objects_in_frame = ss.get_objects().copy()
                if cs.target_object:
                    if cs.check_target_in_frame(objects_in_frame):
                        if cs.check_investigated():
                            cs.relevant_types.remove(cs.target_object.type)
                            L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None
                        else:
                            cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                            L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None #REMOVE IN ACTUAL OPERATION
                    else:
                        L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                        file1.writelines(L)
                        cs.target_object = None
                else:
                    cs.target_object = cs.acquire_target(objects_in_frame)
                    if cs.target_object:
                        pass
                    else:
                        L = "Searching...\r\r"
                        tests_passed += 1
                        file1.writelines(L)
                        break
                
        else:
            tests_passed += 1
            file1.writelines("All objects are investigated. Program exited.\r")
            file1.writelines("\r")

def full_test(filepath, i):
    ss.INPUT_FILE = filepath + str(i) + ".csv"
    object_list = ss.get_objects()
    target = cs.search(object_list)
    if target != None:
        cs.get_movement_vector(target)
    else:
        print("Spin")
if __name__ == '__main__':
    # test_1_1_1()
    # test1_2_1()
    # test1()
    # test3_2_1()
    # test3()
    # test2_1()
    # test3_1_1()
    times = np.zeros(1000)
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List F/CurrentFile"
    for i in range(1000):
        start = time.time()
        full_test(filepath,i)
        end = time.time()
        times[i] = end - start
    print("Min ",np.amin(times))
    print("Max ",np.amax(times))
    print("Mean ",np.mean(times))
    print("STD ", np.std(times))
    print("Median ", np.median(times))