from setuptools import find_packages, setup

package_name = 'subConglomerate'

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
    maintainer='David Jensen',
    maintainer_email='dhjensen02@gmail.com',
    description='This is the package that controls the sub',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = subConglomerate.ex_publisher:main',
            'listener = subConglomerate.ex_subscriber:main',
        ],
    },
)
