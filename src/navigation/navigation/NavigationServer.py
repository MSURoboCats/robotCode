import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

# Import interface definitions
from interfaces.action import Navigate
from interfaces.msg import ThrusterCommand
from interfaces.msg import DepthInfoCommand

class NavigationServer(Node):
    def __init__(self):
        super().__init__("navigation_action_server")

        # Instantiate a new action server that targets the Navigate action
        self._action_server = ActionServer(
            self,
            Navigate,
            'navigate',
            self._navigate
        )
        self.create_subscription = self.create_subscription(
            DepthInfoCommand,
            "depthinfocommand",
            self._handle_pressure_sensor_message
        )
    def _handle_pressure_sensor_message(self):
        # This is where the (int64) input from the PressureSensorController node will be handled

        # TODO: Add context to log message
        self.get_logger().info("Processing DepthInfoCommand from PressureSensorController")
    
    def _navigate(self, goal):
        # This is the entrypoint for completing a navigation goal, and will facilitate the consumption of sensor data and the implementation of the navigation algorithm.
        # TODO: Implement navigation logic
        
        # TODO: Add context to logging messages
        self.get_logger().info("Begining navigation")

        # TODO: Handle success condition
        if(True):
            self.get_logger.info("Navigation goal succeeded")
            goal.succeed()

        # Modify result object to include navigation feedback (TODO: Define navigation feedback)
        result = Navigate.Result()
        result.current_state = Navigate.Feedback()

        # Return the current position (the result of the navigation action)
        return Navigate.Result()

    def _send_thruster_command(self):
        publisher = self.create_publisher(ThrusterCommand, "thruster")

        # TODO: define command
        command = 0

        # Publish command to 'thruster' topic
        publisher.publish(command)       

        # TODO: Add context to logging messages
        self.get_logger().info("Sending Thruster Command: ")

def main(args=None):
    # Initialize the node and consume any paramters
    rclpy.init(args=args)

    # Perform any configuration
    navigation_server = NavigationServer()

    # Release control of the node to the ROS network
    rclpy.spin(navigation_server)

if __name__ == "__main__":
    main()