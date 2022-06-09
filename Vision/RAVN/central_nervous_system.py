# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

from enum import Enum

#import motor_system as ms
import sensory_system as ss

investigated_objects = []
novel_objects = []
relevant_types = [1, 3 , 4 ,5 ,2 ,6]
target_object = None
objects_in_frame = []

class State(Enum):
    SEARCH = 1
    INVESTIGATE = 2
    TASK_COMPLETED = 3

vehicle_state = State.SEARCH

class VisualObject:
    def __init__(self, cx, cy, dx, dy, type):
        self.cx = float(cx)
        self.cy = float(cy)
        self.dx = float(dx)
        self.dy = float(dy)
        self.type = float(type)

        self.bb_area = self.dx * self.dy

    def get_type(self):
        return self.type

    def __repr__(self):
        return "% f" % self.type

# target_info shoud be in the form: [heading, type]
def acquire_target(object_list):
    for k in range(len(relevant_types)):       
            for item in object_list:                    
                if item.type == relevant_types[k]:
                    return item                 

# Returns movement vector in form: [rotation_component, depth_component] where each value is in [-1, 0, 1].
# This will tell qualitatively which direcion the sub needs to move along each axis
def get_movement_vector(target_object):
    rotation_component = 0
    depth_component = 0
    if target_object.cx > ((ss.FRAME_PIXELS_X/2) + 25):
        rotation_component = 1
        print("ROTATE RIGHT")
    elif target_object.cx < ((ss.FRAME_PIXELS_X/2) - 25):
        rotation_component = -1
        print("ROTATE LEFT")
    else:
        print("DO NOT ROTATE")

    if target_object.cy > ((ss.FRAME_PIXELS_Y/2) + 25):
        depth_component = 1
        print("ASCEND")
    elif target_object.cy < ((ss.FRAME_PIXELS_Y/2) - 25):
        depth_component = -1
        print("DESCEND")
    else:
        print("DO NOT CHANGE DEPTH")

    return [rotation_component, depth_component]

def update_known_objects(object_list):
    for item in object_list:
        if item.type not in investigated_objects:
            if item.type not in relevant_types:
                # TO DO: mark heading object was seen at
                novel_objects.append(item)       

def search(object_list):
    target_object = None
    while relevant_types:
        # print("Getting objects from CSV")
        if target_object:
            # print("Target object already exists")
            if check_target_in_frame(object_list):
                # print("Target is in frame")
                if check_investigated(target_object):
                    # print("Marking object as investigated")
                    relevant_types.remove(target_object.type)
                    target_object = None
                else:
                    #print("Target is not yet investigatobject_listed")
                    # get_movement_vector(target_object)
                    pass
                return target_object
            else:
                # print("Target is NOT in frame -- Lost target object")
                target_object = None
        else:
            # print("Target object doesn't already exist - Aquiring Target")
            target_object = acquire_target(object_list)
            if target_object:
                # print("Successfully aquired target")
                # get_movement_vector(target_object)
                return target_object
            else:
                # print("No potential target -- entering search state")
                # search()
                target_object = None
                return None
            
        # print("")

def investigate(target_info):
    target_object = acquire_target(target_info)
    while (target_object.bb_area < ss.FRAME_AREA):
        get_movement_vector(target_object)
        # TO DO: develop ability to actually move the sub to the target
    vehicle_state = State.SEARCH

def enact_state(argument):
    switcher = {
        State.SEARCH: search,
        State.INVESTIGATE: investigate
    }
    action = switcher.get(argument, lambda: "Invalid state")
    action()

def check_target_in_frame(object_list):     
    for item in object_list:                    
        if item.type == target_object.type:
            return True
    return False

def check_investigated(target):
    if target.dx > (ss.FRAME_PIXELS_X * .8) or target.dy > (ss.FRAME_PIXELS_Y * .8):
        return True
    else:
        return False

if __name__ == "__main__":
    vehicle_state = None
    while vehicle_state != State.TASK_COMPLETED:
        enact_state(vehicle_state)
    print("All tasks completed")
