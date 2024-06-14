from sensors.srv import GetControlData
import py_srvcli.sensor_micro_interface as sensors_interface

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(GetControlData, 'get_control_data', self.get_control_data_callback)       # CHANGE
        self.micro = sensors_interface.SensorArduino('/dev/ttyUSB0')

    def get_control_data_callback(self, request, response):
        response.data.depth = self.micro.get_control_data().get('depth')
        self.get_logger().info('Incoming request for control data\n')  # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()