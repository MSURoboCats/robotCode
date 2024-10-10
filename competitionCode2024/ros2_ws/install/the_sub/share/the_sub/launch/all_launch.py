import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    '''
    Launch motor and sensor micro controller nodes, forward rgb camera with
    detection model and center detector, and twist to motor powers translator.
    '''

    FORWARD_RGB_CAM_PORT = '1'
    FORWARD_RGB_DETECTION_MODEL = '8am_530pm_test_medium_batch'
    DOWNWARD_RGB_CAM_PORT = '0'
    DOWNWARD_RGB_DETECTION_MODEL = 'dry_buoy'


    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

#---------------------------------------------------------------------------------------------------------------
# HARDWARE-LEVEL NODES
#---------------------------------------------------------------------------------------------------------------

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
    
    '''
    # create node to publish frames from downward-facing RGB camera (pass 0 for camera index)
    downward_rgb_pub_node = launch_ros.actions.Node(
        namespace='downward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_publisher',
        name='downward_rgb_pub_node',
        arguments=[DOWNWARD_RGB_CAM_PORT],
    )
    ld.add_action(downward_rgb_pub_node)
    '''

    # create node to publish frames from forward-facing RGB camera (pass 1 for camera index)
    forward_rgb_pub_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_publisher',
        name='forward_rgb_pub_node',
        arguments=[FORWARD_RGB_CAM_PORT],
    )
    ld.add_action(forward_rgb_pub_node)


#---------------------------------------------------------------------------------------------------------------
# COMPUTER VISION NODES
#---------------------------------------------------------------------------------------------------------------
    '''
    # create node to subscribe to frames from downward-facing RGB camera
    downward_rgb_sub_node = launch_ros.actions.Node(
        namespace='downward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_subscriber',
        name='downward_rgb_sub_node',
        #remappings=[('/video_frames', '/downward_rgb_camera/video_frames')],
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
    '''

    # create node to detect objects from the forward-facing RGB camera
    forward_rgb_detection_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='yolov8_detector_node',
        name='forward_rgb_detection_node',
        arguments=[FORWARD_RGB_DETECTION_MODEL],
    )
    ld.add_action(forward_rgb_detection_node)

    '''
    # create node to detect objects from the downward-facing RGB camera
    downward_rgb_detection_node = launch_ros.actions.Node(
        namespace='downward_rgb_camera',
        package='the_sub',
        executable='yolov8_detector_node',
        name='downward_rgb_detection_node',
        arguments=[DOWNWARD_RGB_DETECTION_MODEL],
    )
    ld.add_action(downward_rgb_detection_node)
    '''

    # create node to detect objects horizontally centered in the frame from the forward rgb camera
    center_detection_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='center_detection_node',
        name='center_detection_node',
        remappings=[('/forward_rgb_camera/control_data', '/control_data')],
    )
    ld.add_action(center_detection_node)

#---------------------------------------------------------------------------------------------------------------
# CONTROL NODES
#---------------------------------------------------------------------------------------------------------------

    # create node to translate twist or string commands to motor powers
    twist2action_node = launch_ros.actions.Node(
        package='the_sub',
        executable='twist2action_node',
        name='twist2action_node',
    )
    ld.add_action(twist2action_node)

    '''
    # create node to publish twist messages from the keyboard
    keyboard_controller_node = launch_ros.actions.Node(
        package='the_sub',
        executable='keyboard_controller_node',
        name='keyboard_controller_node',
        remappings=[('/keyboard_control_twist', '/control_twist')],
    )
    ld.add_action(keyboard_controller_node)
    '''

    return ld