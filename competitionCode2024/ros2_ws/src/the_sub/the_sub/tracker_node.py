import rclpy
from rclpy.node import Node

from interfaces.msg import Yolov8Detection, ControlData, HeadingGoal

from std_msgs.msg import Int16, Empty
from geometry_msgs.msg import Quaternion


import numpy as np
import quaternion


class Tracker(Node):
    """
    Create an Tracker class to track provided detection
    """
    def __init__(self):
        super().__init__('tracker')

        # publisher for track lost
        self.pub_track_lost = self.create_publisher(
            Empty,
            'track_lost',
            10,
        )

        # publisher for heading goal
        self.pub_heading_goal = self.create_publisher(
            HeadingGoal,
            '/heading_goal',
            10,
        )

        # subscriber for detections
        self.sub_detection = self.create_subscription(
            Yolov8Detection, 
            'yolov8_detections', 
            self.detection_callback, 
            10,
        )
        
        # subscriber for control data
        self.sub_control = self.create_subscription(
            ControlData,
            '/control_data',
            self.control_callback,
            10,
        )

        # subscriber to start tracking
        self.sub_track_start = self.create_subscription(
            Int16,
            'track_start',
            self.track_start_callback,
            10,
        )

        # subscriber to stop tracking
        self.sub_track_stop = self.create_subscription(
            Empty,
            'track_stop',
            self.track_stop_callback,
            10,
        )

        self.current_quat = np.quaternion(1,0,0,0)
        self.saved_detections = []

        self.active = False
        self.tracking_id = None
        self.new_detection_counter = 0

        self.QUAT_FOV_LEFT = np.quaternion(.94, 0, .342, 0)
        self.QUAT_FOV_RIGHT = np.quaternion(.94, 0, -.342, 0)

    def detection_callback(self, data: Yolov8Detection) -> None:
        # if tracking is activated
        if self.active:

            # if the active object is detected, publish heading corrisponding to its location
            if data.tracking_id == self.tracking_id:
                self.new_detection_counter = 0
                np_quat = self.current_quat*quaternion.slerp(self.QUAT_FOV_LEFT, self.QUAT_FOV_RIGHT, 0, 1, data.center.x/640.0)
                ros_quat = Quaternion()
                ros_quat.x = np_quat.x
                ros_quat.y = np_quat.y
                ros_quat.z = np_quat.z
                ros_quat.w = np_quat.w
                message = HeadingGoal()
                message.orientation = ros_quat
                self.pub_heading_goal.publish(message)
    
    def control_callback(self, data: ControlData) -> None:
        if self.active:
            # if the active object hasn't been seen for 20 control callbacks, cancel the tracking
            self.new_detection_counter += 1
            if self.new_detection_counter > 15:
                self.active = False
                self.new_detection_counter = 0
                self.pub_track_lost.publish(Empty())
                self.get_logger().info('Track %d lost. Tracking deactivated' % self.tracking_id)
                return
            
            # update current quaternion heading
            self.current_quat = np.quaternion(
                    data.imu_data.orientation.w,
                    data.imu_data.orientation.x,
                    data.imu_data.orientation.y,
                    data.imu_data.orientation.z,
                )
    
    def track_start_callback(self, data: Int16) -> None:
        self.active = True
        self.tracking_id = data.data
        self.new_detection_counter = 0
        self.get_logger().info('Track started')

    def track_stop_callback(self, data: Empty) -> None:
        self.active = False
        self.get_logger().info('Track cancelled')
        
def main(args=None):
  
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    scanner = Tracker()

    # spin the node so the callback function is called.
    rclpy.spin(scanner)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    scanner.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()