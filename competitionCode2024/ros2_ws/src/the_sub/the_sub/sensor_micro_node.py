import rclpy               
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import rclpy.parameter

from interfaces.srv import ControlData
from interfaces.msg import HullData

import the_sub.sensor_micro_interface as sensor_interface

class SensorMicroNode(Node):

    def __init__(self):
        super().__init__('sensor_micro_node')

        # service for getting control data
        self.get_control_data = self.create_service(ControlData, 'control_data', self.control_data_callback)
        
        # publisher for hull data every second
        self.pub_hull_data = self.create_publisher(HullData, 'hull_data', 10)
        timer_period = 1
        self.time = self.create_timer(timer_period, self.pub_hull_data_callback)

        # initialize microcontroller
        self.sensor_micro = sensor_interface.SensorArduino('/dev/ttyUSB0')

        self.get_logger().info('Sensor microcontroller initialized')

    def control_data_callback(self, request, response):
        # get control data and populate response
        data = self.sensor_micro.get_control_data()

        response.imu_data.orientation.x = data.get('orientation').get('x')
        response.imu_data.orientation.y = data.get('orientation').get('y')
        response.imu_data.orientation.y = data.get('orientation').get('z')
        response.imu_data.orientation.w = data.get('orientation').get('w')
        response.imu_data.angular_velocity.x = data.get('angular_velocity').get('x')
        response.imu_data.angular_velocity.y = data.get('angular_velocity').get('y')
        response.imu_data.angular_velocity.z = data.get('angular_velocity').get('z')
        response.imu_data.linear_acceleration.x = data.get('linear_acceleration').get('x')
        response.imu_data.linear_acceleration.y = data.get('linear_acceleration').get('y')
        response.imu_data.linear_acceleration.z = data.get('linear_acceleration').get('z')
        response.depth = data.get('depth')

        self.get_logger().info('Sending control data: depth %.2fm\n' % response.depth)

        return response
    
    def pub_hull_data_callback(self):
        # get and publish hull data
        data = self.sensor_micro.get_hull_data()

        cur_conditions = HullData()
        cur_conditions.temperature.temperature = data.get('temperature')
        cur_conditions.pressure.fluid_pressure = data.get('pressure')
        cur_conditions.humidity.relative_humidity = data.get('humidity')

        self.pub_hull_data.publish(cur_conditions)
        self.get_logger().debug('Hull data published: %.2fdegC | %.2fhPa | %.2f%%' % (cur_conditions.temperature.temperature,
                                                                                 cur_conditions.pressure.fluid_pressure,
                                                                                 cur_conditions.humidity.relative_humidity))

def main(args=None):
    rclpy.init(args=args)

    arduino = SensorMicroNode()

    rclpy.spin(arduino)

    rclpy.shutdown()

if __name__ == '__main__':
    main()