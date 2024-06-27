import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaces.msg import Yolov8Detection, ControlData, OrientedDetection

from geometry_msgs.msg import Quaternion


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
            'control_data',
            self.control_callback,
            10,
        )

        self.current_quat = Quaternion()
        self.saved_detections = []

    def detection_callback(self, data: Yolov8Detection) -> None:
        if data.center.x > 300 and data.center.x < 340 and data.tracking_id not in self.saved_detections:
            self.saved_detections.append(data.tracking_id)
            message = OrientedDetection()
            message.detection = data
            message.orientation = self.current_quat
            self.pub_centered_detection.publish(message)
            self.get_logger().info("New object in center area detected")
    
    def control_callback(self, data: ControlData) -> None:
        self.current_quat = data.imu_data.orientation


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