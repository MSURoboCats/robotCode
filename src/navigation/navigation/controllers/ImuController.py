import rclpy
from rclpy.node import Node

# Import interface definitions
from interfaces.msg import ThrusterCommand

class ThrusterController(Node):
    def __init__(self):
        super().__init__("thruster_controller")

        # Instantiate a new subscriber that is listening for thruster commands on the 'thruster' topic
        self.create_subscription = self.create_subscription(
            ThrusterCommand,
            "thruster",
            self._handle_message 
        )
    
    def _handle_message(self):
        # This is where the thruster command will be handled (i.e., converted into native instructionts that can be interpreted by the Blue Robotics T100 thrusters)
        # TODO: Implement thruster control logic

        # TODO: Add context to log message
        self.get_logger().info("Actating thruster")

def main(args=None):
    # Consume parameters
    rclpy.init(args=args)

    # Initalize thruster controller
    thruster_contoller = ThrusterController()

    # Release control of node to ROS2
    rclpy.spin(thruster_contoller)

if __name__ == "__main__":
    main()