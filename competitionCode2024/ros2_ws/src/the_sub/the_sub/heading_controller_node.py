import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaces.msg import ControlData, HeadingGoal
from geometry_msgs.msg import Twist, Quaternion
from std_msgs.msg import String

import numpy as np
import quaternion


class HeadingController(Node):
    def __init__(self):
        super().__init__('heading_controller_node')

        # publisher for twists to control the sub rotationally about the y-axis only
        self.pub_twist = self.create_publisher(
            Twist,
            '/control_y_rot_twist',
            10,
        )

        # publisher for when the goal is reached
        self.pub_powers = self.create_publisher(
            String,
            '/heading_goal_status',
            10,
        )

        # subscriber for control data
        self.sub_control_data = self.create_subscription(
            ControlData,
            '/control_data',
            self.control_data_callback,
            10,
        )

        # subscriber for heading goal command
        self.sub_heading_goal = self.create_subscription(
            HeadingGoal,
            '/heading_goal',
            self.heading_goal_callback,
            10,
        )

        self.goal_heading = np.quaternion(1,0,0,0)      # goal heading
        self.cur_heading = np.quaternion(1,0,0,0)       # current heading read from sensor
        self.cur_heading_der = np.quaternion(1,0,0,0)   # current derivative read from sensor
        self.initialized = False                        # heading values not initialized

        self.Kp = .5     # guess
        self.Kd = -.05     # guess


    def control_data_callback(self, data: ControlData) -> None:
        # if it is the first reading, intialize heading variables
        if not self.initialized:
            self.cur_heading = np.quaternion(
                data.imu_data.orientation.w,
                data.imu_data.orientation.x,
                data.imu_data.orientation.y,
                data.imu_data.orientation.z,
            )
            self.goal_heading = np.quaternion(
                data.imu_data.orientation.w,
                data.imu_data.orientation.x,
                data.imu_data.orientation.y,
                data.imu_data.orientation.z,
            )
            self.cur_heading_der = 1/2 * np.quaternion(
                0,
                data.imu_data.angular_velocity.x,
                data.imu_data.angular_velocity.y,
                data.imu_data.angular_velocity.z,
            )
            self.initialized = True
        
        # calculate rolling average for sensor values
        self.cur_heading = np.quaternion(
                (self.cur_heading.w*4 + data.imu_data.orientation.w)/5,
                (self.cur_heading.x*4 + data.imu_data.orientation.x)/5,
                (self.cur_heading.y*4 + data.imu_data.orientation.y)/5,
                (self.cur_heading.z*4 + data.imu_data.orientation.z)/5,
            )
        self.cur_heading_der = 1/2 * np.quaternion(
                0,
                (4* self.cur_heading_der.x + data.imu_data.angular_velocity.x)/5,
                (4* self.cur_heading_der.y + data.imu_data.angular_velocity.y)/5,
                (4* self.cur_heading_der.z + data.imu_data.angular_velocity.z)/5,
            )
        
        # calculate error around the y-axis
        e = self.goal_heading * np.conjugate(self.cur_heading)
        e_y = e.y

        # get the derivative around the y-axis
        delta_y = self.cur_heading_der.y

        # PD controller with time step of .0625 / 16HZ (what control data is published at)
        power_out = self.Kp*e_y + self.Kd*delta_y / .0625

        # publish motor values
        rot_twist = Twist()
        rot_twist.angular.y = power_out
        self.pub_twist.publish(rot_twist)

        self.get_logger().info('Current: %s | Goal: %s | Error: %s | Der: %s | Power: %.2f' % (self.cur_heading.y,
                                                                                               self.goal_heading.y,
                                                                                               e.y,
                                                                                               self.cur_heading_der.y,
                                                                                               power_out,
                                                                                               ))

    def heading_goal_callback(self, data: HeadingGoal) -> None:
        # set heading goal
        self.goal_heading = np.quaternion(
                data.orientation.w,
                data.orientation.x,
                data.orientation.y,
                data.orientation.z,
            )
        self.get_logger().info('Heading goal set to %.2f %.2fi %.2fj %.2fk' % (self.goal_heading.w,
                                                                               self.goal_heading.x,
                                                                               self.goal_heading.y,
                                                                               self.goal_heading.z,
                                                                               ))

def main(args = None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    node = HeadingController()

    # spin the node so the callback function is called
    rclpy.spin(node)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
  
    # shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
  main()