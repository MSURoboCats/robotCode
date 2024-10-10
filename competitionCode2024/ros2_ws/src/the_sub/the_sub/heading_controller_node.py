import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaces.msg import ControlData, HeadingGoal
from geometry_msgs.msg import Twist, Quaternion
from std_msgs.msg import String, Empty

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
        self.pub_goal_reached = self.create_publisher(
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

        # subscriber for activation
        self.sub_heading_control_activation = self.create_subscription(
            Empty,
            '/heading_controller_activation',
            self.heading_control_activation_callback,
            10,
        )

        # subscriber for deactivation
        self.sub_heading_control_deactivation = self.create_subscription(
            Empty,
            '/heading_controller_deactivation',
            self.heading_control_deactivation_callback,
            10,
        )

        self.goal_heading = np.quaternion(1,0,0,0)      # goal heading
        self.cur_heading = np.quaternion(1,0,0,0)       # current heading read from sensor
        self.cur_heading_der = np.quaternion(1,0,0,0)   # current derivative read from sensor
        
        
        self.active = False         # disable it
        self.initialized = False    # heading values not initialized
        self.goal_reached = True    # send success messages when goal_reached=False and cur_heading=goal_heading
        
        # PD controller values
        self.Kp = 2
        self.Kd = -.3

        # maximum rotation speed with mirrored non-constant for slower rotation commands
        self.MAX_POWER = .2
        self.cur_max_power = self.MAX_POWER
        
        # the minimum value of for the rotational velocity for
        # the reading to be discarded and control loop skipped
        self.ROT_VEL_SENSOR_ERROR = 6

        # number of samples to use in the rolling average of the sensor value
        self.ROLLING_AVE = 5

        # the minimum difference between the orientation sensor reading
        #  and the current orientation for the goal reached message to be published
        self.MIN_ERROR = .05

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
            self.get_logger().info('Initialized cur, prev, goal to %s' % data.imu_data.orientation)
        
        # only control heading if active
        if self.active:
            # skip iteration if the derivative value is unreasonable
            if data.imu_data.angular_velocity.z > self.ROT_VEL_SENSOR_ERROR:
                self.get_logger().debug('Unreasonable rot vel z: %.2f' % data.imu_data.angular_velocity.z)
                return
            
            # calculate rolling average for sensor values
            self.cur_heading = np.quaternion(
                    ((self.ROLLING_AVE - 1) * self.cur_heading.w + data.imu_data.orientation.w)/self.ROLLING_AVE,
                    ((self.ROLLING_AVE - 1) * self.cur_heading.x + data.imu_data.orientation.x)/self.ROLLING_AVE,
                    ((self.ROLLING_AVE - 1) * self.cur_heading.y + data.imu_data.orientation.y)/self.ROLLING_AVE,
                    ((self.ROLLING_AVE - 1) * self.cur_heading.z + data.imu_data.orientation.z)/self.ROLLING_AVE,
                )
            self.cur_heading_der = 1/2 * np.quaternion(
                    0,
                    ((self.ROLLING_AVE - 1) * self.cur_heading_der.x + data.imu_data.angular_velocity.x)/self.ROLLING_AVE,
                    ((self.ROLLING_AVE - 1) * self.cur_heading_der.y + data.imu_data.angular_velocity.y)/self.ROLLING_AVE,
                    ((self.ROLLING_AVE - 1) * self.cur_heading_der.z + data.imu_data.angular_velocity.z)/self.ROLLING_AVE,
                )
            
            # calculate error around the y-axis from quaternion orientation
            e = self.goal_heading * np.conjugate(self.cur_heading)
            e_y = e.y

            # get the derivative around the z-axis from gyroscope
            delta_z = self.cur_heading_der.z

            # PD controller with time step of .0625 / 16HZ (what control data is published at)
            power_out = self.Kp*e_y + self.Kd*delta_z / .0625

            # publish motor values
            rot_twist = Twist()
            rot_twist.angular.y = max(-self.cur_max_power, min(power_out, self.cur_max_power))
            self.pub_twist.publish(rot_twist)
            self.get_logger().debug('Cur: %.2f | Goal: %.2f | Const: %.2f | Der: %.2f | Motors: %.2f' % (self.cur_heading.y,
                                                                                                        self.goal_heading.y,
                                                                                                        self.Kp*e_y,
                                                                                                        self.Kd*delta_z / .0625,
                                                                                                        max(-self.cur_max_power, min(power_out, self.cur_max_power)),
                                                                                                        ))

            # check for goal reached condition
            if not self.goal_reached and abs(self.cur_heading.y - self.goal_heading.y) < self.MIN_ERROR:
                # only send message once and reset max power
                self.goal_reached = True    
                self.cur_max_power = self.MAX_POWER
                message = String()
                message.data = "Goal heading reached: %.2f" % self.cur_heading.y
                self.pub_goal_reached.publish(message)

    def heading_goal_callback(self, data: HeadingGoal) -> None:
        # set heading goal
        self.goal_heading = np.quaternion(
                data.orientation.w,
                data.orientation.x,
                data.orientation.y,
                data.orientation.z,
            )
        if data.max_power != 0:
            self.cur_max_power = data.max_power
        self.goal_reached = False
        self.get_logger().info('Goal heading set to %.2f %.2fi %.2fj %.2fk at %.2f%% max power' % (self.goal_heading.w,
                                                                               self.goal_heading.x,
                                                                               self.goal_heading.y,
                                                                               self.goal_heading.z,
                                                                               self.cur_max_power*100,
                                                                               ))
    def heading_control_activation_callback(self, data: Empty) -> None:
        self.active = True
        self.get_logger().info('Controller activated')       
    
    def heading_control_deactivation_callback(self, data: Empty) -> None:
        # kill motors and disable
        self.active = False
        rot_twist = Twist()
        rot_twist.angular.y = 0.0
        self.pub_twist.publish(rot_twist)
        self.get_logger().info('Controller deactivated')


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