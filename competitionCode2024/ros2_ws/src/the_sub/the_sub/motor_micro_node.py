import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
import rclpy.parameter

from interfaces.msg import MotorPowers, Mappings
from interfaces.srv import GetMappings

from sensor_msgs.msg import BatteryState
from std_msgs.msg import Int16

import the_sub.motor_micro_interface as motor_interface

import yaml
import os
import sys

class MotorMicroNode(Node):

    def __init__(self):
        super().__init__('motor_micro_node')

        # subscriber for controlling the motors
        self.set_motor_power = self.create_subscription(MotorPowers, 'motor_powers', self.motor_powers_callback, 10)

        # subscriber for testing an ESC
        self.test_esc = self.create_subscription(Int16, 'test_esc', self.test_esc_callback, 10)
        
        # service for getting motor mappings
        self.get_mappings = self.create_service(GetMappings, "get_mappings", self.get_mappings_callback)

        # subscriber for setting motor mappings
        self.set_mappings = self.create_subscription(Mappings, "set_mappings", self.set_mappings_callback, 10)

        # publisher for board voltage at 5 Hz (unless 'voltage_off' is passed when the node is run)
        self.pub_voltage = self.create_publisher(BatteryState, 'battery_health', 10)
        timer_period = .2
        try:
            if sys.argv[1] == 'voltage_off':
                self.get_logger().info("\n\nNode initialized in setup mode: open a new terminal, source the environment, and run the following command: ros2 run the_sub map_motors_node\n")
            else:
                self.time = self.create_timer(timer_period, self.pub_voltage_callback)
        except:
            pass


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

    def motor_powers_callback(self, motor_powers: list[float]) -> None:
        # send motor powers to the arduino
        self.motor_micro.run_motors([motor_powers.motor1,
                                     motor_powers.motor2,
                                     motor_powers.motor3,
                                     motor_powers.motor4,
                                     motor_powers.motor5,
                                     motor_powers.motor6,
                                     motor_powers.motor7,
                                     motor_powers.motor8])
        self.get_logger().info('Sending motor power values to microcontroller')

    def test_esc_callback(self, esc: Int16) -> None:
        # test ESC
        self.motor_micro.test_esc(esc.data)
    
    def get_mappings_callback(self, request, response: Mappings) -> Mappings:
        # get current mapping/direction values
        motor_mappings = self.get_parameter('motor_mappings').value
        directions = self.get_parameter('motor_directions').value

        # populate response
        response.mappings.motor1.esc = motor_mappings[0]
        response.mappings.motor1.direction = directions[0]
        response.mappings.motor2.esc = motor_mappings[1]
        response.mappings.motor2.direction = directions[1]
        response.mappings.motor3.esc = motor_mappings[2]
        response.mappings.motor3.direction = directions[2]
        response.mappings.motor4.esc = motor_mappings[3]
        response.mappings.motor4.direction = directions[3]
        response.mappings.motor5.esc = motor_mappings[4]
        response.mappings.motor5.direction = directions[4]
        response.mappings.motor6.esc = motor_mappings[5]
        response.mappings.motor6.direction = directions[5]
        response.mappings.motor7.esc = motor_mappings[6]
        response.mappings.motor7.direction = directions[6]
        response.mappings.motor8.esc = motor_mappings[7]
        response.mappings.motor8.direction = directions[7]

        return response

    def set_mappings_callback(self, motor_mappings: Mappings) -> None:
        mappings = [motor_mappings.motor1.esc,
                    motor_mappings.motor2.esc,
                    motor_mappings.motor3.esc,
                    motor_mappings.motor4.esc,
                    motor_mappings.motor5.esc,
                    motor_mappings.motor6.esc,
                    motor_mappings.motor7.esc,
                    motor_mappings.motor8.esc
                    ]
        directions = [motor_mappings.motor1.direction,
                      motor_mappings.motor2.direction,
                      motor_mappings.motor3.direction,
                      motor_mappings.motor4.direction,
                      motor_mappings.motor5.direction,
                      motor_mappings.motor6.direction,
                      motor_mappings.motor7.direction,
                      motor_mappings.motor8.direction,
                      ]
        
        # load new values to the arduino
        self.motor_micro.load_assignments(mappings, directions)
        
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

        # dump new parameters to /ros2_ws/src/the_sub/config/params.yaml
        yaml_path = os.path.join(os.getcwd(), 'src', 'the_sub', 'config', 'params.yaml')
        params = self.get_parameters(['motor_mappings', 'motor_directions'])
        params_dict = {'motor_micro_node': {'ros__parameters' : {param.name : param.value for param in params}}}
        all_params = {}
        with open(yaml_path, 'r') as file:
            all_params = yaml.load(file, Loader=yaml.FullLoader)
        all_params.update(params_dict)
        with open(yaml_path, 'w') as file:
            yaml.dump(all_params, file)

        self.get_logger().info('Motor mappings and directions updated and dumped')
    
    def pub_voltage_callback(self) -> None:
        # get and publish battery voltage
        cur_health = BatteryState()
        cur_health.voltage = self.motor_micro.get_voltage()
        self.pub_voltage.publish(cur_health)

        self.get_logger().info('Publishing voltage: %.2f' % cur_health.voltage)
        
def main(args=None):
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    arduino = MotorMicroNode()

    # spin the node so callback function is called
    rclpy.spin(arduino)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    arduino.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
    main()