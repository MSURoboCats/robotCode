import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    '''
    Launch forward facing camera with '/forward_rgb_camera' namespace with
    detection model and centered detector publishing in the same namespace
    '''
    
    FORWARD_RGB_CAM_PORT = '1'
    FORWARD_RGB_DETECTION_MODEL = 'the_one'

    ld = launch.LaunchDescription()

    # get path to load node parameters from
    config = os.path.join(
        get_package_share_directory('the_sub'),
        'config',
        'params.yaml',
    )

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
    )
    ld.add_action(center_detection_node)

    # create node to track detections
    forward_rgb_track_node = launch_ros.actions.Node(
        namespace='forward_rgb_camera',
        package='the_sub',
        executable='tracker_node',
        name='tracker_node',
    )
    ld.add_action(forward_rgb_track_node)

    return ld