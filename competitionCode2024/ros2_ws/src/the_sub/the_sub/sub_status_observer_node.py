import rclpy               
from rclpy.node import Node

from interfaces.msg import ControlData, HullData, MotorPowers

from sensor_msgs.msg import BatteryState

import os

class StatusObserver(Node):

    def __init__(self):
        super().__init__('esc_tester_node')

        # subscriber for voltage
        self.voltage = self.create_subscription(
            BatteryState,
            "battery_health",
            self.voltage_callback,
            10,
        )
        self.volt = 0.0

        # subscriber for hull data
        self.hull = self.create_subscription(
            HullData,
            "hull_data",
            self.hull_callback,
            10,
        )
        self.temp = 0.0
        self.pressure = 0.0
        self.humidity = 0.0

        # subscriber for control data
        self.control = self.create_subscription(
            ControlData,
            "control_data",
            self.control_callback,
            10,
        )
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0
        self.wx  = 0.0
        self.wy = 0.0
        self.wz = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0
        self.depth = 0.0

        # subscriber for motor data
        self.motor = self.create_subscription(
            MotorPowers,
            "motor_powers",
            self.motor_callback,
            10,
        )
        self.motor1 = 0.0
        self.motor2 = 0.0
        self.motor3 = 0.0
        self.motor4 = 0.0
        self.motor5 = 0.0
        self.motor6 = 0.0
        self.motor7 = 0.0
        self.motor8 = 0.0

    def voltage_callback(self, data: BatteryState) -> None:
        self.volt = data.voltage
        
        self.print_sub()
    
    def hull_callback(self, data: HullData) -> None:
        self.temp = data.temperature.temperature
        self.pressure = data.pressure.fluid_pressure
        self.humidity = data.humidity.relative_humidity
        
        self.print_sub()
    
    def control_callback(self, data: ControlData) -> None:
        self.x = data.imu_data.orientation.x
        self.y = data.imu_data.orientation.y
        self.z = data.imu_data.orientation.z
        self.w = data.imu_data.orientation.w
        self.wx = data.imu_data.angular_velocity.x
        self.wy = data.imu_data.angular_velocity.y
        self.wz = data.imu_data.angular_velocity.z
        self.ax = data.imu_data.linear_acceleration.x
        self.ay = data.imu_data.linear_acceleration.y
        self.az = data.imu_data.linear_acceleration.z
        
        self.print_sub()
    
    def motor_callback(self, data: MotorPowers) -> None:
        self.motor1 = data.motor1
        self.motor2 = data.motor2
        self.motor3 = data.motor3
        self.motor4 = data.motor4
        self.motor5 = data.motor5
        self.motor6 = data.motor6
        self.motor7 = data.motor7
        self.motor8 = data.motor8
        
        self.print_sub()

    def print_sub(self) -> None:
        os.system("clear")
        # print the layout of the sub
        print("""---------------------------------------------------------
--------------------------------------------------------- 
                        SUB STATUS
                    o: %-6.2f     
            ---------------------
            |                   | 
            |                   |                               
   o: %-6.2f|                   |o: %-6.2f  
            |                   |                        x       y       z       w
            |   Vsys: %-6.2fV   |           Orientation  %-6.2f  %-6.2f  %-6.2f  %-6.2f
   v: %-6.2f|   Temp: %-6.2fC   |v: %-6.2f      Rot Vel  %-6.2f  %-6.2f  %-6.2f
            |   Pres: %-6.2fmPa |               Lin Acc  %-6.2f  %-6.2f  %-6.2f
            |   Hmid: %-6.2f%%   |                 Depth  %-6.2f
   o: %-6.2f|                   |o: %-6.2f
            |                   |
            |                   |
            ---------------------
                    o: %-6.2f
---------------------------------------------------------
---------------------------------------------------------""" % (self.motor1,
                                                                self.motor2, self.motor3,
                                                                self.volt, self.x, self.y, self.z, self.w,
                                                                self.motor4, self.temp, self.motor5, self.wx, self.wy, self.wz,
                                                                self.pressure, self.ax, self.ay, self.az,
                                                                self.humidity, self.depth,
                                                                self.motor6, self.motor7, 
                                                                self.motor8))
        
def main(args=None):
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    observer = StatusObserver()

    # spin the node
    rclpy.spin(observer)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    observer.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()


if __name__ == '__main__':
    main()