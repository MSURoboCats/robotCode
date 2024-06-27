import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
import rclpy.parameter

from interfaces.msg import ControlData, HullData

import the_sub.sensor_micro_interface as sensor_interface

class SensorMicroNode(Node):

    def __init__(self):
        super().__init__('sensor_micro_node')

        # publisher for control data
        self.pub_control_data = self.create_publisher(ControlData, 'control_data', 10) 

        # publisher for hull data
        self.pub_hull_data = self.create_publisher(HullData, 'hull_data', 10)

        # callback for publishing at 5 Hz
        period = .2
        self.time = self.create_timer(period, self.publish_all_data)

        # initialize microcontroller
        self.sensor_micro = sensor_interface.SensorArduino('/dev/ttyUSB0')
        self.get_logger().info('Sensor microcontroller initialized')

    def publish_all_data(self) -> None:
        # get control data
        data = self.sensor_micro.get_control_data()
        
        # populate message
        cur_data = ControlData()
        cur_data.imu_data.orientation.x = data.get('orientation').get('x')
        cur_data.imu_data.orientation.y = data.get('orientation').get('y')
        cur_data.imu_data.orientation.y = data.get('orientation').get('z')
        cur_data.imu_data.orientation.w = data.get('orientation').get('w')
        cur_data.imu_data.angular_velocity.x = data.get('angular_velocity').get('x')
        cur_data.imu_data.angular_velocity.y = data.get('angular_velocity').get('y')
        cur_data.imu_data.angular_velocity.z = data.get('angular_velocity').get('z')
        cur_data.imu_data.linear_acceleration.x = data.get('linear_acceleration').get('x')
        cur_data.imu_data.linear_acceleration.y = data.get('linear_acceleration').get('y')
        cur_data.imu_data.linear_acceleration.z = data.get('linear_acceleration').get('z')
        cur_data.depth = data.get('depth')

        # publish message
        self.pub_control_data.publish(cur_data)
        self.get_logger().info('Control data published')
        
        # get hull data 
        data = self.sensor_micro.get_hull_data()

        # populate message
        cur_conditions = HullData()
        cur_conditions.temperature.temperature = float(data.get('temperature'))
        cur_conditions.pressure.fluid_pressure = float(data.get('pressure'))
        cur_conditions.humidity.relative_humidity = float(data.get('humidity'))

        # publish message
        self.pub_hull_data.publish(cur_conditions)
        self.get_logger().info('Hull data published')
        
        
def main(args=None):
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    arduino = SensorMicroNode()

    # spin the node so callback function is called
    rclpy.spin(arduino)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    arduino.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
    main()