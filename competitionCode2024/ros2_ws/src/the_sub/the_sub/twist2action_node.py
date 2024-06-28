import rclpy               
from rclpy.node import Node

from interfaces.msg import MotorPowers

from geometry_msgs.msg import Twist

class Twist2Action(Node):

    def __init__(self):
        super().__init__('twist2action')

        # subscriber to receive twist to be translated to motor powers
        self.twist_command_srv = self.create_subscription(Twist, 'control_twist', self.twist_command_callback, 10)

        # subscriber to receive twist to be translated to motor powers for linear motion in along the y-axis
        # (depth control)
        self.twist_command_srv = self.create_subscription(Twist, 'control_y_twist', self.twist_y_command_callback, 10)

        # publisher for motor powers
        self.motor_powers_pub = self.create_publisher(MotorPowers, 'motor_powers', 10)

        # message to keep track of motor powers
        self.motor_powers = MotorPowers()

        # map standard commands to motor powers based on the motor configuration (see Notion for documentation)
        self.STOP = [0.0]*8
        self.FORWARD = [0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0]
        self.BACKWARD = [0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0]
        self.UP = [0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
        self.DOWN = [0.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0]
        self.left = [1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]
        self.RIGHT = [-1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        self.POS_ROTATE = [1, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 1.0]
        self.NEG_ROTATE = [-1, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, -1.0]

    def twist_command_callback(self, data: Twist) -> None:
        # translate twist to basic control
        # coordinate system looking at front: x to the right, y up, z out of the page
        if data.linear.z == 1:
            self.set_motors([x*.12 for x in self.FORWARD])
            self.get_logger().info('Going forward...')
        elif data.linear.z == -1:
            self.set_motors([x*.12 for x in self.BACKWARD])
            self.get_logger().info('Going backward...')
        elif data.linear.y == 1:
            self.set_motors([x*.12 for x in self.UP])
            self.get_logger().info('Going up...')
        elif data.linear.y == -1:
            self.set_motors([x*.12 for x in self.DOWN])
            self.get_logger().info('Going down...')
        elif data.linear.x == 1:
            self.set_motors([x*.12 for x in self.left])
            self.get_logger().info('Going left...')
        elif data.linear.x == -1:
            self.set_motors([x*.12 for x in self.RIGHT])
            self.get_logger().info('Going right...')
        elif data.angular.y == 1:
            self.set_motors([x*.12 for x in self.POS_ROTATE])
            self.get_logger().info('Rotating positvely...')
        elif data.angular.y == -1:
            self.set_motors([x*.12 for x in self.NEG_ROTATE])
            self.get_logger().info('Rotating negatively...')
        else:
            self.set_motors(self.STOP)
            self.get_logger().info('Stopping...')

    def twist_y_command_callback(self, data: Twist) -> None:
        
        # clamp power to [-1,1]
        power = max(-1, min(data.linear.y, 1))

        # only updated motors that control depth
        self.motor_powers.motor2 = power
        self.motor_powers.motor3 = power
        self.motor_powers.motor6 = power
        self.motor_powers.motor7 = power

        # publish motor values
        self.motor_powers_pub.publish(self.motor_powers)
        self.get_logger().info("Depth goal powers updated")

    def set_motors(self, values: MotorPowers) -> None:
        # populate and publish motor powers
        self.motor_powers.motor1 = values[0]
        self.motor_powers.motor2 = values[1]
        self.motor_powers.motor3 = values[2]
        self.motor_powers.motor4 = values[3]
        self.motor_powers.motor5 = values[4]
        self.motor_powers.motor6 = values[5]
        self.motor_powers.motor7 = values[6]
        self.motor_powers.motor8 = values[7]

        self.motor_powers_pub.publish(self.motor_powers)

def main(args=None):
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    twister = Twist2Action()

    # spin the node so callback function is called
    rclpy.spin(twister)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    twister.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
    main()