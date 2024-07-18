import rclpy
from rclpy.node import Node

from interfaces.msg import ControlData, DepthGoal

from geometry_msgs.msg import Twist
from std_msgs.msg import String

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
        
        self.goal_depth = 0.0       # float
        self.cur_depth = 0.0        # rolling average of most recent samples
        self.prev_depth = 0.0       # rolling average one time step behind cur_depth

        self.initialized = False    # depth values not initialized
        self.goal_reached = True    # send success messages when goal_reached=False and cur_depth=goal_depth

        # PD controller values
        self.Kp = -6
        self.Kd = 4

        # the minimum difference between the sensor reading and the current depth for
        # the reading to be discarded and control loop skipped
        self.SENSOR_ERROR = .2

        # number of samples to use in the rolling average of the sensor value
        self.ROLLING_AVE = 5

        # the minimum difference between the sensor reading and the current depth for
        # the goal reached message to be published
        self.MIN_ERROR = .1
    
    def control_data_callback(self, data: ControlData) -> None:
        # if it is the first reading, intialize depth variables
        if not self.initialized:
            # don't initialize on a bad sensor reading
            if data.depth == 0:
                return
            self.cur_depth = data.depth
            self.prev_depth = data.depth
            self.goal_depth = data.depth
            self.initialized = True
            self.get_logger().info('Initialized cur, prev, goal depth to %.2fm' % data.depth)

        # if it is a bad sensor reading, skip the iteration
        if abs(data.depth - self.cur_depth) > self.SENSOR_ERROR:
            self.get_logger().warn('Unreasonable value | Current: %.2f | New: %.2f' % (self.cur_depth, data.depth))
            return
        
        # calculate error and derivative
        self.prev_depth = self.cur_depth
        self.cur_depth = (data.depth + (self.ROLLING_AVE-1)*self.cur_depth) / self.ROLLING_AVE
        e = self.goal_depth - self.cur_depth
        delta_depth = self.cur_depth - self.prev_depth

        # PD controller with time step of .0625 / 16HZ (what control data is published at)
        power_out = self.Kp*e + self.Kd*delta_depth / .0625

        # publish motor values
        depth_twist = Twist()
        depth_twist.linear.y = power_out
        self.pub_twist.publish(depth_twist)
        self.get_logger().info('Cur: %.2f | Goal: %.2f | Const: %.2f | Der: %.2f | Motors: %.2f' % (self.cur_depth,
                                                                                                    self.goal_depth,
                                                                                                    self.Kp*e,
                                                                                                    self.Kd*delta_depth / .0625,
                                                                                                    power_out))

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