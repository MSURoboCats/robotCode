# ROS2 Workspace
Outline of file and file structure in the ROS2 workspace.

<details open>
<summary>File Structure</summary>

# File Structure
The follow outline shows the general file structure for all folders with files relevant to the design.
```
ros2-ws
├── bash_scripts
├── models
├── src
│   ├── interfaces
│   │   ├── msg
│   │   └── srv
│   └── the_sub
│       ├── config
│       ├── launch
│       ├── resource
│       ├── test
│       └── the_sub
└── training_data
```
- [`bash_scripts`](./bash_scripts/) holds bash scripts used to start and run multiple nodes for specific tasks. These files are used to start running the sub.
- [`models`](./models/) holds the computer vision models that are used. The `*.pt` models are in Yolo format, and the `*.engine` models are in a format accelerated for the Nvidia AGX Orin.
- [`src`](./src/) holds all the ROS2 code.
    - [`interfaces`](./src/interfaces/) holds custom defined messages and servicves.
    - [`the_sub/the_sub`](./src/the_sub/the_sub/) holds all the ROS2 nodes used to run the sub.
- [`training_data`](./training_data/) holds folders with images recorded from the on-board cameras
</details>

<details open>
<summary>Node Documentation</summary>

# Node Documentation
- [tracker_node.py](#tracker_nodepy)
- [sub_status_observer_node.py](#sub_status_observer_nodepy)
<br><br>

# tracker_node.py
[*Return to Node list*](#Node-Documentation)<br>
**File name:** [`tracker_node.py`](./src/the_sub/the_sub/)<br>
**Compiled name:** `tracker_node.py`<br>
**Arguments:** `Node`<br>
**Overview:** This node adjusts the sub's heading to track an object specified by it's tracking ID.

## Publishers
### `pub_track_lost`
**Topic:** `track_lost`<br>
**Message Type:** `Empty`<br>

### `pub_heading_goal`
**Topic:** `heading_goal`<br>
**Message Type:** `HeadingGoal`<br>

## Subscribers
### `sub_detection`
**Topic:** `yolov8_detections`<br>
**Message Type:** `Yolov8Detection`<br>
**Callback Function:** `detection_callback`<br>

### `sub_control`
**Topic:** `control_data`<br>
**Message Type:** `ControlData`<br>
**Callback Function:** `control_callback`<br>

### `sub_track_start`
**Topic:** `track_start`<br>
**Message Type:** `Int16`<br>
**Callback Function:** `track_start_callback`<br>

### `sub_track_stop`
**Topic:** `track_stop`<br>
**Message Type:** `Empty`<br>
**Callback Function:** `track_stop_callback`<br>

## Functionality
### Overall
This node takes in all published detections. When activated, it publishes commands to rotate the sub to track an object with a set tracking ID, passed on activation. Tracking continues until disabled or until the object is lost (no detections in frame).
### Initialization
Publishers and Subscribers are created. In addition, the field of view of the camera is defined as quaternions used to interpolate the pixel location of an object to the actual orientation.
### Callback Functions
#### `detection_callback`
A Yolov8Detection message is passed as a parameter.
If tracking is activated and active object is detected, this publishes a heading that corresponds to the location of the active object.
#### `control_callback`
A ControlData message is passed as a parameter.
The current orientation of the sub is saved to internal variables.
If tracking is activated and the active object hasn't been seen for 20 control callbacks, the tracking is cancelled.
#### `track_start_callback`
An Int16 message that holds the tracking id of the object to track is passed as a parameter.
This activates tracking for the passed object's tracking id, resets the detection counter used for cancelling the tracking, and logs that tracking has started.
#### `track_stop_callback`
An Empty message is passed as a parameter.
This stops tracking and logs that tracking was cancelled.
### Other Functions
#### `main()`
Initializes the rclpy library, creates the node, spins the node so the callback functions are enabled, and when quit, destroys the node explicitly and shuts down the ROS client library for Python.

# `sub_status_observer_node.py`
[*Return to Node list*](#Node-Documentation)<br>
**File name:** [`sub_status_observer_node.py`](./src/the_sub/the_sub/sub_status_observer_node.py)<br>
**Compiled name:** `sub_status_observer_node`<br>
**Arguments:** `None`<br>
**Overview:** This node displays information about the subs systems, including system voltage, temperature, pressure, and humidity as well as motor powers and sensor readings for depth, orientation, rotational velocities, and linear accelerations.

## Subscribers
### `voltage`
**Topic:** `battery_health`<br>
**Message Type:** `BatteryState`<br>
**Callback Function:** `voltage_callback`<br>
### `hull`
**Topic:** `hull_data`<br>
**Message Type:** `HullData`<br>
**Callback Function:** `hull_callback`<br>
### `control`
**Topic:** `control_data`<br>
**Message Type:** `ControlData`<br>
**Callback Function:** `control_callback`<br>
### `motor`
**Topic:** `motor_powers`<br>
**Message Type:** `MotorPowers`<br>
**Callback Function:** `motor_callback`<br>
## Functionality
### Overall
On the terminal, an ASCII representation of the sub is displayed with systems values. Each time new information about the system is received, internal variables holding the info are updated. Simultaneiously, the display is cleared and rewritten at 20 Hz.
### Initialization
Publishers and Subscribers are created. In addition, all displayed values are initialized to `0.0`.
### Callback Functions
#### `voltage_callback()`
When new voltage data is received, the corresponding internal variable is updated.
#### `hull_callback()`
When new temperature, pressure, and humidity data are received, the corresponding internal variables are updated.
#### `control_callback()`
When new IMU data are received, the corresponding internal variables are updated.
#### `motor_callback()`
When new motor powers are received, the corresponding internal variables are updated.
#### `refresh_callback()`
`print_sub()` is called at 20 Hz.
### Other Functions
#### `main()`
Initializes the rclpy library, creates the node, spins the node so the callback functions are enabled, and when quit, destroys the node explicitly and shuts down the ROS client library for Python.
#### `print_sub()`
The screen is first cleared, and then the ASCII representation of the sub is printed, with all values being written from the internal variables that are continously updated by the callback functions.