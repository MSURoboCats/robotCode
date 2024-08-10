'''
COMMAND LINE ARGS: ros2 run the_sub gate_task_node <depth>
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


global forward_twist
forward_twist = Twist()

class GateTask(Node):

    def __init__(self):
        super().__init__('gate_task_node')

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
                                    # 4: gate detected; activate track, creep and check loop until close,
                                    #    then deactivate track, pass through, hold, and end script
                                    # 5: surfaced (if track is lost): end script
        
        self.creep = False          # only run CV once it is needed
        self.initialized = False    # wait for control data to start publishing
        self.track_lost = False     # surface if the track is lost
        self.success = False        # set as true if gate passed through

        self.DETECTION_NAME = 'red_ccw'
        self.ROT_POWER = .2         # max power for rotation
        self.SCAN_POWER = .1        # max power for scanning
        self.DRIVE_POWER = .25       # power for driving 
        self.BUMP_POWER = .3        # power for going through the gate

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
            # give time for the sub to stabilize at the surface
            time.sleep(2)
            # kill the controllers
            self.pub_depth_controller_deactivation.publish(Empty())
            self.pub_heading_controller_deactivation.publish(Empty())
            self.get_logger().info('Stage 5 complete: surfaced, stabilized, and controllers killed')
            raise SystemExit

    def heading_goal_status_callback(self, data: String) -> None:
        # run third (ish):
        self.get_logger().info(data.data)
        
        # initial scan heading reached at (1,0,0,0): stage 1 compete
        if self.seek_stage == 1:
            # reorient to (0,0,1,0): 180deg CCW
            time.sleep(2)
            self.seek_stage = 2
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 1.0
            heading.orientation.z = 0.0
            heading.orientation.w = 0.0
            heading.max_power = self.SCAN_POWER
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
            heading.max_power = self.SCAN_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 2 complete: 180deg CCW reached')
            self.get_logger().info('Stage 3 started: rotate 180deg CCW to y=%.2f' % heading.orientation.y)
        
        # second 180deg compete to (-1,0,0,0): stage 3 compete
        elif self.seek_stage == 3:
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 3 complete: 360deg net CCW reached')
            self.get_logger().info('Stage 5 started: surface as no gate detected after a full scan')
        
        # gate heading has been reached, loop creep and check
        elif self.seek_stage == 4 and self.creep == False:
            message = Int16()
            message.data = self.tracking_id
            self.pub_track_start.publish(message)
            self.get_logger().info('Stage 4 initiated: gate heading reached and tracking started')
            
            time.sleep(4)   
            
            self.creep = True
            drive_twist = Twist()
            drive_twist.linear.z = self.DRIVE_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop started: creep towards gate')

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second (ish):
        # only if the goal depth has been reached, a gate has not been detected, and the detected object is a gate (with 70% certainty)
        if self.seek_stage in [2,3] and data.detection.name == self.DETECTION_NAME and data.detection.confidence > .7:
            self.get_logger().info('Stage 3 terminated: gate detected at y=%.2f' % data.orientation.y)

            # rotate to gate
            self.tracking_id = data.detection.tracking_id
            self.seek_stage = 4     # gate has been detected, stop 180deg scan loop
            heading = HeadingGoal()
            heading.orientation = data.orientation
            global forward_twist
            forward_twist = data.orientation
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 4 started: rotate to gate at y=%.2f' % data.orientation.y)
            time.sleep(1)

    def any_detection_callback(self, data: Yolov8Detection) -> None:
        # surface if track is lost
        if self.creep and self.track_lost:
            self.creep = False
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 4 terminated: gate lost')
            self.get_logger().info('Stage 5 started: surface')

        # stop creeping if we are close to the gate
        if self.creep and data.name == self.DETECTION_NAME and data.dimensions.x >= 90:
                
            # cancel creep and tracking
            self.creep = False
            self.pub_track_stop.publish(Empty())

            # pass through gate
            drive_twist = Twist()
            drive_twist.linear.z = self.DRIVE_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop broken: gate close, last push')
            time.sleep(8.5)
            drive_twist.linear.z = 0.0
            self.pub_drive_twist.publish(drive_twist)

            # hold and exit
            self.get_logger().info('Stage 4 complete: gate passed; holding')
            self.success = True
            raise SystemExit
    
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


class BuoyTask(Node):

    def __init__(self):
        super().__init__('buoy_task_node')

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

        # publisher for twists to control the sub
        self.pub_manual_control = self.create_publisher(
            Twist,
            '/control_twist',
            10,
        )

        # publisher for activating detections
        self.pub_activate_detections = self.create_publisher(
            Empty,
            '/forward_rgb_camera/activate_detections',
            10,
        )

        # publisher for deactivating detections
        self.pub_deactivate_detections = self.create_publisher(
            Empty,
            '/forward_rgb_camera/deactivate_detections',
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
        self.seek_stage = 1     # Key: 
                                    # 0: descendng to set depth
                                    # 1: depth reached; rotating to initialial search orientation 
                                    # 2: initial orientation reached; rotating the first 180deg CCW
                                    # 3: first 180deg complete; rotating the final 180deg CCW
                                    # 4: buoy detected; activate track, creep and check loop until close,
                                    #    then deactivate track, bump, scoot out of the way, and end script
                                    # 5: surfaced (if track is lost): end script
        
        self.creep = False          # only run CV once it is needed
        self.initialized = True     # wait for control data to start publishing
        self.track_lost = False     # surface if the track is lost
        self.success = False        # set as true if buoy bumped

        self.DETECTION_NAME = 'buoy_red'
        self.ROT_POWER = .2         # max power rotation
        self.SCAN_POWER = .1        # max power for scanning
        self.DRIVE_POWER = .25       # power for driving 
        self.BUMP_POWER = .3        # power for bumping the buoy
        

        #-- SKIP THE FIRST STAGE AND JUST CONTINUE AT THE SAME DEPTH AS BEFORE
        # reorient to (1,0,0,0)
        time.sleep(1)
        heading = HeadingGoal()
        heading.orientation.x = 0.0
        heading.orientation.y = 0.0
        heading.orientation.z = 0.0
        heading.orientation.w = 1.0
        heading.max_power = self.ROT_POWER
        self.pub_heading_goal.publish(heading)
        self.get_logger().info('Stage 1 started: initialize scan at y=%.2f' % heading.orientation.y)
        
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
            time.sleep(2)
            # kill the controllers
            self.pub_depth_controller_deactivation.publish(Empty())
            self.pub_heading_controller_deactivation.publish(Empty())
            self.get_logger().info('Stage 5 complete: surfaced, stabilized, and controllers killed')
            raise SystemExit

    def heading_goal_status_callback(self, data: String) -> None:
        # run third (ish):
        self.get_logger().info(data.data)
        
        # initial scan heading reached at (1,0,0,0): stage 1 compete
        if self.seek_stage == 1:
            # reorient to (0,0,1,0): 180deg CCW
            time.sleep(2)
            self.seek_stage = 2
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 1.0
            heading.orientation.z = 0.0
            heading.orientation.w = 0.0
            heading.max_power = self.SCAN_POWER
            self.pub_heading_goal.publish(heading)
            self.pub_activate_detections.publish(Empty())
            self.get_logger().info('Stage 1 complete: initial orientation reached')
            self.get_logger().info('Stage 2 started: detections activated; rotate 180deg CCW to y=%.2f' % heading.orientation.y)

        # first 180deg compete to (0,0,1,0): stage 2 compete
        elif self.seek_stage == 2:
            # reorient to (-1,0,0,0): 180deg CCW
            self.seek_stage = 3
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 0.0
            heading.orientation.z = 0.0
            heading.orientation.w = -1.0
            heading.max_power = self.SCAN_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 2 complete: 180deg CCW reached')
            self.get_logger().info('Stage 3 started: rotate 180deg CCW to y=%.2f' % heading.orientation.y)
        
        # second 180deg compete to (-1,0,0,0): stage 3 compete
        elif self.seek_stage == 3:
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 3 complete: 360deg net CCW reached')
            self.get_logger().info('Stage 5 started: surface as no buoy detected after a full scan')
        
        # buoy heading has been reached, loop creep and check
        elif self.seek_stage == 4 and self.creep == False:
            message = Int16()
            message.data = self.tracking_id
            self.pub_track_start.publish(message)
            self.get_logger().info('Stage 4 initiated: buoy heading reached and tracking started')
            time.sleep(5)

            self.creep = True
            drive_twist = Twist()
            drive_twist.linear.z = self.DRIVE_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop started: creep towards buoy')

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second (ish):
        # only if the goal depth has been reached, a buoy has not been detected, and the detected object is a buoy (with 65% certainty)
        if self.seek_stage in [2,3] and data.detection.name == self.DETECTION_NAME and data.detection.confidence > .7:
            self.buoy_detected = True
            self.get_logger().info('Stage 3 terminated: buoy detected at y=%.2f' % data.orientation.y)

            # rotate to buoy
            self.tracking_id = data.detection.tracking_id
            self.seek_stage = 4     # buoy has been detected, stop 180deg scan loop
            heading = HeadingGoal()
            heading.orientation = data.orientation
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 4 started: rotate to buoy at y=%.2f' % data.orientation.y)
            time.sleep(1)

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

        # stop creeping if we are close to the buoy
        if self.creep and data.name == self.DETECTION_NAME and data.dimensions.x >= 200:
                
            # cancel creep and tracking
            self.creep = False
            self.pub_track_stop.publish(Empty())

            # bump into buoy
            drive_twist = Twist()
            drive_twist.linear.z = self.BUMP_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop broken: buoy close, last push')
            time.sleep(3)
            self.get_logger().info('Stage 4 complete: buoy bumped; scoot out of the way and hold')


            # deactivate heading control, scoot sideways, reactivate heading conrol, and exit
            self.pub_heading_controller_deactivation.publish(Empty())
            drive_twist.linear.z = 0.0
            drive_twist.linear.x = -self.BUMP_POWER
            self.pub_drive_twist.publish(drive_twist)
            time.sleep(5)
            drive_twist.linear.x = 0.0
            self.pub_drive_twist.publish(drive_twist)
            self.pub_heading_controller_activation.publish(Empty())
            self.success = True
            raise SystemExit
            
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


class OctagonTask(Node):

    def __init__(self):
        super().__init__('octagon_task_node')

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

        # publisher for activating detections
        self.pub_activate_detections = self.create_publisher(
            Empty,
            '/forward_rgb_camera/activate_detections',
            10,
        )

        # publisher for deactivating detections
        self.pub_deactivate_detections = self.create_publisher(
            Empty,
            '/forward_rgb_camera/deactivate_detections',
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
        self.seek_stage = 1     # Key: 
                                    # 0: descendng to set depth
                                    # 1: depth reached; rotating to initialial search orientation 
                                    # 2: initial orientation reached; rotating the first 180deg CCW
                                    # 3: first 180deg complete; rotating the final 180deg CCW
                                    # 4: table detected; activate track, creep and check loop until close,
                                    #    then deactivate track and surface
                                    # 5: surfaced (on success or if track is lost): end script
        
        self.creep = False          # only run CV once it is needed
        self.initialized = True     # wait for control data to start publishing
        self.track_lost = False     # surface if the track is lost
        self.success = False        # set as true if gate passed through

        self.DETECTION_NAME = 'table'
        self.ROT_POWER = .2         # max power rotation
        self.SCAN_POWER = .1        # max power for scanniing
        self.DRIVE_POWER = .25       # power for driving 
        self.BUMP_POWER = .3        # power for last approach to table

        
        #-- SKIP THE FIRST STAGE AND JUST CONTINUE AT THE SAME DEPTH AS BEFORE
        # reorient to (1,0,0,0)
        time.sleep(3)
        heading = HeadingGoal()
        heading.orientation.x = 0.0
        heading.orientation.y = 0.0
        heading.orientation.z = 0.0
        heading.orientation.w = 1.0
        heading.max_power = self.ROT_POWER
        self.pub_heading_goal.publish(heading)
        self.get_logger().info('Stage 1 started: initialize scan at y=%.2f' % heading.orientation.y)
        

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
            # give time for the sub to stabilize at the surface
            time.sleep(2)
            # kill the controllers
            self.pub_depth_controller_deactivation.publish(Empty())
            self.pub_heading_controller_deactivation.publish(Empty())
            self.get_logger().info('Stage 5 complete: surfaced, stabilized, and controllers killed')
            raise SystemExit

    def heading_goal_status_callback(self, data: String) -> None:
        # run third (ish):
        self.get_logger().info(data.data)
        
        # initial scan heading reached at (1,0,0,0): stage 1 compete
        if self.seek_stage == 1:
            # reorient to (0,0,1,0): 180deg CCW
            time.sleep(2)
            self.seek_stage = 2
            heading = HeadingGoal()
            heading.orientation.x = 0.0
            heading.orientation.y = 1.0
            heading.orientation.z = 0.0
            heading.orientation.w = 0.0
            heading.max_power = self.SCAN_POWER
            self.pub_heading_goal.publish(heading)
            self.pub_activate_detections.publish(Empty())
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
            heading.max_power = self.SCAN_POWER
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 2 complete: 180deg CCW reached')
            self.get_logger().info('Stage 3 started: rotate 180deg CCW to y=%.2f' % heading.orientation.y)
        
        # second 180deg compete to (-1,0,0,0): stage 3 compete
        elif self.seek_stage == 3:
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 3 complete: 360deg net CCW reached')
            self.get_logger().info('Stage 5 started: surface as no table detected after a full scan')
        
        # table heading has been reached, loop creep and check
        elif self.seek_stage == 4 and self.creep == False:
            message = Int16()
            message.data = self.tracking_id
            self.pub_track_start.publish(message)
            self.get_logger().info('Stage 4 initiated: table heading reached and tracking started')
    
            self.creep = True
            drive_twist = Twist()
            drive_twist.linear.z = self.DRIVE_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop started: creep towards table')

    def oriented_detection_callback(self, data: OrientedDetection) -> None:
        # run second (ish):
        # only if the goal depth has been reached, a table has not been detected, and the detected object is a table (with 50% certainty)
        if self.seek_stage in [2,3] and data.detection.name == self.DETECTION_NAME and data.detection.confidence > .5:
            self.get_logger().info('Stage 3 terminated: table detected at y=%.2f' % data.orientation.y)

            # rotate to table
            self.tracking_id = data.detection.tracking_id
            self.seek_stage = 4     # table has been detected, stop 180deg scan loop
            heading = HeadingGoal()
            heading.orientation = data.orientation
            self.pub_heading_goal.publish(heading)
            self.get_logger().info('Stage 4 started: rotate to table at y=%.2f' % data.orientation.y)
            time.sleep(1)

    def any_detection_callback(self, data: Yolov8Detection) -> None:
        # surface if track is lost
        if self.creep and self.track_lost:
            self.creep = False
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 4 terminated: table lost')
            self.get_logger().info('Stage 5 started: surface')

        # stop creeping if we are close to the table
        if self.creep and data.name == self.DETECTION_NAME and data.dimensions.x >= 160:
                
            # cancel creep and tracking
            self.creep = False
            self.pub_track_stop.publish(Empty())

            # last approach to table
            drive_twist = Twist()
            drive_twist.linear.z = self.BUMP_POWER
            self.pub_drive_twist.publish(drive_twist)
            self.get_logger().info('Stage 4 loop broken: table close, last push')
            time.sleep(5)
            drive_twist.linear.z = 0.0
            self.pub_drive_twist.publish(drive_twist)

            # surface
            self.success = True
            self.seek_stage = 5
            depth_goal =  DepthGoal()
            depth_goal.depth = 0.00
            self.pub_depth_goal.publish(depth_goal)
            self.get_logger().info('Stage 4 complete: table reached')
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
    
#-- GATE task
    gate_task = GateTask()

    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    try:
        rclpy.spin(gate_task)
    except SystemExit:
        rclpy.logging.get_logger('Quitting').info('Gate task complete! Node killed.')
        if gate_task.success == False:
            rclpy.shutdown()
            return
    
#-- BUOY task 
    buoy_task = BuoyTask()

    #-- DO A COUPLE SPINS TO START OUT WITH
    buoy_task.get_logger().info('Spinning for 10 seconds')
    buoy_task.pub_heading_controller_deactivation.publish(Empty())  # deactivate heading
    buoy_task.pub_deactivate_detections.publish(Empty())            # deactivate detections
    rot_twist = Twist()                                             # start spinning
    rot_twist.angular.y = 0.6
    buoy_task.pub_manual_control.publish(rot_twist)

    time.sleep(14)                                                  # spin...

    rot_twist.angular.y = 0.0                                       # stop spinning
    buoy_task.get_logger().info('Spinning complete')
    buoy_task.pub_manual_control.publish(rot_twist)
    heading = HeadingGoal()                                         # rotate to original heading
    heading.orientation.x = 0.0
    heading.orientation.y = 0.0
    heading.orientation.z = 0.0
    heading.orientation.w = 1.0
    heading.max_power = buoy_task.ROT_POWER
    buoy_task.pub_heading_goal.publish(heading)
    buoy_task.pub_heading_controller_activation.publish(Empty())    # activate heading

    time.sleep(8)                                                   # wait a bit
    
    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    try:
        rclpy.spin(buoy_task)
    except SystemExit:
        rclpy.logging.get_logger('Quitting').info('Buoy task complete! Node killed.')
        if buoy_task.success == False:
            rclpy.shutdown()
            return
    

#-- OCTAGON task
    octagon_task = OctagonTask()
    
    # get closer to the table hopefully with center detections deactivated
    octagon_task.pub_deactivate_detections.publish(Empty())
    octagon_task.get_logger().info('Attempting to get closer to the table: rotating toward it?')
    #-- rotate in same direction gate was detected
    global forward_twist
    heading = HeadingGoal()
    heading.orientation = forward_twist
    heading.max_power = octagon_task.ROT_POWER
    octagon_task.pub_heading_goal.publish(heading)
    time.sleep(15)
    #-- creep forward for some time, the spin up node to scan
    octagon_task.get_logger().info('Attempting to get closer to the table: approaching it?')
    drive_twist = Twist()
    drive_twist.linear.z = octagon_task.DRIVE_POWER
    octagon_task.pub_drive_twist.publish(drive_twist)
    time.sleep(10)
    drive_twist = Twist()
    drive_twist.linear.z = 0.0
    octagon_task.pub_drive_twist.publish(drive_twist)   
    
    # spin the node so the task can be begin
    # node will automatically destory itself on completion
    try:
        rclpy.spin(octagon_task)
    except SystemExit:
        rclpy.logging.get_logger('Quitting').info('Task complete! Node killed.')
        if octagon_task.success == False:
            rclpy.shutdown()
            return

    # shutdown the ROS client library for Python
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()