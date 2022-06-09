# RAVN

This is a README for specifically for the 2020-2021 Capstone Team RAVN's code base

## Installation

There are no installations required beyond cloning the existing RoboCat's repository. 

```bash
git clone https://github.com/MSURoboCats/robotCode.git
```

## Usage
### Sensory_System.py
The input file path lives here. This file path needs point to where the current frame CSV is stored. Ideally this file is continually being overwritten by the OILT team's output, but this variable could be manipulated by a different python script for testing. 
```python
INPUT_FILE = "/some file path to current frame/CurrentFrame.csv"
```
The camera variables are also contained in this file and will need to be changed in the event a new camera is installed.
```python
CAMERA_X_FOV_DEGREES = 65.6
CAMERA_Y_FOV_DEGREES = 39.9
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720
FRAME_AREA = FRAME_PIXELS_X * FRAME_PIXELS_Y
```
The ``` get_objects() ``` handles the ingestion of the CSV file and parses it into a ```VisualObject``` class defined in the ```central_nervous_system.py``` file. It stores all of the data from the OILT CSV and has two helper functions. These functions return the class of an object and print out the class numbers of all of the objects stored in the class.
```python
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
```
### Central_Nervous_System.py
This is the file that the majority of the RAVN logic is contained within. The primary function is the ```search()``` function. It first checks if the ```relevant_types``` list is empty. This list contains the class numbers for the potential objects in the competition space and will need to be intialized by a club member at the time of competion. Next, there is a check if there is a target object to investigate. If not, the ```acquire_target(objet_list)``` is called.
```python
def acquire_target(object_list):
    for k in range(len(relevant_types)):       
            for item in object_list:                    
                if item.type == relevant_types[k]:
                    return item
```
This function take the list of objects in the frame and compares it to the list of object classes that are still to be investigated. It returns the highest priority object that has yet to be investigated. This object is now the object that needs to be investigated. If there are no objects in frame or all of them have been investigated, the sub needs to spin to find new objects.
In the case there is a target object identified, it first checks if the object is still in the frame. 
```python
def check_target_in_frame(object_list):     
    for item in object_list:                    
        if item.type == target_object.type:
            return True
    return False
```
It parses through the objects currently in view and checks if the target is still in frame. If so, it continues, if not the target object will be cleared and the system will need to call ```acquire_target(object_list)``` again. If the object is still in the frame, the sub will check if it is close enough to call the object investigated. The RAVN team defined this as the bounding box of the object takes up more than 80% of the screen. 
```python
def check_investigated(target):
    if target.dx > (ss.FRAME_PIXELS_X * .8) or target.dy > (ss.FRAME_PIXELS_Y * .8):
        return True
    else:
        return False
```
If the sub is close enough, it will remove that object class from the list and search for a new target. If not, the ```get_movement_vector(target_object)``` function is called. This function takes in the output from ```search``` and turns on the the thrusters to navigate the sub in the direction of the target object. The autonomous navigation is intiated by running the ```central_nervous_system.py``` Python file and will run until all of the objects have been removed from the list and the program will stop. This state is controlled by the ```vehicle_state``` variable and can take on the values ```SEARCH``` or ```TASKS_COMPLETE```.
### Motor_System.py
This code was written by the 2019-2020 Capstone team and was just copied over. The details for how these motor functions work can be found in their documentation.
### Wrapper
This file was used to complete the tests detailed in RAVN's Final Capstone Report. It could be used for more tests should more become necessary. 
## Contributing
Please contact the RoboCat's officers or Dr. Bradley Whitaker before making any changes to this code base
