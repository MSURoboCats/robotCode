import rclpy               
from rclpy.node import Node

from interfaces.msg import Mappings
from interfaces.srv import GetMappings

from std_msgs.msg import Int16

import os

class ESCTesterNode(Node):

    def __init__(self):
        super().__init__('esc_tester_node')
        
        # publisher to test an ESC
        self.test_esc = self.create_publisher(Int16, 'test_esc', 10)

        # client to get motor mappings
        self.get_mappings_cli = self.create_client(GetMappings, 'get_mappings')
        while not self.get_mappings_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('get_mappings service not available, waiting again...')
        self.get_mappings_req = GetMappings.Request()

        # publisher to set motor mapping
        self.mappings_pub = self.create_publisher(Mappings, 'set_mappings', 10)

    def get_motor_mappings(self) -> None:
        # make a request for motor mappings
        self.get_mappings_future = self.get_mappings_cli.call_async(self.get_mappings_req)
    
    def print_sub(self) -> None:
        # print the layout of the sub
        print("         1<\n" +
                "  ----------------     * * * * * * *\n" +
                "  |       DOME   |     * FORWARD:  *\n" +
                "2o|              |3o   * o - up    *\n" +
                "  |              |     * < - left  *\n" +
                "4v|   SUB (TOP)  |5v   * > - right *\n" +
                "  |              |     * v - down  *\n" +
                "6o|         PORTS|7o   * o - up    *\n" +
                "  ----------------     * * * * * * *\n" +
                "         8>")

    def print_mappings(self, assignments: Mappings) -> None:
        # print the current motor mappings/directions
        print("Motor: 1 2 3 4 5 6 7 8\nesc:   %d %d %d %d %d %d %d %d\nFlip:  %d %d %d %d %d %d %d %d" %
                (assignments.motor1.esc,
                assignments.motor2.esc,
                assignments.motor3.esc,
                assignments.motor4.esc,
                assignments.motor5.esc,
                assignments.motor6.esc,
                assignments.motor7.esc,
                assignments.motor8.esc,
                assignments.motor1.direction,
                assignments.motor2.direction,
                assignments.motor3.direction,
                assignments.motor4.direction,
                assignments.motor5.direction,
                assignments.motor6.direction,
                assignments.motor7.direction,
                assignments.motor8.direction))

def main(args=None):
    os.system("clear")
    
    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    tester = ESCTesterNode()

    # var to hold the current mappings
    cur_assignments = Mappings()

    # get the current mappings
    tester.get_motor_mappings()
    while rclpy.ok():
        rclpy.spin_once(tester)
        if tester.get_mappings_future.done():
            try:
                cur_assignments = tester.get_mappings_future.result().mappings
            except Exception as e:
                tester.get_logger().info(
                    'Service call for motor mappings failed %r' % (e,))
            else:
                tester.get_logger().info(
                    'Motor mappings read successfully')
            break

    # run the UI to test/set motor mappings and directions
    while True:
        tester.print_sub()
        tester.print_mappings(cur_assignments)

        # get ESC to test
        esc = int(input("Enter esc to test (1-8) or -1 to save and quit: "))
        while esc not in range(1, 9) and esc != -1:
            esc = int(input("Enter esc to test (1-8) or -1 to save and quit: "))
        
        # exit if the assignments are good - keep looping if not
        if esc == -1:
            if len(set([cur_assignments.motor1.esc,
                        cur_assignments.motor2.esc,
                        cur_assignments.motor3.esc,
                        cur_assignments.motor4.esc,
                        cur_assignments.motor5.esc,
                        cur_assignments.motor6.esc,
                        cur_assignments.motor7.esc,
                        cur_assignments.motor8.esc,
                        ])) != 8:
                os.system("clear")
                print("Invalid assignment: each ESC must map to a single motor. Fix it.")
                continue
            else:
                break
        
        # publish ESC number to test
        esc_msg = Int16()
        esc_msg.data = esc
        tester.test_esc.publish(esc_msg)

        # assign to motor or leave unchanged
        motor = int(input("Assign to motor (1-8) OR -1 to leave unchanged: "))
        while motor not in range(1,9) and motor != -1:
            motor = int(input("Assign to motor (1-8) OR -1 to leave unchanged: "))

        if motor == -1:
            os.system("clear")
            continue       

        # assign direction
        reverse = int(input("Direction reverse? (0 for False or 1 for True): "))
        while reverse not in [0, 1]:
            reverse = int(input("Direction reverse? (0 for False or 1 for True): "))
        
        # only change assignments for the updated motor
        if motor == 1:
            cur_assignments.motor1.esc = esc
            cur_assignments.motor1.direction = reverse
        elif motor == 2:
            cur_assignments.motor2.esc = esc
            cur_assignments.motor2.direction = reverse
        elif motor == 3:
            cur_assignments.motor3.esc = esc
            cur_assignments.motor3.direction = reverse
        elif motor == 4:
            cur_assignments.motor4.esc = esc
            cur_assignments.motor4.direction = reverse
        elif motor == 5:
            cur_assignments.motor5.esc = esc
            cur_assignments.motor5.direction = reverse
        elif motor == 6:
            cur_assignments.motor6.esc = esc
            cur_assignments.motor6.direction = reverse
        elif motor == 7:
            cur_assignments.motor7.esc = esc
            cur_assignments.motor7.direction = reverse
        elif motor == 8:
            cur_assignments.motor8.esc = esc
            cur_assignments.motor8.direction = reverse
        os.system("clear")

        # publish new assignments
        tester.mappings_pub.publish(cur_assignments)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    tester.destroy_node()

    # shutdown the ROS client library for Python
    rclpy.shutdown()


if __name__ == '__main__':
    main()