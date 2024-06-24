import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2
import sys
import os
import numpy as np
 
class FrameSaver(Node):
  """
  Create an FrameSaver class, to save images from a provided topic to use for training CV models
  """
  def __init__(self):
    super().__init__('frame_saver')
      
    # create subscriber to a camera topic
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
    
    # specify how often images are saved in seconds
    timer_period = float(sys.argv[2])
      
    # Create the timer
    self.timer = self.create_timer(timer_period, self.timer_callback)

    # specify folder where images should be saved (inside workspace)
    self.file_path = os.path.join(os.getcwd(), 'cv_training_data', str(sys.argv[1]))
    os.mkdir(self.file_path)
    
    # create counter and image vars for current image
    self.counter = 0
    self.frame = None

    # convert ROS Image message to OpenCV image
    self.br = CvBridge()
   
  def listener_callback(self, data):
    self.frame = self.br.imgmsg_to_cv2(data)
  
  def timer_callback(self):
    full_img_path = os.path.join(self.file_path, str(self.counter) + '.jpg')
    if type(self.frame) == np.ndarray:
      cv2.imwrite(full_img_path, self.frame)
      self.get_logger().info("Frame saved: %s" % ('cv_training_data/' + str(sys.argv[1]) + '/' + str(self.counter) + '.jpg'))
      self.counter += 1
    else:
      self.get_logger().info("Frame lock not aquired")

  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  frame_saver = FrameSaver()
  
  # Spin the node so the callback function is called.
  rclpy.spin(frame_saver)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  frame_saver.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()