import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2
import sys
 
class ImageSubscriber(Node):

  def __init__(self):
    super().__init__('image_subscriber')
      
    # subscriber for camera frames
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
      
    # convert ROS Image message <-> OpenCV image
    self.br = CvBridge()
   
  def listener_callback(self, data):
    self.get_logger().info("Receiving frame")
    
    # convert to cv2 format and display
    current_frame = self.br.imgmsg_to_cv2(data)
    cv2.imshow("camera", current_frame)
    
    cv2.waitKey(1)
  
def main(args=None):
  
  # initialize the rclpy library
  rclpy.init(args=args)
  
  # create the node
  image_subscriber = ImageSubscriber()
  
  # spin the node so the callback function is called.
  rclpy.spin(image_subscriber)
  
  # destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  image_subscriber.destroy_node()
  
  # shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()