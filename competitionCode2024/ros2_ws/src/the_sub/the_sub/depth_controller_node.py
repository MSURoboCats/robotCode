import rclpy
from rclpy.node import Node

from interfaces.msg import ControlData, DepthGoal

from geometry_msgs.msg import Twist
from std_msgs.msg import String, Empty

class DepthController(Node):

    def __init__(self):
        super().__init__('depth_controller_node')

        # publisher for twists to control the sub linearly along the y-axis only
        self.pub_twist = self.create_publisher(
            Twist,
            "/control_y_twist",
            10,
        )

        # publisher for when the goal is reached
        self.pub_goal_reached = self.create_publisher(
            String,
            '/depth_goal_status',
            10,
        )

        # subscriber for control data
        self.sub_control_data = self.create_subscription(
            ControlData, 
            '/control_data', 
            self.control_data_callback, 
            10)
        
        # subscriber for depth goal command
        self.sub_depth_goal = self.create_subscription(
            DepthGoal, 
            '/depth_goal', 
            self.depth_goal_callback, 
            10)
        
        # subscriber for activation
        self.sub_depth_control_activation = self.create_subscription(
            Empty,
            '/depth_controller_activation',
            self.depth_control_activation_callback,
            10,
        )

        # subscriber for deactivation
        self.sub_depth_control_deactivation = self.create_subscription(
            Empty,
            '/depth_controller_deactivation',
            self.depth_control_deactivation_callback,
            10,
        )
        
        # PID controller constant values
        self.Ki = 0
        self.Kp = -6
        self.Kd = 4

        # sampling time
        self.T = 1/16

        # high frequency noise rejection
        self.TAU = .25*self.T

        # clamp output
        self.OUTMAX = 1.0
        self.OUTMIN = -1.0

        # number of samples to use in the rolling average of the sensor value
        self.ROLLING_AVE = 5

        # rolling average of most recent samples
        self.cur_depth = 0.0

        # int/der memeory
        self.integrator = 0
        self.differentiator = 0

        # previous data
        self.prev_depth = 0

        # goal depth
        self.set_pt = 0

        # active/deactive status
        self.status = False

        # the minimum difference between the sensor reading and the current depth for
        # the reading to be discarded and control loop skipped
        self.SENSOR_ERROR = .2

        # number of samples to use in the rolling average of the sensor value
        self.ROLLING_AVE = 5

        # the minimum difference between the sensor reading and the current depth for
        # the goal reached message to be published
        self.MIN_ERROR = .1

        self.initialized = False    # depth values not initialized
        self.goal_reached = True    # send success messages when goal_reached=False and cur_depth=goal_depth
        
    
    def control_data_callback(self, data: ControlData) -> None:
        if self.active:
            
            # if it is the first reading, intialize depth variables
            if not self.initialized:
                self.cur_depth = 0.0
                self.prev_depth = 0.0
                self.initialized = True
                self.get_logger().info('Initialized cur, prev depth to %.2fm | Goal is %.2f' % (0.0, self.goal_depth))

            # if it is a bad sensor reading, skip the iteration
            if abs(data.depth - self.cur_depth) > self.SENSOR_ERROR:
                self.get_logger().debug('Unreasonable value | Current: %.2f | New: %.2f' % (self.cur_depth, data.depth))
                return

            # rolling average to smooth out data
            self.cur_depth = (data.depth + (self.ROLLING_AVE-1)*self.cur_depth) / self.ROLLING_AVE

            error = self.set_pt - self.cur_depth

            # proportional term
            proportional = self.Kp*error

            # integral term
            self.integrator = self.integrator + self.Ki*self.T*error

            # dynamic integrator clamping limits
             if self.OUTMAX > proportional:
               integrator_max = self.OUTMAX - proportional
            else:
                integrator_max = 0

            if self.OUTMIN < proportional :
                integrator_min = self.OUTMIN - proportional
            else:
                integrator_min = 0

            # clamping integrator
            if self.integrator > integrator_max :
                self.integrator = integrator_max
            elif self.integrator < integrator_min:
                self.integrator = integrator_min

            # derivative term
            self.differentiator = (2 * self.Kd * (self.cur_depth - self.prev_depth) + (2 * self.TAU - self.T) * self.differentiator) / (2 * self.TAU + self.T)

            # calculate and clamp output
            power = proportional + self.integrator + self.differentiator

            if power > self.OUTMAX:
               power = self.OUTMAX
            elif power < self.OUTMIN:
               power = self.OUTMIN

            # store current data point for next update
            self.prev_depth = self.cur_depth

            # publish motor values
            depth_twist = Twist()
            depth_twist.linear.y = power
            self.pub_twist.publish(depth_twist)
            self.get_logger().debug('Cur: %.2f | Goal: %.2f | Const: %.2f | Der: %.2f | Int: %.2f | Motors: %.2f' % (self.cur_depth,
                                                                                                        self.set_pt,
                                                                                                        proportional,
                                                                                                        self.differentiator,
                                                                                                        self.integrator,
                                                                                                        power))

            # check for goal reached condition
            if not self.goal_reached and abs(self.cur_depth - self.goal_depth) < self.MIN_ERROR:
                self.goal_reached = True
                message = String()
                message.data = "Goal depth reached: %.2f" % self.cur_depth
                self.pub_goal_reached.publish(message)

    def depth_goal_callback(self, data: DepthGoal) -> None:
        # set depth goal
        self.goal_depth = data.depth
        self.goal_reached = False
        self.get_logger().info('Depth goal set to %.2f' % self.goal_depth)
    
    def depth_control_activation_callback(self, data: Empty) -> None:
        self.active = True
        self.get_logger().info('Controller activated')
    
    def depth_control_deactivation_callback(self, data: Empty) -> None:
        # kill motors and deactivate
        depth_twist = Twist()
        depth_twist.linear.y = 0.0
        self.pub_twist.publish(depth_twist)
        self.active = False
        self.get_logger().info('Controller deactivated')

def main(args = None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    node = DepthController()

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