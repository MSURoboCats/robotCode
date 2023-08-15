import rclpy
from rclpy.node import Node

# Import interface definitions (definitly not copying code rn)
from interfaces.msg import cameraData

class CameraController(Node):
    def __init__(self):
        super().__init__("camera_controller")

        # This is a copy of a comment
        self.create_publisher = self.create_publisher(
            cameraData,
            "camera",
            self._handle_message
        )
    
    def _handle_message(self):
        
        # This is a copy of a comment
        # This is also a copy of a comment

        # Another one lol
        self.get_logger().info("Activating camera")

def main(args=None):
    # Copy
    rclpy.init(args=args)

    # Copy
    camera_controller = CameraController()

    # Copy
    rclpy.spin(camera_controller)

if __name__ == "__main__":
    main()
