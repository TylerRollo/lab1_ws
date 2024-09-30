#!/usr/bin/env python3

from xml.etree.ElementTree import tostring
import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        # Declare parameters for speed (v) and steering angle (d)
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        # Create a publisher for AckermannDriveStamped messages
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)

        # Create a timer to publish messages as fast as possible (1 ms interval)
        self.timer_ = self.create_timer(1, self.publish_message)

    def publish_message(self):
        # Get the current values of the parameters
        v = self.get_parameter('v').get_parameter_value().double_value
        d = self.get_parameter('d').get_parameter_value().double_value

        # Create and populate the AckermannDriveStamped message
        msg = AckermannDriveStamped()
        msg.drive.speed = v
        msg.drive.steering_angle = d

        # Publish to drive_relay
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: speed={v}, steering_angle={d}')

    def print_values(self):
        v = self.get_parameter('v').get_parameter_value().double_value
        d = self.get_parameter('d').get_parameter_value().double_value

        print(v)
        print(d)

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()

    # Print out the values of speed (v) and steering angle (d)
    talker.print_values()

    # Spin the node to keep it running and publishing
    rclpy.spin(talker)

    # Shutdown the node when done
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
