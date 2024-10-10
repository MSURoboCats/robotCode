'''
COMMAND LINE ARGS: ros2 run the_sub frame_saver_node <folder_name> <interval> --ros-args --remap /video_frames:=<topic_to_save_from>
  folder name: folder name THAT DOES NOT ALREADY EXIST to save the images in 
  interval: interval to save images at
'''

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
  Create an FrameSaver class to save images from a provided topic to use for training CV models
  """
  def __init__(self):
    super().__init__('frame_saver')
      
    # subscriber to /video_frames
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
    
    # specify folder name or path where images should be saved
    # note the base path is ros2_ws/training_data/
    self.file_path = os.path.join(os.getcwd(), 'training_data', str(sys.argv[1]))
    os.mkdir(self.file_path)

    # specify how often images are saved in seconds
    timer_period = float(sys.argv[2])
      
    # timer for callback function
    self.timer = self.create_timer(timer_period, self.timer_callback)
    
    # counter and image vars for current image
    self.counter = 0
    self.frame = None

    # convert ROS Image message <-> OpenCV image
    self.br = CvBridge()
   
  def listener_callback(self, data: Image) -> None:
    # save new frame in cv2 image format
    self.frame = self.br.imgmsg_to_cv2(data)
  
  def timer_callback(self) -> None:
    full_img_path = os.path.join(self.file_path, str(self.counter) + '.jpg')

    # ensure that a frame has been received before trying to save images
    if type(self.frame) == np.ndarray:
      cv2.imwrite(full_img_path, cv2.resize(self.frame, (640,640), interpolation=cv2.INTER_AREA))
      self.get_logger().info("Frame saved: %s" % ('/media/robocats/32GB_SD/' + str(sys.argv[1]) + '/' + str(self.counter) + '.jpg'))
      self.counter += 1
    else:
      self.get_logger().info("Frame lock not aquired")

  
def main(args=None):
  
  # initialize the rclpy library
  rclpy.init(args=args)
  
  # create the node
  frame_saver = FrameSaver()
  
  # spin the node so the callback function is called
  rclpy.spin(frame_saver)
  
  # destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  frame_saver.destroy_node()
  
  # shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()