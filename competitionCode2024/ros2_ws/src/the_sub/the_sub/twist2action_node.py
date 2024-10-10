import rclpy               
from rclpy.node import Node

from interfaces.msg import MotorPowers

from geometry_msgs.msg import Twist

class Twist2Action(Node):

    def __init__(self):
        super().__init__('twist2action')

        # subscriber to receive twist to be translated to motor powers
        self.sub_twist_command = self.create_subscription(Twist, 'control_twist', self.twist_command_callback, 10)

        # subscriber to receive twist to be translated to motor powers for linear motion in along the y-axis
        # (depth control)
        self.sub_twist_command_y = self.create_subscription(Twist, 'control_y_twist', self.twist_y_command_callback, 10)

        # subscriber to receive twist to be translated to motor powers for rotation about the y axis
        self.sub_twist_command_y_rot = self.create_subscription(Twist, 'control_y_rot_twist', self.twist_y_rot_command_callback, 10)

        # subscriber to receive twist to be translated to motor powers for rotation about the y axis
        self.sub_twist_command_drive = self.create_subscription(Twist, 'control_drive_twist', self.twist_drive_command_callback, 10)

        # publisher for motor powers
        self.motor_powers_pub = self.create_publisher(MotorPowers, 'motor_powers', 10)

        # message to keep track of motor powers
        self.motor_powers = MotorPowers()

        # map standard commands to motor powers based on the motor configuration (see Notion for documentation)
        self.STOP = [0.0]*8
        self.ZAXIS = [0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0]
        self.YAXIS = [0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
        self.XAXIS = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        self.YAXIS_ROT = [1.0, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 1.0]

    def twist_command_callback(self, data: Twist) -> None:
        # translate twist to basic control (clamp to [-1, 1])
        # coordinate system looking out the front: x to the right, y up, z forward
        if data.linear.z != 0:
            self.set_motors([max(-1.0, min(x*data.linear.z, 1.0)) for x in self.ZAXIS])
            self.get_logger().info('Going forward or backward (z-axis)...')
        elif data.linear.y != 0:
            self.set_motors([max(-1.0, min(x*data.linear.y, 1.0)) for x in self.YAXIS])
            self.get_logger().info('Going up or down (y-axis)...')
        elif data.linear.x != 0:
            self.set_motors([max(-1.0, min(x*data.linear.x, 1.0)) for x in self.XAXIS])
            self.get_logger().info('Going left or right (x-axis)...')
        elif data.angular.y != 0:
            self.set_motors([max(-1.0, min(x*data.angular.y, 1.0)) for x in self.YAXIS_ROT])
            self.get_logger().info('Rotating around the y-axis...')
        else:
            self.set_motors(self.STOP)
            self.get_logger().info('Stopping...')

    def twist_y_command_callback(self, data: Twist) -> None:
        
        # clamp power to [-1,1]
        power = max(-1.0, min(data.linear.y, 1.0))

        # only updated motors that control depth
        self.motor_powers.motor2 = power
        self.motor_powers.motor3 = power
        self.motor_powers.motor6 = power
        self.motor_powers.motor7 = power

        # publish motor values
        self.motor_powers_pub.publish(self.motor_powers)
        self.get_logger().info("Depth powers updated")

    def twist_y_rot_command_callback(self, data: Twist) -> None:

        # clamp power to [-1,1]
        power = max(-1.0, min(data.angular.y, 1.0))

        # only updated motors that control rotation not on forward motors
        self.motor_powers.motor1 = power
        #self.motor_powers.motor4 = power
        #self.motor_powers.motor5 = -power
        self.motor_powers.motor8 = power

        # publish motor values
        self.motor_powers_pub.publish(self.motor_powers)
        self.get_logger().info("Rotation powers updated")
    
    def twist_drive_command_callback(self, data: Twist) -> None:

        # clamp power to [-1,1]
        power = max(-1.0, min(data.linear.z, 1.0))

        # only updated motors that control forward motion, accounting for power differences
        if power > 0:
            self.motor_powers.motor4 = -power
            self.motor_powers.motor5 = -power*.85
        else:
            self.motor_powers.motor4 = -power*.85
            self.motor_powers.motor5 = -power

        # publish motor values
        self.motor_powers_pub.publish(self.motor_powers)
        self.get_logger().info("Drive powers updated")

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