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

        # callback for publishing at 16 Hz
        period = .0625
        self.time = self.create_timer(period, self.publish_all_data)

        # initialize microcontroller
        self.sensor_micro = sensor_interface.SensorArduino('/dev/ttyUSB0')
        self.get_logger().info('Initial data reads complete...getting surface offset')
        self.OFFSET = self.sensor_micro.get_external_pressure_offsest()
        self.get_logger().info('Sensor microcontroller initialized')

    def publish_all_data(self) -> None:
        # get control data
        #data = self.sensor_micro.get_control_data()
        data = self.sensor_micro.get_data()

        # populate control message
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
        cur_data.depth = (data.get('external_pressure') - self.OFFSET)*100 / (9.80665 * 997.0474) # subtract off surface offset and use P = rho * g * h

        # publish control message
        self.pub_control_data.publish(cur_data)
        self.get_logger().info('Control data published')
        
        # populate hull message
        cur_conditions = HullData()
        cur_conditions.temperature.temperature = data.get('temperature')
        cur_conditions.pressure.fluid_pressure = data.get('hull_pressure')
        cur_conditions.humidity.relative_humidity = data.get('humidity')
        

        # publish hull message
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