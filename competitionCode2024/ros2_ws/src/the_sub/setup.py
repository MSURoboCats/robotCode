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
            'rgb_usb_camera_publisher = the_sub.rgb_usb_camera_publisher:main',
            'rgb_usb_camera_subscriber = the_sub.rgb_usb_camera_subscriber:main',
            'motor_micro_node = the_sub.motor_micro_node:main',
            'sensor_micro_node = the_sub.sensor_micro_node:main',
            'twist2action_node = the_sub.twist2action_node:main',
            'yolov8_detector_node = the_sub.yolov8_detector_node:main',
            'keyboard_controller_node = the_sub.keyboard_controller_node:main',
            'tester_node = the_sub.tester_node:main',
            'set_motor_mappings_node = the_sub.set_motor_mappings_node:main',
            'frame_saver_node = the_sub.frame_saver_node:main',
            'esc_tester_node = the_sub.esc_tester_node:main',
        ],
    },
)
