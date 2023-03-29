import rclpy
from rclpy.node import Node

# Import interface definitions
from interfaces.msg import ImuOutput
from interfaces.msg import ImuRawData

class ImuController(Node): #create ImuController class from node class
    def __init__(self):     #create instance of ImuController class
        super().__init__("Imu_controller")   #inherit attributes from parent class

        # Instantiate a new subscriber that is listening for imu outputs on the 'Imu_raw_data' topic
        self.create_subscription = self.create_subscription(
            ImuRawData,
            "Imu_raw_data",
            self._handle_message 
        )

    def _handle_message(self):
        # This is where the raw data will be processed
        # TODO: initial data processing
        # TODO: Add context to log message
        self.get_logger().info("Processing information from IMU")


        #instantiate new publisher that publishes processed data to "Imu_output" topic
    def _send_imu_info(self):
        publisher = self.create_publisher(ImuOutput, "Imu_output")
        # TODO: format data and assign it to the ProcessedData variable
        ProcessedData = 0

        # Publish command to 'Imu_output' topic
        publisher.publish(ProcessedData)       

        # TODO: Add context to logging message
        self.get_logger().info("Sending IMU information to Navigation Node")


def main(args=None):
    # Initialize the node and consume any paramters
    rclpy.init(args=args)

    # Perform any configuration
    Imu_controller = ImuController()

    # Release control of the node to the ROS network
    rclpy.spin(Imu_controller)

if __name__ == "__main__":
    main()
    