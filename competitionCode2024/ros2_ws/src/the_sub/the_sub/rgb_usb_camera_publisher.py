'''
COMMAND LINE ARGS: ros2 run the_sub rgb_usb_camera_publisher <port_number> 
  port_number: indicates where to start opening ports from, eg. '1' would mean start looking at 'video1'
'''

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2
import sys
 
class ImagePublisher(Node):

  def __init__(self):
    super().__init__('image_publisher')
      
    # publisher for camera frames
    self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
      
    # publishing interval in seconds
    timer_period = .0625
      
    # timer for callback function
    self.timer = self.create_timer(timer_period, self.timer_callback)
         
    # create VideoCapture object, looping through ports as needed (capped at video20)
    self.cam_idx = int(sys.argv[1])
    self.cap = cv2.VideoCapture(self.cam_idx)
    while not self.cap.isOpened():
      self.cam_idx += 1
      self.cap = cv2.VideoCapture(self.cam_idx)
      if self.cam_idx > 20:
        self.get_logger().error('No camera found checking up through video%d' % self.cam_idx)
        break

    self.get_logger().info('Camera added on port %d' % self.cam_idx)

    # convert ROS Image message <-> OpenCV image
    self.br = CvBridge()
   
  def timer_callback(self):
    # read and publish if successful
    ret, frame = self.cap.read()
          
    if ret == True:
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
      self.get_logger().debug("Frame published by camera on video%d" % self.cam_idx)
    else:
      self.get_logger().warning('Camera on video%d failed to capture frame' % self.cam_idx)

  
def main(args=None):
  
  # initialize the rclpy library
  rclpy.init(args=args)
  
  # create the node
  image_publisher = ImagePublisher()
  
  # spin the node so the callback function is called
  rclpy.spin(image_publisher)
  
  # destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  image_publisher.destroy_node()
  
  # shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()