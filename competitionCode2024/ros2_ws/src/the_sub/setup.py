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
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'downward_publisher = the_sub.downward_publisher:main',
            'downward_subscriber = the_sub.downward_subscriber:main',

        ],
    },
)
