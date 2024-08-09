import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaces.msg import Yolov8Detection, ControlData, OrientedDetection

from geometry_msgs.msg import Quaternion
from std_msgs.msg import Empty

import numpy as np
import quaternion


class CenterScanner(Node):
    """
    Create an Scanner class to scan for detections in the center of the screen
    """
    def __init__(self):
        super().__init__('scanner')

        # publisher for centered detections
        self.pub_centered_detection = self.create_publisher(OrientedDetection, 'oriented_detection', 10)

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

        # subscriber for activating
        self.sub_activate = self.create_subscription(
            Empty,
            'activate_detections',
            self.activate_detections_callback,
            10,
        )

        # subscriber for deactivating
        self.sub_deactivate = self.create_subscription(
            Empty,
            'deactivate_detections',
            self.deactivate_detections_callback,
            10,
        )

        self.current_quat = np.quaternion(1,0,0,0)
        self.saved_detections = []
        self.active = True

        self.QUAT_FOV_LEFT = np.quaternion(.94, 0, .342, 0)
        self.QUAT_FOV_RIGHT = np.quaternion(.94, 0, -.342, 0)

    def detection_callback(self, data: Yolov8Detection) -> None:
        if data.center.x > 300 and data.center.x < 340 and data.tracking_id not in self.saved_detections and self.active == True:
            self.saved_detections.append(data.tracking_id)
            message = OrientedDetection()
            message.detection = data
            np_quat = self.current_quat*quaternion.slerp(self.QUAT_FOV_LEFT, self.QUAT_FOV_RIGHT, 0, 1, data.center.x/640.0)
            ros_quat = Quaternion()
            ros_quat.x = np_quat.x
            ros_quat.y = np_quat.y
            ros_quat.z = np_quat.z
            ros_quat.w = np_quat.w
            message.orientation = ros_quat
            self.pub_centered_detection.publish(message)
            self.get_logger().info("New object in center area detected")
    
    def control_callback(self, data: ControlData) -> None:
        # update current quaternion heading
        self.current_quat = np.quaternion(
                data.imu_data.orientation.w,
                data.imu_data.orientation.x,
                data.imu_data.orientation.y,
                data.imu_data.orientation.z,
            )
        
    def activate_detections_callback(self, data: Empty):
        self.active == True
        self.saved_detections = []
        self.get_logger().info('Detections activated')

    def deactivate_detections_callback(self, data: Empty):
        self.active == False
        self.saved_detections = []
        self.get_logger().info('Detections deactivated')

        
def main(args=None):
  
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    scanner = CenterScanner()

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