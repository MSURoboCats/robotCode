import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import rclpy.parameter
from sensor_msgs.msg import Imu

from interfaces.srv import ControlData
from interfaces.msg import HullData

import the_sub.sensor_micro_interface as sensor_interface

class SensorArduinoNode(Node):

    def __init__(self):
        super().__init__('sensor_arduino_node')

        self.get_control_data = self.create_service(ControlData, 'control_data', self.control_data_callback)
        
        self.pub_hull_data = self.create_publisher(HullData, 'hull_data', 10)
        timer_period = 1
        self.time = self.create_timer(timer_period, self.pub_hull_data_callback)

        self.sensor_micro = sensor_interface.SensorArduino('/dev/ttyUSB0')
        
        '''
        Example Parameter:
        motor_mappings_descriptor = ParameterDescriptor(description="Maps each motor to an ESC - see Notion Code Companion motor_micro_main.ino for mappings.")
        self.declare_parameter('motor_mappings', [1,2,3,4,5,6,7,8], motor_mappings_descriptor)
        '''

    def control_data_callback(self, request, response):
        data = self.sensor_micro.get_control_data()

        response.imu_data.orientation.x = 0
        response.imu_data.orientation.y = 0
        response.imu_data.orientation.y = 0
        response.imu_data.orientation.w = 0
        response.angular_velocity.x = data.get('angular_velocity').get('x')
        response.angular_velocity.y = data.get('angular_velocity').get('y')
        response.angular_velocity.z = data.get('angular_velocity').get('z')
        response.linear_acceleration.x = data.get('linear_acceleration').get('x')
        response.linear_acceleration.y = data.get('linear_acceleration').get('y')
        response.linear_acceleration.z = data.get('linear_acceleration').get('z')
        response.depth = data.get('depth')

        self.get_logger().info('Sending control data: depth %.2fm' % response.depth)

        return response
    
    def pub_hull_data_callback(self):
        data = self.sensor_micro.get_environment_data()

        cur_conditions = HullData()
        cur_conditions.temperature.temperature = data.get('temperature')
        cur_conditions.pressure.fluid_pressure = data.get('pressure')
        cur_conditions.humidity.relative_humidity = data.get('humidity')

        self.pub_hull_data.publish(cur_conditions)
        self.get_logger().info('Publishing hull data: %.2fdegC' % cur_conditions.temperature.temperature)

def main(args=None):
    rclpy.init(args=args)

    arduino = SensorArduinoNode()

    rclpy.spin(arduino)

    rclpy.shutdown()

if __name__ == '__main__':
    main()