from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package="robot_telemetry",
            executable="robot_controller",
            output="screen"
        ),

        Node(
            package="robot_telemetry",
            executable="robot_monitor",
            output="screen"
        ),

        Node(
            package="robot_telemetry",
            executable="robot_status",
            output="screen"
        )

    ])