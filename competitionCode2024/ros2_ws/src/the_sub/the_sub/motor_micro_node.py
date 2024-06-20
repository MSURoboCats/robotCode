import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import rclpy.parameter
from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers

import the_sub.motor_micro_interface as motor_interface
from std_srvs.srv import Empty

import yaml
import os

class MotorMicroNode(Node):

    def __init__(self):
        super().__init__('motor_micro_node')

        # service for controlling the motors
        self.set_motor_power = self.create_service(MotorPowers, 'motor_powers', self.motor_powers_callback)
        
        # service for running through motor mapping UI
        self.set_mappings = self.create_service(Empty, "motor_mappings", self.motor_mappings_callback)

        # publisher for board voltage every second
        self.pub_voltage = self.create_publisher(BatteryState, 'battery_health', 10)
        timer_period = 1
        self.time = self.create_timer(timer_period, self.pub_voltage_callback)

        # intialize the microcontroller
        self.motor_micro = motor_interface.MotorArduino('/dev/ttyACM0')
        
        # parameter to hold the motor/ESC mappings
        motor_mappings_descriptor = ParameterDescriptor(description="Maps each motor to an ESC - see Notion Code Companion motor_micro_main.ino for mappings.")
        self.declare_parameter('motor_mappings', [1,2,3,4,5,6,7,8], motor_mappings_descriptor)

        # parameter to hold the motor directions
        motor_directions_descriptor = ParameterDescriptor(description="Determines whether each motor should be reversed or not (0 for normal, 1 for reversed)")
        self.declare_parameter('motor_directions', [0,0,0,0,0,0,0,0], motor_directions_descriptor)

        # update the sub with the current motor/ESC mappings and directions
        self.motor_micro.load_assignments(
            self.get_parameter('motor_mappings').get_parameter_value().integer_array_value,
            self.get_parameter('motor_directions').get_parameter_value().integer_array_value
        )

        self.get_logger().info('Motor microcontroller initialized')

    def motor_powers_callback(self, request, response):
        # send motor powers to the arduino
        self.motor_micro.run_motors([request.motor1,
                                     request.motor2,
                                     request.motor3,
                                     request.motor4,
                                     request.motor5,
                                     request.motor6,
                                     request.motor7,
                                     request.motor8])
        self.get_logger().debug('Sending motor power values to microcontroller')
        return response
    
    def motor_mappings_callback(self, request, response):
        # run UI to set mappings
        mappings, directions = self.motor_micro.set_assignments()

        # update parameters
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

        # dump new parameters
        yaml_path = os.path.join(os.getcwd(), 'src', 'the_sub', 'config', 'params.yaml')
        params = self.get_parameters(['motor_mappings', 'motor_directions'])
        params_dict = {'motor_micro_node': {'ros__parameters' : {param.name : param.value for param in params}}}
        all_params = {}
        with open(yaml_path, 'r') as file:
            all_params = yaml.load(file)
        all_params.update(params_dict)
        with open(yaml_path, 'w') as file:
            yaml.dump(all_params, file)

        self.get_logger().info('Motor mappings and directions updated and dumped')
        return response
    
    def pub_voltage_callback(self):
        # get and publish battery voltage
        cur_health = BatteryState()
        cur_health.voltage = self.motor_micro.get_voltage()
        self.pub_voltage.publish(cur_health)

        self.get_logger().debug('Publishing voltage: %.2f' % cur_health.voltage)

def main(args=None):
    rclpy.init(args=args)

    arduino = MotorMicroNode()

    rclpy.spin(arduino)

    rclpy.shutdown()

if __name__ == '__main__':
    main()