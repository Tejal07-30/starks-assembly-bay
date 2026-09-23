from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'robot_telemetry'

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
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tejal',
    maintainer_email='tejal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'robot_controller = robot_telemetry.robot_controller:main',
		'robot_monitor = robot_telemetry.robot_monitor:main',
        'robot_status = robot_telemetry.robot_status:main',
        ],
    },
)
