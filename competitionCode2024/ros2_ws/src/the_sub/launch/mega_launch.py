import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit

def generate_launch_description():
    '''
    Launch all nodes needed for the gate, buoy, and octagon task
    '''
    
    ld = launch.LaunchDescription()

    DEPTH = '.53'
    FORWARD_RGB_CAM_PORT = '1'
    FORWARD_RGB_DETECTION_MODEL = '8am_530pm_test_medium_batch'

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

#---------------------------------------------------------------------------------------------------------------
# HARDWARE-LEVEL NODES
#---------------------------------------------------------------------------------------------------------------

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


#---------------------------------------------------------------------------------------------------------------
# COMPUTER VISION NODES
#---------------------------------------------------------------------------------------------------------------
    
    # create node to publish frames from forward-facing RGB camera (pass 1 for camera index)
    forward_rgb_pub_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='rgb_usb_camera_publisher',
        name='forward_rgb_pub_node',
        arguments=[FORWARD_RGB_CAM_PORT],
    )
    ld.add_action(forward_rgb_pub_node)

    # create node to detect objects from the forward-facing RGB camera
    forward_rgb_detection_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='yolov8_detector_node',
        name='forward_rgb_detection_node',
        arguments=[FORWARD_RGB_DETECTION_MODEL],
    )
    ld.add_action(forward_rgb_detection_node)

    # create node to detect objects horizontally centered in the frame 
    center_detection_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='center_detection_node',
        name='center_detection_node',
        remappings=[('/forward_rgb_camera/control_data', '/control_data')],
    )
    ld.add_action(center_detection_node)

    # create node to track detections
    forward_rgb_track_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='tracker_node',
        name='tracker_node',
        #remappings=[('/forward_rgb_camera/control_data', '/control_data'),
        #            ('/forward_rgb_camera/heading_goal', '/heading_goal')],
    )
    ld.add_action(forward_rgb_track_node)

#---------------------------------------------------------------------------------------------------------------
# CONTROL NODES
#---------------------------------------------------------------------------------------------------------------

    # create node to control depth
    depth_controller_node = launch_ros.actions.Node(
        package='the_sub',
        executable='depth_controller_node',
        name='depth_controller_node',
    )
    ld.add_action(depth_controller_node)

    # create node to control heading
    heading_controller_node = launch_ros.actions.Node(
        package='the_sub',
        executable='heading_controller_node',
        name='depth_controller_node',
    )
    ld.add_action(heading_controller_node)

#---------------------------------------------------------------------------------------------------------------
# TASK NODES
#---------------------------------------------------------------------------------------------------------------

    # gate task node
    gate_task_node = launch_ros.actions.Node(
        package='the_sub',
        executable='gate_task_node',
        name='gate_task_node',
        arguments=[DEPTH],
    )
    ld.add_action(gate_task_node)

    # buoy task node
    buoy_task_node = launch_ros.actions.Node(
        package='the_sub',
        executable='buoy_task_node',
        name='buoy_task_node',
        arguments=[DEPTH],
    )

    # octagon task node
    octagon_task_node = launch_ros.actions.Node(
        package='the_sub',
        executable='octagon_task_node',
        name='octagon_task_node',
        arguments=[DEPTH],
    )

#---------------------------------------------------------------------------------------------------------------
# FLOW 
#---------------------------------------------------------------------------------------------------------------
    
    on_gate_exit = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=gate_task_node,
            on_exit=[buoy_task_node],
        )
    )
    ld.add_action(on_gate_exit)

    
    on_buoy_exit = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=buoy_task_node,
            on_exit=[octagon_task_node],
        )
    )
    ld.add_action(on_buoy_exit)


    return ld