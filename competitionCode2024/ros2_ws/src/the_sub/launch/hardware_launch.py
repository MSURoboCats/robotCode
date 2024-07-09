import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    '''
    Launch file for motor and sensor microcontrollers and twist to motor powers translator
    '''

    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

    # create node for sensor microcontroller
    sensor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='sensor_micro_node',
        name='sensor_micro_node',
    )
    ld.add_action(sensor_micro_node)

    # create node for motor microcontroller (load motor mapping parameters) (voltage publishing on by default)
    motor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='motor_micro_node',
        name='motor_micro_node',
        parameters=[config],
    )
    ld.add_action(motor_micro_node)
    
    # create node to translate twist or string commands to motor powers
    twist2action_node = launch_ros.actions.Node(
        package='the_sub',
        executable='twist2action_node',
        name='twist2action_node',
    )
    ld.add_action(twist2action_node)

    return ld