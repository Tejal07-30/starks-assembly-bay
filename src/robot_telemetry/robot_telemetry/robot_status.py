import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
import json

class RobotStatus(Node):

    def __init__(self):
        super().__init__("robot_status")

        self.j1 = 0.0
        self.j2 = 0.0
        self.j3 = 0.0

        self.create_subscription(Float32, "/joint1_command", self.j1_callback, 10)
        self.create_subscription(Float32, "/joint2_command", self.j2_callback, 10)
        self.create_subscription(Float32, "/joint3_command", self.j3_callback, 10)

        self.publisher = self.create_publisher(String, "/robot_status", 10)

        self.timer = self.create_timer(1.0, self.publish_status)

    def j1_callback(self, msg):
        self.j1 = msg.data

    def j2_callback(self, msg):
        self.j2 = msg.data

    def j3_callback(self, msg):
        self.j3 = msg.data

    def publish_status(self):

        safe = (
            0 <= self.j1 <= 180 and
            -180 <= self.j2 <= 180 and
            -5 <= self.j3 <= 20
        )

        data = {
            "joint1": round(self.j1, 1),
            "joint2": round(self.j2, 1),
            "joint3": round(self.j3, 1),
            "status": "SAFE" if safe else "LIMIT EXCEEDED"
        }

        msg = String()
        msg.data = json.dumps(data)

        self.publisher.publish(msg)

        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = RobotStatus()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()