import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():

    FORWARD_RGB_CAM_PORT = '1'
    FORWARD_RGB_DETECTION_MODEL = 'yolov8n'
    DOWNWARD_RGB_CAM_PORT = '0'
    FORWARD_RGB_DETECTION_MODEL = 'yolov8n'


    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

    # create node for motor microcontroller (load motor mapping parameters)
    motor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='motor_micro_node',
        name='motor_micro_node',
        parameters=[config],
    )
    ld.add_action(motor_micro_node)

    
    # create node to call the service to run through settings motors
    set_motor_mappings_node = launch_ros.actions.Node(
        package='the_sub',
        executable='set_motor_mappings_node',
        name='set_motor_mappings_node',
    )
    ld.add_action(set_motor_mappings_node)

    return ld