'''
COMMAND LINE ARGS: ros2 run the_sub buoy_seeking_node <depth>
  depth: depth to perform the task at
'''

import rclpy
import rclpy.logging
from rclpy.node import Node

from interfaces.msg import DepthGoal, HeadingGoal, OrientedDetection, Yolov8Detection, ControlData

from std_msgs.msg import String, Int16, Empty
from geometry_msgs.msg import Twist

import sys
import time

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

        # publisher for forward drive power
        self.pub_drive_twist = self.create_publisher(
            Twist,
            '/control_drive_twist',
            10,
        )

        # publisher for starting track
        self.pub_track_start = self.create_publisher(
            Int16,
            '/forward_rgb_camera/track_start',
            10,
        )

        # publisher for stopping track
        self.pub_track_stop = self.create_publisher(
            Empty,
            '/forward_rgb_camera/track_stop',
            10,
        )

        # publisher for starting depth controller
        self.pub_depth_controller_activation = self.create_publisher(
            Empty,
            '/depth_controller_activation',
            10,
        )

        # publisher for starting heading controller
        self.pub_heading_controller_activation = self.create_publisher(
            Empty,
            '/heading_controller_activation',
            10,
        )

        # publisher for stopping depth controller
        self.pub_depth_controller_deactivation = self.create_publisher(
            Empty,
            '/depth_controller_deactivation',
            10,
        )

        # publisher for stopping heading controller
        self.pub_heading_controller_deactivation = self.create_publisher(
            Empty,
            '/heading_controller_deactivation',
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

        # subscriber for any detections
        self.sub_any_detection = self.create_subscription(
            Yolov8Detection, 
            '/forward_rgb_camera/yolov8_detections', 
            self.any_detection_callback, 
            10,
        )

        # subscriber for control data
        self.sub_any_detection = self.create_subscription(
            ControlData, 
            '/control_data', 
            self.control_callback, 
            10,
        )

        # subscriber for track lost
        self.sub_track_lost = self.create_subscription(
            Empty,
            '/forward_rgb_camera/track_lost',
            self.track_lost_callback,
            10,
        )

        # flow control variable
        self.seek_stage = 0     # Key: 
                                    # 0: descendng to set depth
                                    # 1: depth reached; rotating to initialial search orientation 
                                    # 2: initial orientation reached; rotating the first 180deg CCW
                                    # 3: first 180deg complete; rotating the final 180deg CCW
                                    # 4: buoy detected; activate track, creep and check loop until close
                                    # 5: deactivate track, bump, and surface
        
        self.creep = False          # only run CV once it is needed
        self.initialized = False    # wait for control data to start publishing
        self.track_lost = False     # surface if the track is lost

        self.DETECTION_NAME = 'buoys'
        self.ROT_POWER = .1     # max power for scannning rotation
        self.DRIVE_POWER = .2   # power for driving forward

    def depth_goal_status_callback(self, data: String) -> None:
        # stage 0 complete:
        # only if the goal depth had not been previously reached
        if self.seek_stage == 0 and self.initialized:
            self.seek_stage = 1
            self.get_logger().info(data.data)

            # reorient to (1,0,0,0)
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 0.0
            heading.orientation.z = 0.0
            heading.orientation.w = 1.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 0 complete: depth reached')
            self.get_logger().info('Stage 1 started: initialize scan at y=%.2f' % heading.orientation.y)
        
        elif self.seek_stage == 5:
            self.get_logger().info('Stage 5 complete: surfaced and controllers killed')
            raise SystemExit

    def heading_goal_status_callback(self, data: String) -> None:
        # run third (ish):
        self.get_logger().info(data.data)
        
        # initial scan heading reached at (1,0,0,0): stage 1 compete
        if self.seek_stage == 1:
            # reorient to (0,0,1,0): 180deg CCW
            self.seek_stage = 2
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 1.0
            heading.orientation.z = 0.0
            heading.orientation.w = 0.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 1 complete: initial orientation reached')
            self.get_logger().info('Stage 2 started: rotate 180deg CCW to y=%.2f' % heading.orientation.y)

        # first 180deg compete to (0,0,1,0): stage 2 compete
        elif self.seek_stage == 2:
            # reorient to (-1,0,0,0): 180deg CCW
            self.seek_stage = 3
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 0.0
            heading.orientation.z = 0.0
            heading.orientation.w = -1.0
            heading.max_power = self.ROT_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 2 complete: 180deg CCW reached')
            self.get_logger().info('Stage 3 started: rotate 180deg CCW to y=%.2f' % heading.orientation.y)
        
        # second 180deg compete to (-1,0,0,0): stage 3 compete
        elif self.seek_stage == 3:
            self.get_logger().info('Stage 3 complete: 360deg net CCW reached')
            self.get_logger().info('No buoy detected after a full scan. Exiting spin...')
            raise SystemExit
        
        # buoy heading has been reached, loop creep and check
        elif self.seek_stage == 4 and self.creep == False:
            message = Int16()
            message.data = self.tracking_id
            self.pub_track_start.publish(message)
            self.get_logger().info('Stage 4 initiated: buoy heading reached and tracking started')
    
            self.creep = True
            self.get_logger().info('Stage 4 loop started: creep towards buoy')

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second (ish):
        # only if the goal depth has been reached, a buoy has not been detected, and the detected object is a buoy (with 80% certainty)
        if self.seek_stage in [1,2,3] and data.detection.name == self.DETECTION_NAME and data.detection.confidence > .8:
            self.buoy_detected = True
            self.get_logger().info('Stage 3 terminated: buoy detected at y=%.2f' % data.orientation.y)

            # rotate to buoy
            self.tracking_id = data.detection.tracking_id
            self.seek_stage = 4     # buoy has been detected, stop 180deg scan loop
            heading = HeadingGoal()
            heading.orientation = data.orientation
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 4 started: rotate to buoy at y=%.2f' % data.orientation.y)
            time.sleep(2)

    def any_detection_callback(self, data: Yolov8Detection) -> None:
        # surface if track is lost
        if self.creep and self.track_lost:
            self.creep = False
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 4 terminated: buoy lost')
            self.get_logger().info('Stage 5 started: surface')

        # creep towards the buoy if we have a detection for it
        if self.creep and data.name == self.DETECTION_NAME:
            
            # continue creeping if it is far away
            if data.dimensions.x < 200:
                drive_twist = Twist()
                drive_twist.linear.z = - self.DRIVE_POWER
                self.pub_drive_twist.publish(drive_twist)
                self.get_logger().info('Stage 4 looped: buoy far -> continue creep')
                time.sleep(2)

            # one last creep to bump it if we are close
            elif data.dimensions.x >= 200:

                # cancel creep and tracking
                self.creep = False
                self.pub_track_stop.publish(Empty())

                # bump into buoy
                drive_twist = Twist()
                drive_twist.linear.z = - self.DRIVE_POWER
                self.pub_drive_twist.publish(drive_twist)
                self.get_logger().info('Stage 4 loop broken: buoy close, last creep')
                time.sleep(4)

                # surface
                self.seek_stage = 5
                depth_goal =  DepthGoal()
                depth_goal.depth = 0.00
                self.pub_depth_goal.publish(depth_goal)
                self.get_logger().info('Stage 4 complete: buoy bumped')
                self.get_logger().info('Stage 5 started: surface')
    
    def control_callback(self, data: ControlData) -> None:
        if not self.initialized:
            self.initialized = True
            # activate depth and heading control nodees
            self.pub_depth_controller_activation.publish(Empty())
            self.pub_heading_controller_activation.publish(Empty())
            
            # begin task by descending
            depth_goal = DepthGoal()
            depth_goal.depth = float(sys.argv[1])
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 0 started: descending to %.2f' % depth_goal.depth)


    def track_lost_callback(self, data: Empty) -> None:
        self.track_lost = True
        
def main(args=None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    buoy_seeker = BuoySeeker()

    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    try:
        rclpy.spin(buoy_seeker)
    except SystemExit:
        rclpy.logging.get_logger('Quitting').info('Task complete! Node killed.')
    
    # kill the controllers
    buoy_seeker.pub_depth_controller_deactivation.publish(Empty())
    buoy_seeker.pub_heading_controller_deactivation.publish(Empty())

    # kill the node
    buoy_seeker.destroy_node()
    
    # shutdown the ROS client library for Python
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()