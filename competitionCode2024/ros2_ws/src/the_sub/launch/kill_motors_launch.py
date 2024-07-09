import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    '''
    Launch file to kill all motors
    '''
    
    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

    # create node for motor microcontroller (load motor mapping parameters) (voltage publishing on)
    motor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='motor_micro_node',
        name='motor_micro_node',
        parameters=[config],
    )
    ld.add_action(motor_micro_node)

    # publish message to kill motors
    kill = launch.actions.ExecuteProcess(cmd=['ros2', 'topic', 'pub', '--once', '/motor_powers', 'interfaces/msg/MotorPowers',
                                       '{motor1: 0, motor2: 0, motor3: 0, motor4: 0, motor5: 0, motor6: 0, motor7: 0, motor8: 0}'])
    ld.add_action(kill)

    return ld