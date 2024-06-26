import rclpy
from rclpy.node import Node

from interfaces.msg import Yolov8Detection

from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
import os
import sys
 
class Yolov8Detector(Node):

  def __init__(self):
    super().__init__('yolov8_detector_node')
    
    # subscriber for video feed
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
    
    # publisher for detected objects
    self.detector = self.create_publisher(Yolov8Detection, 'yolov8_detections', 10)

    # convert ROS Image message <-> OpenCV image
    self.br = CvBridge()

    # create TensorRT model if needed
    trt_model_path = os.path.join(os.getcwd(), 'models', str(sys.argv[1]) + '.engine')
    if not os.path.exists(trt_model_path):
      self.get_logger().info("Creating creating TensorRT model...give it some time")
      model = YOLO('models/' + (sys.argv[1]) + '.pt')
      model.export(format='engine')
      os.remove(os.path.join(os.getcwd(), 'models', str(sys.argv[1]) + '.onnx'))

    # load TensorRT model
    self.get_logger().info("Loading TensorRT model: %s" % (str(sys.argv[1]) + '.engine'))
    self.trt_model = YOLO(trt_model_path, task='detect')
    self.get_logger().info("Model loaded")
   
  def listener_callback(self, data: Image) -> None:
    self.get_logger().info("Receiving frame")
    
    # convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data)
    
    # get detection results
    results = self.trt_model.track(current_frame, persist=True)[0]
    
    # publish each detection
    for r in results:
      for box in r.boxes:
        if float(box.conf) > .7:
          detection = Yolov8Detection()
          detection.name = self.trt_model.names[int(box.cls)]
          if r.boxes.is_track:
            detection.tracking_id = int(box.id)
          detection.confidence = float(box.conf)
          detection.center.x = float(box.xywh[0][0])
          detection.center.y = float(box.xywh[0][1])
          detection.dimensions.x = float(box.xywh[0][2])
          detection.dimensions.y = float(box.xywh[0][3])
          self.detector.publish(detection)
          
          # draw circle for object center and add tracking ID
          current_frame = cv2.circle(current_frame, (int(detection.center.x), int(detection.center.y)), color=(0,0,255), radius=5, thickness=-1)
          current_frame = cv2.putText(current_frame,
                                      self.trt_model.names[int(box.cls)] + ': ' + str(detection.tracking_id) + '(' + str(detection.confidence) + ')',
                                      (int(detection.center.x), int(detection.center.y)),
                                      cv2.FONT_HERSHEY_SIMPLEX,
                                      1,
                                      (255, 255, 0),
                                      2, 
                                      cv2.LINE_AA)
    # show annotated image
    cv2.imshow("detections", current_frame)
    
    cv2.waitKey(1)
  
def main(args=None):
  
  # initialize the rclpy library
  rclpy.init(args=args)
  
  # create the node
  detector = Yolov8Detector()
  
  # spin the node so the callback function is called.
  rclpy.spin(detector)
  
  # destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  detector.destroy_node()
  
  # shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()