import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'the_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml')))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robocats',
    maintainer_email='dhjensen02@gmail.com',
    description='For the whole sub',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # hardware interface
            'motor_micro_node = the_sub.motor_micro_node:main',
            'sensor_micro_node = the_sub.sensor_micro_node:main',
            'rgb_usb_camera_publisher = the_sub.rgb_usb_camera_publisher:main',
            # computer vision
            'rgb_usb_camera_subscriber = the_sub.rgb_usb_camera_subscriber:main',
            'yolov8_detector_node = the_sub.yolov8_detector_node:main',
            'frame_saver_node = the_sub.frame_saver_node:main',
            'center_detection_node = the_sub.center_detection_node:main',
            # control
            'twist2action_node = the_sub.twist2action_node:main',
            'depth_controller_node = the_sub.depth_controller_node:main',
            'heading_controller_node = the_sub.heading_controller_node:main',
            'keyboard_controller_node = the_sub.keyboard_controller_node:main',
            'gui_control_node = the_sub.gui_control_node:main',
            'sub_status_observer_node = the_sub.sub_status_observer_node:main',
            'tracker_node = the_sub.tracker_node:main',
            # Tasks
            'gate_qual_node = the_sub.gate_qual_node:main',
            'buoy_task_node = the_sub.buoy_task_node:main',
            'gate_task_node = the_sub.gate_task_node:main',
            'octagon_task_node = the_sub.octagon_task_node:main',
            'mega_task_node = the_sub.mega_task_node:main',
            # setup
            'map_motors_node = the_sub.map_motors_node:main',
        ],
    },
)
