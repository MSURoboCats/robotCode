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
- [template_documentation.py](#template_documentationpy)
- [sub_status_observer_node.py](#sub_status_observer_nodepy)
<br><br>

# `template_documentation.py`
[*Return to Node list*](#Node-Documentation)<br>
**File name:** [`name.py`](./src/the_sub/the_sub/)<br>
**Compiled name:** `name_from_setup.py`<br>
**Arguments:** `arguments`<br>
**Overview:** Quick description here of what the node does at a high level!

## Publishers
### `publisher_name`
**Topic:** `topic_name`<br>
**Message Type:** `MessageType`<br>

## Subscribers
### `subscriber_name`
**Topic:** `topic_name`<br>
**Message Type:** `MessageType`<br>
**Callback Function:** `callback_function`<br>

## Functionality
### Overall
Detailed look at how the node works
### Initialization
Details of what happens in `__init__()` besides setting publishers and subscribers.
### Callback Functions
#### `callback_function_name`functionality explained here
### Other Functions
#### `function_name`: functionality explained here


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
#### `print_sub()`
The screen is first cleared, and then the ASCII representation of the sub is printed, with all values being written from the internal variables that are continously updated by the callback functions.