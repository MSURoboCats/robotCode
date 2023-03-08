import rclpy
from rclpy.node import Node

# Import interface definitions
from interfaces.msg import DepthSensorOutput
from interfaces.msg import DepthInfoCommand

class PressureSensorController(Node):
    def __init__(self):
        super().__init__("pressure_sensor_controller")

        # Instantiate a new subscriber that is listening for thruster commands on the 'thruster' topic
        self.create_subscription = self.create_subscription(
            DepthSensorOutput,
            "depthsensoroutput",
            self._handle_message 
        )

    def _handle_message(self):
        # This is where the thruster command will be handled (i.e., converted into native instructionts that can be interpreted by the Blue Robotics T100 thrusters)
        # TODO: Implement thruster control logic

        # TODO: Add context to log message
        self.get_logger().info("Processing depth information from Depth Sensor")

    def _send_depth_info_command(self):
        publisher = self.create_publisher(DepthInfoCommand, "depthinfocommand")

        # TODO: define command
        command = 0

        # Publish command to 'thruster' topic
        publisher.publish(command)       

        # TODO: Add context to logging messages
        self.get_logger().info("Sending Depth Information Command to Navigation: ")

def main(args=None):
    # Initialize the node and consume any paramters
    rclpy.init(args=args)

    # Perform any configuration
    pressure_sensor_controller = PressureSensorController()

    # Release control of the node to the ROS network
    rclpy.spin(pressure_sensor_controller)

if __name__ == "__main__":
    main()