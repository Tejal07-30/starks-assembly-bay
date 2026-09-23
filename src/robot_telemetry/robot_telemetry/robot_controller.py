import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class RobotController(Node):

    def __init__(self):
        super().__init__("robot_controller")

        self.pub1 = self.create_publisher(Float32, "/joint1_command", 10)
        self.pub2 = self.create_publisher(Float32, "/joint2_command", 10)
        self.pub3 = self.create_publisher(Float32, "/joint3_command", 10)

        self.timer = self.create_timer(1.0, self.publish_values)

    def publish_values(self):

        j1 = random.uniform(0, 180)
        j2 = random.uniform(-220, 220)
        j3 = random.uniform(-10, 25)

        self.pub1.publish(Float32(data=j1))
        self.pub2.publish(Float32(data=j2))
        self.pub3.publish(Float32(data=j3))

        self.get_logger().info(
            f"Joint1={j1:.1f}, Joint2={j2:.1f}, Joint3={j3:.1f}"
        )

def main():
    rclpy.init()
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
