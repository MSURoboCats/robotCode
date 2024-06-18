import rclpy               
from rclpy.node import Node

from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers

import time

class TestMotorMicroNode(Node):

    def __init__(self):
        super().__init__('motor_tester')
        self.cli = self.create_client(MotorPowers, 'motor_powers')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = MotorPowers.Request()                                  # CHANGE

    def send_request(self, values):
        self.req.motor1 = values[0]
        self.req.motor1 = values[1]
        self.req.motor1 = values[2]
        self.req.motor1 = values[3]
        self.req.motor1 = values[4]
        self.req.motor1 = values[5]
        self.req.motor1 = values[6]
        self.req.motor1 = values[7]

        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    motor_tester = TestMotorMicroNode()
    motor_tester.send_request([.1]*8)

    while rclpy.ok():
        rclpy.spin_once(motor_tester)
        if motor_tester.future.done():
            try:
                response = motor_tester.future.result()
            except Exception as e:
                motor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                motor_tester.get_logger().info(
                    'motor values set to .1')  # CHANGE
            break
    
    time.sleep(2)

    motor_tester.send_request([0.0]*8)

    while rclpy.ok():
        rclpy.spin_once(motor_tester)
        if motor_tester.future.done():
            try:
                response = motor_tester.future.result()
            except Exception as e:
                motor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                motor_tester.get_logger().info(
                    'motor values set to 0')  # CHANGE
            break

    motor_tester.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()