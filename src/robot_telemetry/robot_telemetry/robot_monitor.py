import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RobotMonitor(Node):

    def __init__(self):
        super().__init__("robot_monitor")

        self.j1 = 0.0
        self.j2 = 0.0
        self.j3 = 0.0

        self.create_subscription(Float32, "/joint1_command", self.j1_callback, 10)
        self.create_subscription(Float32, "/joint2_command", self.j2_callback, 10)
        self.create_subscription(Float32, "/joint3_command", self.j3_callback, 10)

    def print_status(self):
        s1 = "SAFE" if 0 <= self.j1 <= 180 else "LIMIT EXCEEDED"
        s2 = "SAFE" if -180 <= self.j2 <= 180 else "LIMIT EXCEEDED"
        s3 = "SAFE" if -5 <= self.j3 <= 20 else "LIMIT EXCEEDED"

        print("\n-*-*-*-*-*-*-*-")
        print(f"Joint 1: {self.j1:.1f}°   -> {s1}")
        print(f"Joint 2: {self.j2:.1f}°   -> {s2}")
        print(f"Joint 3: {self.j3:.1f} cm -> {s3}")

    def j1_callback(self, msg):
        self.j1 = msg.data
        self.print_status()

    def j2_callback(self, msg):
        self.j2 = msg.data
        self.print_status()

    def j3_callback(self, msg):
        self.j3 = msg.data
        self.print_status()

def main():
    rclpy.init()
    node = RobotMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
