import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from sshkeyboard import listen_keyboard

class KeyboardController(Node):

    def __init__(self):
        super().__init__("KeyboardController")

        # publisher for twists to control the sub
        self.pub_twist = self.create_publisher(Twist, "control_twist", 10)

        # keep track of the twist
        self.keyboard_twist = Twist()

        # reset motor powers to 0.0
        self.pub_twist.publish(self.keyboard_twist)

        # scaler to adjust motor power
        self.power_scaler = .1

    def press(self, key) -> None:
        '''
        Handle keystrokes for control
        '''
        # calculate movement vectors:
        # (coordinate system looking out the front: x to the right, y up, z forward)
            #   l/r arrows for x (left/right)
            #   up/down arrows for z (forward/backward)
            #   w/s keys for y (up/down)
            #   a/d keys for rotation about y (rotate left/right)
        # update max power
            #   1-10 for .1 to 1 motor power
        # anything else to stop
        if key == 'up':
            self.keyboard_twist.linear.z = 1 * self.power_scaler
        elif key == 'down':
            self.keyboard_twist.linear.z = -1 * self.power_scaler
        elif key == 'left':
            self.keyboard_twist.linear.x = -1 * self.power_scaler
        elif key == 'right':
            self.keyboard_twist.linear.x = 1 * self.power_scaler
        elif key == 'w':
            self.keyboard_twist.linear.y = 1 * self.power_scaler
        elif key == 's':
            self.keyboard_twist.linear.y = -1 * self.power_scaler
        elif key == 'a':
            self.keyboard_twist.angular.y = 1 * self.power_scaler
        elif key == 'd':
            self.keyboard_twist.angular.y = -1 * self.power_scaler
        elif key in [str(num) for num in range(1, 11)]:
            self.power_scaler = float(key) / 10.0
            self.get_logger().info("Power updated to %.1f" % self.power_scaler)
            return
        else:
            self.keyboard_twist = Twist()

        self.pub_twist.publish(self.keyboard_twist)
        #self.get_logger().info('Non-zero twist published')

    def release(self, key) -> None:
        '''
        Handle keyreleases, publishing a twist with all zeros
        '''
        self.keyboard_twist = Twist()
        self.pub_twist.publish(self.keyboard_twist)
        #self.get_logger().info('Reset twist published')

    def listen(self) -> None:
        '''
        Listen for keystrokes
        '''
        self.get_logger().info("Keyboard control intitiated...")
        print("Arrow keys for forard/backwad/left/right\nw/s/a/d for up/down/rotate left/rotate right\n1-10 to adjust power\nEscape to exit")
        listen_keyboard(on_press=self.press, on_release=self.release)
        self.get_logger().info("Motors killed and keyboard control relinquished!")
        self.keyboard_twist = Twist()
        self.pub_twist.publish(self.keyboard_twist)

def main(args = None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    node = KeyboardController()

    # listen for keystrokes
    node.listen()

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
  
    # shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
  main()