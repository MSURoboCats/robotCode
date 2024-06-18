import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import rclpy.parameter
from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers

import the_sub.motor_micro_interface as motor_interface

class MotorArduinoNode(Node):

    def __init__(self):
        super().__init__('motor_arduino_node')

        self.set_motor_power = self.create_service(MotorPowers, 'motor_powers', self.motor_powers_callback)
        
        self.pub_voltage = self.create_publisher(BatteryState, 'battery_health', 10)
        timer_period = 1
        self.time = self.create_timer(timer_period, self.pub_voltage_callback)

        self.motor_micro = motor_interface.MotorArduino('/dev/ttyACM0')
        
        motor_mappings_descriptor = ParameterDescriptor(description="Maps each motor to an ESC - see Notion Code Companion motor_micro_main.ino for mappings.")
        self.declare_parameter('motor_mappings', [1,2,3,4,5,6,7,8], motor_mappings_descriptor)

    def motor_powers_callback(self, request, response):
        self.motor_micro.run_motors([request.motor1,
                                     request.motor2,
                                     request.motor3,
                                     request.motor4,
                                     request.motor5,
                                     request.motor6,
                                     request.motor7,
                                     request.motor8])
        self.get_logger().info('Sending motor power values to arduino')
        return response
    
    def pub_voltage_callback(self):
        cur_health = BatteryState()
        cur_health.voltage = self.motor_micro.get_voltage()
        self.pub_voltage.publish(cur_health)
        self.get_logger().info('Publishing battery health: %.2fV' % cur_health.voltage)

def main(args=None):
    rclpy.init(args=args)

    arduino = MotorArduinoNode()

    rclpy.spin(arduino)

    rclpy.shutdown()

if __name__ == '__main__':
    main()