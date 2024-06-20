import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():

    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml'
    )

    # create node for sensor microcontroller
    sensor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='sensor_micro_node',
        name='sensor_micro_node',
    )
    ld.add_action(sensor_micro_node)

    # create node for motor microcontroller (load motor mapping parameters)
    motor_micro_node = launch_ros.actions.Node(
        package='the_sub',
        executable='motor_micro_node',
        name='motor_micro_node',
        parameters=[config],
    )
    ld.add_action(motor_micro_node)

    # create node to publish frames from downward-facing RGB camera (pass 0 for camera index)
    downward_rgb_pub_node = launch_ros.actions.Node(
        namespace='downward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_publisher',
        name='downward_rgb_pub_node',
        arguments=['0'],
    )
    ld.add_action(downward_rgb_pub_node)

    # create node to publish frames from forward-facing RGB camera (pass 1 for camera index)
    forward_rgb_pub_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_publisher',
        name='forward_rgb_pub_node',
        arguments=['1'],
    )
    ld.add_action(forward_rgb_pub_node)

    # create node to subscribe to frames from downward-facing RGB camera
    downward_rgb_sub_node = launch_ros.actions.Node(
        package='the_sub',
        executable='rgb_usb_camera_subscriber',
        name='downward_rgb_sub_node',
        remappings=[('/video_frames', '/downward_rgb_camera/video_frames')],
    )
    ld.add_action(downward_rgb_sub_node)

    # create node to subscribe to frames from forward-facing RGB camera
    forward_rgb_sub_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_subscriber',
        name='forward_rgb_sub_node',
    )
    ld.add_action(forward_rgb_sub_node)

    # create node to translate twist or string commands to motor powers
    twist_transaltor = launch_ros.actions.Node(
        package='the_sub',
        executable='twist_translator_node',
        name='twist_command_translator',
    )
    ld.add_action(twist_transaltor)
    '''
    # create node for to test with
    tester_node = launch_ros.actions.Node(
        package='the_sub',
        executable='tester_node',
        name='tester_node',
    )
    ld.add_action(tester_node)
    '''

    return ld