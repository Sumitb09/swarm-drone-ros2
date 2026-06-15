import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose

class LeaderNode(Node):

    def __init__(self):
        super().__init__('leader_node')

        self.publisher_ = self.create_publisher(
            Pose,
            'leader_pose',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_pose
        )

        self.x = 0.0

    def publish_pose(self):
        msg = Pose()

        msg.position.x = self.x
        msg.position.y = self.x * 0.5
        msg.position.z = 10.0

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing Pose -> x={msg.position.x:.1f}, '
            f'y={msg.position.y:.1f}, '
            f'z={msg.position.z:.1f}'
        )

        self.x += 1.0


def main(args=None):
    rclpy.init(args=args)

    node = LeaderNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
