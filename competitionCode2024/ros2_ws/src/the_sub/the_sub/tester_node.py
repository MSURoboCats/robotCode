import rclpy               
from rclpy.node import Node

from sensor_msgs.msg import BatteryState

from interfaces.srv import MotorPowers, ControlData
from std_srvs.srv import Empty

import time

class TotalTester(Node):

    def __init__(self):
        super().__init__('tester')

        self.motor_cli = self.create_client(MotorPowers, 'motor_powers')       # CHANGE
        while not self.motor_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.motor_req = MotorPowers.Request() 
        
        self.motor_mappings_cli = self.create_client(Empty, 'motor_mappings')       # CHANGE
        while not self.motor_mappings_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.motor_mappings_req = Empty.Request()

        self.sensor_cli = self.create_client(ControlData, 'control_data')       # CHANGE
        while not self.sensor_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.sensor_req = ControlData.Request()

    def set_motors(self, values):
        self.motor_req.motor1 = values[0]
        self.motor_req.motor1 = values[1]
        self.motor_req.motor1 = values[2]
        self.motor_req.motor1 = values[3]
        self.motor_req.motor1 = values[4]
        self.motor_req.motor1 = values[5]
        self.motor_req.motor1 = values[6]
        self.motor_req.motor1 = values[7]

        self.motors_future = self.motor_cli.call_async(self.motor_req)

    def set_motor_mappings(self):
        self.mappings_future = self.motor_mappings_cli.call_async(self.motor_mappings_req)

    def get_control_data(self):
        self.control_future = self.sensor_cli.call_async(self.sensor_req)


def main(args=None):
    rclpy.init(args=args)

    motor_tester = TotalTester()
    motor_tester.set_motors([.1]*8)

    while rclpy.ok():
        rclpy.spin_once(motor_tester)
        if motor_tester.motors_future.done():
            try:
                response = motor_tester.motors_future.result()
            except Exception as e:
                motor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                motor_tester.get_logger().info(
                    'motor values set to .1')  # CHANGE
            break
    
    time.sleep(2)

    motor_tester.set_motors([0.0]*8)

    while rclpy.ok():
        rclpy.spin_once(motor_tester)
        if motor_tester.motors_future.done():
            try:
                response = motor_tester.motors_future.result()
            except Exception as e:
                motor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                motor_tester.get_logger().info(
                    'motor values set to 0')  # CHANGE
            break

    motor_tester.set_motor_mappings()

    while rclpy.ok():
        rclpy.spin_once(motor_tester)
        if motor_tester.motors_future.done():
            try:
                response = motor_tester.motors_future.result()
            except Exception as e:
                motor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                motor_tester.get_logger().info(
                    'motors have been mapped')  # CHANGE
            break

    motor_tester.destroy_node()

    sensor_tester = TotalTester()
    sensor_tester.get_control_data()

    while rclpy.ok():
        rclpy.spin_once(sensor_tester)
        if sensor_tester.control_future.done():
            try:
                response = sensor_tester.control_future.result()
            except Exception as e:
                sensor_tester.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                sensor_tester.get_logger().info(
                    'Control data received: lin_acc_x %.2f' % response.imu_data.linear_acceleration.x)  # CHANGE
            break
    
    sensor_tester.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()