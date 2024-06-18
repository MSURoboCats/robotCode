import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import rclpy.parameter
from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers

import the_sub.motor_micro_interface as motor_interface
from std_srvs.srv import Empty

class MotorArduinoNode(Node):

    def __init__(self):
        super().__init__('motor_arduino_node')

        self.set_motor_power = self.create_service(MotorPowers, 'motor_powers', self.motor_powers_callback)
        
        self.set_mappings = self.create_service(Empty, "motor_mappings", self.motor_mappings_callback)

        self.pub_voltage = self.create_publisher(BatteryState, 'battery_health', 10)
        timer_period = 1
        self.time = self.create_timer(timer_period, self.pub_voltage_callback)

        self.motor_micro = motor_interface.MotorArduino('/dev/ttyACM0')
        
        motor_mappings_descriptor = ParameterDescriptor(description="Maps each motor to an ESC - see Notion Code Companion motor_micro_main.ino for mappings.")
        self.declare_parameter('motor_mappings', [1,2,3,4,5,6,7,8], motor_mappings_descriptor)

        motor_directions_descriptor = ParameterDescriptor(description="Determines whether each motor should be reversed or not (0 for normal, 1 for reversed)")
        self.declare_parameter('motor_directions', [0,0,0,0,0,0,0,0], motor_directions_descriptor)

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
    
    def motor_mappings_callback(self, request, response):
        mappings, directions = self.motor_micro.set_assignments()

        updated_mappings = rclpy.parameter.Parameter(
            'motor_mappings',
            rclpy.Parameter.Type.INTEGER_ARRAY,
            mappings
        )
        updated_directions = rclpy.parameter.Parameter(
            'motor_directions',
            rclpy.Parameter.Type.INTEGER_ARRAY,
            directions
        )

        self.set_parameters([updated_mappings, updated_directions])

        self.get_logger().info('Motor mappings and directions updated')
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