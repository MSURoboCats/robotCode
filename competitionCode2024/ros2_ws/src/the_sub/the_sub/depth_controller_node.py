import rclpy
from rclpy.node import Node

from interfaces.msg import ControlData, DepthGoal

from geometry_msgs.msg import Twist

class DepthController(Node):

    def __init__(self):
        super().__init__('depth_controller_node')

        # publisher for twists to control the sub linearly along the y-axis only
        self.pub_twist = self.create_publisher(Twist, "control_y_twist", 10)

        # subscriber for control data
        self.sub_control_data = self.create_subscription(
            ControlData, 
            'control_data', 
            self.control_data_callback, 
            10)
        
        # subscriber for depth setting command
        self.sub_depth_goal = self.create_subscription(
            DepthGoal, 
            'depth_goal', 
            self.depth_goal_callback, 
            10)
        
        self.goal_depth = 0.0       # float
        self.cur_depth = 0.0        # rolling average of most recent 5 samples
        self.prev_depth = 0.0       # rolling average one time step behind cur_depth
        self.initialized = False    # depth values not initialized

        self.Kp = 1.5  # full motor power if more than 3m away from goal 
        self.Kd = -.5        # complete guess
    
    def control_data_callback(self, data: ControlData) -> None:
        # if it is the first reading, intialize depth variables
        if not self.initialized:
            if data.depth == 0:
                return
            self.cur_depth = data.depth
            self.prev_depth = data.depth
            self.goal_depth = data.depth
            self.initialized = True

        # if it is a bad sensor reading, skip the iteration
        if abs(data.depth - self.cur_depth) > .2:
            print(data.depth, self.cur_depth, abs(data.depth - self.cur_depth))
            return
        
        # calculate error and derivative
        self.prev_depth = self.cur_depth
        self.cur_depth = (data.depth + 4*self.cur_depth) / 5
        e = self.goal_depth - self.cur_depth
        delta_depth = self.cur_depth - self.prev_depth

        # PD controller with time step of .0625 / 16HZ (what control data is published at)
        power_out = self.Kp*e + self.Kd*delta_depth / .0625

        # publish motor values
        depth_twist = Twist()
        depth_twist.linear.y = power_out
        self.pub_twist.publish(depth_twist)
        self.get_logger().info('Current: %.2f | Goal: %.2f | Motors: %.2f' % (self.cur_depth, self.goal_depth, power_out))

    def depth_goal_callback(self, data: DepthGoal) -> None:
        self.goal_depth = data.depth
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