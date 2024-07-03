import serial

class MotorArduino:
    """
    This class provides methods to interface with the Teensy 4.1 that is used to drive the ESCs. Prior to use,
    the motor/ESC mappings and directions must be set. The board voltage is also measured by the Teensy 4.1
    """

    def __init__(self, com_port: str, br: int = 115200, timeout: int = .2):
        """
        Initialize the Teensy 4.1 controlling the ESCs on the sub

        @param com_port: name of serial port that the Teensy is on
        @param br: baud rate that matches the baud rate specified on the Teensy (115,200)
        """

        self.port = serial.Serial(com_port, baudrate=br, timeout=timeout)
        self.__clear_buffer__()
        self.motor2esc_mapping = [0] * 9  # NOTE: first value should always be zero to make
        self.esc_reverse_mapping = [0] * 9  # indexing and naming conventions match (motor 1 @ index 1)

    def get_voltage(self) -> float:
        """
        Get the voltage of the sub

        @rtype float
        @return: sub voltage
        """

        self.__clear_buffer__()
        self.port.write("<V>".encode("utf-8"))
        line = self.port.read(4)
        
        try:
            voltage = ((line[1] << 8) | line[2]) / 1000  # shift decimal to the left three places to get real value
        except:
            voltage = -1.0

        return voltage

    def get_assignments(self) -> tuple[list[int], list[int]]:
        """
        Get the current motor/ESC mappings and directions from the sub,
        saving, printing, and returning the results

        @rtype tuple
        @return Tuple holding the motor/ESC mappings (first) and the motor directions (second)
        """

        self.__clear_buffer__()
        self.port.write("<G>".encode("utf-8"))
        line = self.port.read(10)

        for i in range(1, 9):
            motor_esc = (line[i] & 0xf0) >> 4
            motor_reverse = (line[i] & 0x1)
            self.motor2esc_mapping[i] = motor_esc
            self.esc_reverse_mapping[i] = motor_reverse

        self.__print_current_assignments__()

        return (self.motor2esc_mapping[1:], self.esc_reverse_mapping[1:])

    def set_assignments(self) -> tuple[list[int], list[int]]:
        """
        Run through basic console interface to test and assign motors
        to their corresponding ESCs and reverse directions as needed,
        saving, printing, and returning the results.

        @rtype tuple
        @return Tuple holding the motor/ESC mappings (first) and the motor directions (second)
        """

        while True:
            self.__print_current_assignments__()
            esc = int(input("Enter esc to test (1-8) or -1 to save and quit: "))

            while esc not in range(1, 9) and esc != -1:
                esc = int(input("Enter esc to test (1-8) or -1 to save and quit: "))

            if esc == -1:
                break

            self.test_esc(esc)

            motor = int(input("Assign to motor (1-8) OR -1 to leave unchanged: "))
            while motor not in range(1,9) and motor != -1:
                motor = int(input("Assign to motor (1-8) OR -1 to leave unchanged: "))

            if motor == -1:
                continue

            self.motor2esc_mapping[motor] = esc

            reverse = int(input("Direction reverse? (0 for False or 1 for True): "))
            while reverse not in [0, 1]:
                reverse = int(input("Direction reverse? (0 for False or 1 for True): "))
            self.esc_reverse_mapping[motor] = reverse
            
            message = "<S".encode("utf-8")
            for i in range(1, 9):
                message += ((self.motor2esc_mapping[i] << 4) | self.esc_reverse_mapping[i]).to_bytes(1, "big")
            message += ">".encode("utf-8")
            self.port.write(message)

        print("Saved assignments:")
        self.__print_current_assignments__()

        return (self.motor2esc_mapping[1:], self.esc_reverse_mapping[1:])

    def load_assignments(self, mappings: list[int], directions: list[int]) -> tuple[list[int], list[int]]:
        """
        Load preset motor/ESC mappings and motor directions, returning the updated values

        @rtype tuple
        @return Tuple holding the motor/ESC mappings (first) and the motor directions (second)
        """

        for i in range(8):
            self.motor2esc_mapping[i+1] = mappings[i]
            self.esc_reverse_mapping[i+1] = directions[i]

        message = "<S".encode("utf-8")
        for i in range(1, 9):
            message += ((self.motor2esc_mapping[i] << 4) | self.esc_reverse_mapping[i]).to_bytes(1, "big")
        message += ">".encode("utf-8")
        self.port.write(message)

        return (self.motor2esc_mapping[1:], self.esc_reverse_mapping[1:])

    def run_motors(self, motor_powers: list[float]) -> None:
        """
        Set PWM values for all motors on the sub with 7-bit resolution in each direction

        @param motor_powers: list of 8 values between -1 and 1 (clamped to .4 for out-of-water testing)
                             for each of the 8 motors
        """

        # artificial cap on motors for keeping them slow
        cap = .4
        for i in range(len(motor_powers)):
            if motor_powers[i] > cap:
                motor_powers[i] = cap
                print("Looks like some of those motor values were too high!")
            if motor_powers[i] < -cap:
                motor_powers[i] = -cap
                print("Looks like some of those motor values were too high!")

        # build message with motor values
        motor_message = "<C".encode("utf-8")
        for pwr in motor_powers:
            motor_message += round(127 + 127 * pwr).to_bytes(1, "big")
        motor_message += ">".encode("utf-8")
        self.port.write(motor_message)

    def kill_motors(self) -> None:
        """
        Stop all motors
        """
        message = "<K>".encode("utf-8")
        self.port.write(message)
    
    def test_esc(self, esc: int) -> None:
        """
        Test an ESC at low RPM for out-of-water direction/motor testing

        @param esc: esc number to test (1-8)
        """
        message = "<" + str(esc) + ">"
        self.port.write(bytes(message, "utf-8"))

    def __print_current_assignments__(self) -> None:
        """
        Print out the current motor/ESC mapping and reversed flag
        """

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
        print("Motor: 1 2 3 4 5 6 7 8\nesc:   %d %d %d %d %d %d %d %d\nFlip:  %d %d %d %d %d %d %d %d" %
              (self.motor2esc_mapping[1],
               self.motor2esc_mapping[2],
               self.motor2esc_mapping[3],
               self.motor2esc_mapping[4],
               self.motor2esc_mapping[5],
               self.motor2esc_mapping[6],
               self.motor2esc_mapping[7],
               self.motor2esc_mapping[8],
               self.esc_reverse_mapping[1],
               self.esc_reverse_mapping[2],
               self.esc_reverse_mapping[3],
               self.esc_reverse_mapping[4],
               self.esc_reverse_mapping[5],
               self.esc_reverse_mapping[6],
               self.esc_reverse_mapping[7],
               self.esc_reverse_mapping[8]))

    def __clear_buffer__(self) -> None:
        """
        Clear the write buffer by reading all bytes currently in it
        """
        while self.port.inWaiting() != 0:
            self.port.read()