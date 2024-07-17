import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Quaternion, Twist

from interfaces.msg import DepthGoal, HeadingGoal, OrientedDetection, Yolov8Detection


class BuoySeeker(Node):

    def __init__(self):
        super().__init__('buoy_seeking_node')

        # publisher for depth goal
        self.pub_depth_goal = self.create_publisher(
            DepthGoal,
            'depth_goal',
            10,
        )

        # publisher for heading goal
        self.pub_heading_goal = self.create_publisher(
            HeadingGoal,
            'heading_goal',
            10,
        )

        # publisher for twists to control the sub rotationally about the y-axis only
        self.pub_twist = self.create_publisher(
            Twist,
            '/control_y_rot_twist',
            10,
        )

        # subscriper for depth goal status
        self.sub_depth_goal_status = self.create_subscription(
            String,
            '/depth_goal_status',
            self.depth_goal_status_callback,
            10,
        )

        # subscriper for heading goal status
        self.sub_heading_goal_status = self.create_subscription(
            String,
            '/heading_goal_status',
            self.heading_goal_status_callback,
            10,
        )

        # subscriber for centered detections
        self.sub_centered_detection = self.create_subscription(
            OrientedDetection, 
            'oriented_detection', 
            self.oriented_detection_callback, 
            10,
        )

        # subscriber for all detections
        self.sub_detection = self.create_subscription(
            Yolov8Detection, 
            '/forward_rgb_camera/oriented_detection', 
            self.detection_callback, 
            10,
        )

        self.depth_reached = False
        self.gate_detected = False
        self.heading_reached = False

        # max power for scannning rotation
        self.ROT_SPEED = .3

        # begin task be descending to 1.5m
        depth = DepthGoal()
        depth.depth = 1.5
        self.pub_depth_goal.publish(depth)

    def depth_goal_status_callback(self, data: String) -> None:
        # run first:
        # only if the goal depth had not been previously reached
        if not self.depth_reached:
            self.depth_reached = True
            self.get_logger().info(data.data)

            # start scanning in the positive y (CCW from top)
            twist = Twist()
            twist.angular.y = self.ROT_SPEED
            self.pub_twist.publish(twist)

    def heading_goal_status_callback(self, data: String) -> None:
        # run third:
        # only if goal depth has been reached, a gate has been detected, and the heading goal had not been previously reached
        if self.depth_reached and self.gate_detected and not self.heading_reached:
            self.heading_reached = True
            self.get_logger().info(data.data)

            # kill the node
            self.destroy_node()

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second:
        # only if the goal depth has been reached, a gate has not been detected, and the detected object is a gate (with 80% certainty)
        if self.depth_reached and not self.gate_detected and data.detection.name == 'red_bouy' and data.detection.confidence > .8:
            self.gate_detected = True
            self.get_logger().info('Gate detected at %s' % data.orientation)

            # stop scanning
            twist = Twist()
            self.pub_twist.publish(twist)

            # rotate to goal
            heading = HeadingGoal()
            heading.orientation = data.orientation
            self.pub_heading_goal.publish(heading)
    
    def detection_callback(self, data: Yolov8Detection) -> None:

        pass


def main(args=None):
  
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    buoy_seeker = BuoySeeker()

    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    rclpy.spin(buoy_seeker)

    # shutdown the ROS client library for Python
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()