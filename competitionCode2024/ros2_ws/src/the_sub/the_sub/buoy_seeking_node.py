'''
COMMAND LINE ARGS: ros2 run the_sub buoy_seeking_node <depth>
  depth: depth to perform the task at
'''

import rclpy
import rclpy.logging
from rclpy.node import Node

from std_msgs.msg import String

from interfaces.msg import DepthGoal, HeadingGoal, OrientedDetection

import sys

class BuoySeeker(Node):

    def __init__(self):
        super().__init__('buoy_seeking_node')

        # publisher for depth goal
        self.pub_depth_goal = self.create_publisher(
            DepthGoal,
            '/depth_goal',
            10,
        )

        # publisher for heading goal
        self.pub_heading_goal = self.create_publisher(
            HeadingGoal,
            '/heading_goal',
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
            '/forward_rgb_camera/oriented_detection', 
            self.oriented_detection_callback, 
            10,
        )

        # flow control variables
        self.depth_reached = False
        self.scan_stage = 0                 # Key: 
        self.gate_detected = False              # 0: rotating to start at (1,0,0,0)
        self.gate_heading_reached = False       # 1: rotating 180deg from start to (0,0,1,0)
                                                # 2: rotating from (0,0,1,0) back to start at (-1,0,0,0)
                                                # 3: gate has been detected!

        # max power for scannning rotation
        self.ROT_POWER = .1

    def depth_goal_status_callback(self, data: String) -> None:
        # run first:
        # only if the goal depth had not been previously reached
        if not self.depth_reached:
            self.depth_reached = True
            self.get_logger().info(data.data)

            # reorient to (1,0,0,0)
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 0.0
            heading.orientation.z = 0.0
            heading.orientation.w = 1.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.scan_stage = 0
            self.get_logger().info('Initializing scan at %s' % heading.orientation)

    def heading_goal_status_callback(self, data: String) -> None:
        # run third (ish):
        self.get_logger().info(data.data)

        # only if goal depth has been reached, a gate has been detected, scanning has stopped, and the heading goal had not been previously reached
        if self.depth_reached and self.gate_detected and self.scan_stage == 3 and not self.gate_heading_reached:
            self.gate_heading_reached = True
            self.get_logger().info('Exiting spin...')
            raise SystemExit
        
        # initial scan heading reached at (1,0,0,0): stage 0 compete
        elif self.depth_reached and not self.gate_detected and self.scan_stage == 0:
            # reorient to (0,0,1,0): 180deg CCW
            self.scan_stage = 1
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 1.0
            heading.orientation.z = 0.0
            heading.orientation.w = 0.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Rotating 180deg CCW to %s' % heading.orientation)

        # first 180deg compete to (0,0,1,0): stage 1 compete
        elif self.depth_reached and not self.gate_detected and self.scan_stage == 1:
            # reorient to (-1,0,0,0): 180deg CCW
            self.scan_stage = 2
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 0.0
            heading.orientation.z = 0.0
            heading.orientation.w = -1.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Rotating 180deg CCW to %s' % heading.orientation)
        
        # second 180deg compete to (-1,0,0,0): stage 2 compete
        elif self.depth_reached and not self.gate_detected and self.scan_stage == 2:
            self.get_logger().info('No gate detected after a full scan. Exiting spin...')
            raise SystemExit

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second (ish):
        # only if the goal depth has been reached, a gate has not been detected, and the detected object is a gate (with 80% certainty)
        if self.depth_reached and not self.gate_detected and data.detection.name == 'red_bouy' and data.detection.confidence > .8:
            self.gate_detected = True
            self.get_logger().info('Gate detected at %s' % data.orientation)

            # rotate to gate
            self.scan_stage = 3     # gate has been detected, stop 180deg scan loop
            heading = HeadingGoal()
            heading.orientation = data.orientation
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Scanning stopped. Rotating to gate at %s' % data.orientation)


def main(args=None):
  
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    buoy_seeker = BuoySeeker()

    # begin task by descending
    depth_goal = DepthGoal()
    depth_goal.depth = float(sys.argv[1])
    buoy_seeker.pub_depth_goal.publish(depth_goal)
    buoy_seeker.get_logger().info('Initial depth set to %.2f' % depth_goal.depth)
    
    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    try:
        rclpy.spin(buoy_seeker)
    except SystemExit:
        rclpy.logging.get_logger('Quitting').info('Task complete! Node killed.')
    

    # kill the node
    buoy_seeker.destroy_node()
    
    # shutdown the ROS client library for Python
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()