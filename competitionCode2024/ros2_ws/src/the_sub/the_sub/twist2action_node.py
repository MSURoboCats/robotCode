import rclpy               
from rclpy.node import Node

from geometry_msgs.msg import Twist

from interfaces.srv import UserTwistCommand, UserStringCommand, MotorPowers

class Twist2Action(Node):

    def __init__(self):
        super().__init__('twist2action')

        # create service to receive twist that should be translated to motor powers
        self.twist_command_srv = self.create_service(UserTwistCommand, 'twist_command', self.twist_command_callback)

        # create service to receive string that should be translated to motor powers
        self.string_command_srv = self.create_service(UserStringCommand, 'string_command', self.string_command_callback)

        # create client for motor powers
        self.motor_powers_cli = self.create_client(MotorPowers, 'motor_powers')
        while not self.motor_powers_cli.wait_for_service(timeout_sec=1):
            self.get_logger().info('service not available, waiting again...')
        self.motor_powers_req = MotorPowers.Request() 

        self.stop = [0.0]*8
        self.forward = [0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0]
        self.backward = [0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0]
        self.up = [0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
        self.down = [0.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0]
        self.left = [1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]
        self.right = [-1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        self.pos_rotate = [1, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 1.0]
        self.neg_rotate = [-1, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, -1.0]

    def twist_command_callback(self, request, response):
        # coordinate system looking at front: x to the right, y up, z out of the page
        if request.twist_command.linear.z == 1:
            self.set_motors([x*.12 for x in self.forward])
            self.get_logger().info('Going forward...')
        elif request.twist_command.linear.z == -1:
            self.set_motors([x*.12 for x in self.backward])
            self.get_logger().info('Going backward...')
        elif request.twist_command.linear.y == 1:
            self.set_motors([x*.12 for x in self.up])
            self.get_logger().info('Going up...')
        elif request.twist_command.linear.y == -1:
            self.set_motors([x*.12 for x in self.down])
            self.get_logger().info('Going down...')
        elif request.twist_command.linear.x == 1:
            self.set_motors([x*.12 for x in self.left])
            self.get_logger().info('Going left...')
        elif request.twist_command.linear.x == -1:
            self.set_motors([x*.12 for x in self.right])
            self.get_logger().info('Going right...')
        elif request.twist_command.angular.y == 1:
            self.set_motors([x*.12 for x in self.pos_rotate])
            self.get_logger().info('Rotating positvely...')
        elif request.twist_command.angular.y == -1:
            self.set_motors([x*.12 for x in self.neg_rotate])
            self.get_logger().info('Rotating negatively...')
        else:
            self.set_motors(self.stop)
            self.get_logger().info('Stopping...')

        return response
    
    def string_command_callback(self, request, response):
        # coordinate system looking at front: x to the right, y up, z out of the page
        if request.string_command == 'forward':
            self.set_motors([x*.12 for x in self.forward])
            self.get_logger().info('Going forward...')
        elif request.string_command == 'backward':
            self.set_motors([x*.12 for x in self.backward])
            self.get_logger().info('Going backward...')
        elif request.string_command == 'up':
            self.set_motors([x*.12 for x in self.up])
            self.get_logger().info('Going up...')
        elif request.string_command == 'down':
            self.set_motors([x*.12 for x in self.down])
            self.get_logger().info('Going down...')
        elif request.string_command == 'left':
            self.set_motors([x*.12 for x in self.left])
            self.get_logger().info('Going left...')
        elif request.string_command == 'right':
            self.set_motors([x*.12 for x in self.right])
            self.get_logger().info('Going right...')
        elif request.string_command == 'pos_rot':
            self.set_motors([x*.12 for x in self.pos_rotate])
            self.get_logger().info('Rotating positvely...')
        elif request.string_command == 'neg_rot':
            self.set_motors([x*.12 for x in self.neg_rotate])
            self.get_logger().info('Rotating negatively...')
        elif request.string_command == 'stop':
            self.set_motors(self.stop)
            self.get_logger().info('Stopping...')
        else:
            self.set_motors(self.stop)
            self.get_logger().info('Stopping...')

        return response

    def set_motors(self, values):
        self.motor_powers_req.motor1 = values[0]
        self.motor_powers_req.motor2 = values[1]
        self.motor_powers_req.motor3 = values[2]
        self.motor_powers_req.motor4 = values[3]
        self.motor_powers_req.motor5 = values[4]
        self.motor_powers_req.motor6 = values[5]
        self.motor_powers_req.motor7 = values[6]
        self.motor_powers_req.motor8 = values[7]

        self.motors_future = self.motor_powers_cli.call_async(self.motor_powers_req)

def main(args=None):
    rclpy.init(args=args)

    twister = Twist2Action()

    rclpy.spin(twister)

    rclpy.shutdown()

if __name__ == '__main__':
    main()