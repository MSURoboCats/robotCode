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
            'downward_publisher = the_sub.downward_publisher:main',
            'downward_subscriber = the_sub.downward_subscriber:main',
            'motor_micro_node = the_sub.motor_micro_node:main',
            'sensor_micro_node = the_sub.sensor_micro_node:main',
            'tester_node = the_sub.tester_node:main',

        ],
    },
)
