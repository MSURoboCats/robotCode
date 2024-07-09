import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    '''
    Launch file to go through motor mapping interface and save results
    '''

    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

    # create node for motor microcontroller (load motor mapping parameters) (voltage publishing off)
    motor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='motor_micro_node',
        name='motor_micro_node',
        parameters=[config],
        arguments=['voltage_off'],
    )
    ld.add_action(motor_micro_node)

    return ld