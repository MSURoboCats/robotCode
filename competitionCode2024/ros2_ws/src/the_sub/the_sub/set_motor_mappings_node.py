import rclpy               
from rclpy.node import Node

from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers, ControlData
from std_srvs.srv import Empty

import time

class TotalTester(Node):

    def __init__(self):
        super().__init__('tester')
        
        self.motor_mappings_cli = self.create_client(Empty, 'motor_mappings')       # CHANGE
        while not self.motor_mappings_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.motor_mappings_req = Empty.Request()

    def set_motor_mappings(self):
        self.mappings_future = self.motor_mappings_cli.call_async(self.motor_mappings_req)

def main(args=None):
    rclpy.init(args=args)

    tester = TotalTester()

    tester.set_motor_mappings()

    while rclpy.ok():
        rclpy.spin_once(tester)
        if tester.mappings_future.done():
            try:
                response = tester.motors_future.result()
            except Exception as e:
                tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                tester.get_logger().info(
                    'Motor mappings set successfully')  # CHANGE
            break

    tester.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()