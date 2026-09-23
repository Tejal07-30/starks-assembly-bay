from setuptools import find_packages, setup 
#It installs 2 packages findpackage - finds the python packages and setup - creates and install the packages
from glob import glob
#search for files and pathnames.It uses matching pattern instaead of using full expressions.
import os
#helps create file paths.
package_name = 'robot_telemetry'

#creating the package
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/robot_telemetry']
        ),
        (
            'share/robot_telemetry',
            ['package.xml']
        ),
        (
            os.path.join('share', 'robot_telemetry', 'launch'),
            glob('launch/*.py')
        ),
    ],
    install_requires=['setuptools'], #prerequisite required for the package 
    zip_safe=True, #optional
    maintainer='tejal',
    maintainer_email='tejal@todo.todo', #temporary placeholder...
    description='ROS 2 package for robot telemetry communication.', #can write TODO too
    license='TODO: License declaration',
    #creates executable commands
    entry_points={
        'console_scripts': [
		'robot_controller = robot_telemetry.robot_controller:main',
		'robot_monitor = robot_telemetry.robot_monitor:main',
        'robot_status = robot_telemetry.robot_status:main',
        ],
    },
)
