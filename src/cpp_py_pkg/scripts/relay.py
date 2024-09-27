import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')

        # Create a subscriber to the 'drive' topic
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10
        )

        # Create a publisher for the modified AckermannDriveStamped messages
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

    def listener_callback(self, msg):
        # Multiply the speed and steering angle by 3
        new_speed = msg.drive.speed * 3
        new_steering_angle = msg.drive.steering_angle * 3

        # Create a new AckermannDriveStamped message
        new_msg = AckermannDriveStamped()
        new_msg.drive.speed = new_speed
        new_msg.drive.steering_angle = new_steering_angle

        # Publish the modified message to the 'drive_relay' topic
        self.publisher_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    relay = Relay()

    # Spin the node to keep it running and processing messages
    rclpy.spin(relay)

    # Shutdown the node when done
    relay.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
