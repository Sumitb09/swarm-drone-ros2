import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose


class FollowerNode(Node):

    def __init__(self):
        super().__init__('follower_node')

        self.declare_parameter('x_offset', 0.0)
        self.declare_parameter('y_offset', 0.0)
        self.declare_parameter('follower_id', 1)

        self.x_offset = self.get_parameter(
            'x_offset').value

        self.y_offset = self.get_parameter(
            'y_offset').value

        self.follower_id = self.get_parameter(
            'follower_id').value

        topic_name = f'/follower{self.follower_id}_pose'

        self.publisher = self.create_publisher(
            Pose,
            topic_name,
            10
        )

        self.subscription = self.create_subscription(
            Pose,
            '/leader_pose',
            self.pose_callback,
            10
        )

        self.get_logger().info(
            f'Follower {self.follower_id} publishing to {topic_name}'
        )

    def pose_callback(self, msg):

        follower_pose = Pose()

        follower_pose.position.x = msg.position.x + self.x_offset
        follower_pose.position.y = msg.position.y + self.y_offset
        follower_pose.position.z = msg.position.z

        follower_pose.orientation = msg.orientation

        self.publisher.publish(follower_pose)

        self.get_logger().info(
            f'Follower {self.follower_id} -> '
            f'x={follower_pose.position.x:.1f}, '
            f'y={follower_pose.position.y:.1f}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = FollowerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
