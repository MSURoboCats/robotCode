// Written for Teensy 4.1
// David Jensen
// May 2024

// ESC's numbered left to right on PCB
uint8_t esc1pin = 9;
uint8_t esc2pin = 8;
uint8_t esc3pin = 7;
uint8_t esc4pin = 6;
uint8_t esc5pin = 5;
uint8_t esc6pin = 4;
uint8_t esc7pin = 3;
uint8_t esc8pin = 2;

// ESCs run on 20ms period (50Hz) with min and max at 1.1ms (5.5% duty) and 1.9ms (9.5% duty); stop at 1.5ms (7.5% duty)
// Clock is 15-bit (32767 = 2^15 - 1)
uint16_t max_pwm = .095*32767;
uint16_t stop_pwm = .075*32767;
uint16_t min_pwm = .055*32767;

// default ESC/motor mapping info
// NOTE: first value should always be zero - makes indexing and naming conventions match (motor 1 @ index 1)
uint8_t esc2pin_mapping[] = {0, esc1pin, esc2pin, esc3pin, esc4pin, esc5pin, esc6pin, esc7pin, esc8pin}; // index is ESC (index 1 -> ESC 1); value is pin number
uint8_t motor2esc_mapping[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};                                               // index is motor number (index 1 -> motor 1); value is ESC number (1-8)
uint8_t esc_reverse_mapping[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};                                              // 0 for correct; 1 for reversed

// voltage divider constants
uint16_t board_voltage_adc_val;               // value read from analog pin
float ten_bit_scaler = 1/1023.0 * 3.3;        // scale 10-bit value to 0-3.3V
float corrective_scaler = 1.0046;             // experimentally determined by dividing read voltage vs measured voltage
float divider_scaler = 8.136 / (46.98+8.136); // voltage divider from resistors using measured resistance values

// read message setup
// has format: "< task_byte motor1_byte motor2_byte .... motor8_byte >"
// a motor byte is either uint8_t with 0 corresponding to -1 and 255 to 1 (min/max motor pwm)
// or
// 0000 xxx0 -> first four used to assign which ESC the motor is controlled by; last used to specify whether the motor direction should be reversed
char start_marker = '<';
char end_marker = '>';
const int READ_BUFF_SIZE = 9;
char read_buff[READ_BUFF_SIZE];
bool new_data = false;

// mappings message setup
// has format: "< motor1_byte motor2_byte .... motor8_byte >"
// each motor byte: 0000 xxx0 -> first four used to assign which ESC the motor is controlled by; last  used to specify whether the motor direction should be reversed
const int MAPPINGS_BUFF_SIZE = 8;
char mappings_buff[MAPPINGS_BUFF_SIZE];

// voltage message setup
// has format: "< voltage_byte1 voltage_byte2 >"
// representing voltage reading 0x<byte1><byte2> * 10^-3 (value*10^-3)
const int VOLTAGE_BUFF_SIZE = 4;
char voltage_buff[VOLTAGE_BUFF_SIZE];

//-------------------------------------------------------------------------------

void setup() {
//-- Serial setup
  Serial.begin(115200);       // baud rate set at 115.2kHz
  while(!Serial);             // wait for serial connection to be established
  Serial.setTimeout(100000);  // serial input timeout after 100 seconds

//-- ESC pin setup 
  // set all motor pins as outputs
  pinMode(esc1pin, OUTPUT);
  pinMode(esc2pin, OUTPUT);
  pinMode(esc3pin, OUTPUT);
  pinMode(esc4pin, OUTPUT);
  pinMode(esc5pin, OUTPUT);
  pinMode(esc6pin, OUTPUT);
  pinMode(esc7pin, OUTPUT);
  pinMode(esc8pin, OUTPUT);

  // set frequency of all ouotput pins to 50Hz
	analogWriteFrequency(esc1pin, 50); // sets 2,3 to 50Hz
  analogWriteFrequency(esc2pin, 50); // sets 2,3 to 50Hz
  analogWriteFrequency(esc3pin, 50); // sets 4,33 to 50Hz
  analogWriteFrequency(esc4pin, 50); // sets 5 to 50Hz
  analogWriteFrequency(esc5pin, 50); // sets 6,9 to 50Hz
  analogWriteFrequency(esc6pin, 50); // sets 7,8 to 50Hz
  analogWriteFrequency(esc7pin, 50); // sets 7,8 to 50Hz
  analogWriteFrequency(esc8pin, 50); // sets 6,9 to 50Hz

  // set duty cycle resolution to 15-bit (0-32767)
	analogWriteResolution(15);

  // initialize all ESCs with a stop signal
	analogWrite(esc1pin, stop_pwm);
  analogWrite(esc2pin, stop_pwm); 
	analogWrite(esc3pin, stop_pwm); 
	analogWrite(esc4pin, stop_pwm); 
	analogWrite(esc5pin, stop_pwm);
	analogWrite(esc6pin, stop_pwm);
	analogWrite(esc7pin, stop_pwm); 
	analogWrite(esc8pin, stop_pwm); 
	delay(2000); // delay to allow for initialization to be recognized
}

void loop() {

  // read standard message from serial to read buffer
  receiveMessage();

  // if a full message has been received, reset and act on message
  if (new_data == true) {
    new_data = false;

    // determine action based off task_byte (char):
    //  1 through 8: test ESC with the corresponing number
    //  G: get current motor/ESC and direction mappings
    //  S: set motor/ESC and direction mappings
    //  C: control motor PWM values
    //  V: get board voltage
    //  K: kill all motors
    switch (read_buff[0]) {
      case '1': // test ESC 1 (run ESC in "forward" as mapped to ESC)
        testESC(1, 2);
        break;
      case '2': // test ESC 2 (run ESC in "forward" as mapped to ESC)
        testESC(2, 2);
        break;
      case '3': // test ESC 3 (run ESC in "forward" as mapped to ESC)
        testESC(3, 2);
        break;
      case '4': // test ESC 4 (run ESC in "forward" as mapped to ESC)
        testESC(4, 2);
        break;
      case '5': // test ESC 5 (run ESC in "forward" as mapped to ESC)
        testESC(5, 2);
        break;
      case '6': // test ESC 6 (run ESC in "forward" as mapped to ESC)
        testESC(6, 2);
        break;
      case '7': // test ESC 7 (run ESC in "forward" as mapped to ESC)
        testESC(7, 2);
        break;
      case '8': // test ESC 8 (run ESC in "forward" as mapped to ESC)
        testESC(8, 2);
        break;

      case 'G': // get motor mappings
        writeMappings(mappings_buff);
        Serial.write('<');
        Serial.write(mappings_buff, MAPPINGS_BUFF_SIZE);
        Serial.write('>');
        break;

      case 'S': // set motor mappings
        setMappings(read_buff);
        break;

      case 'C': // control motor values
        setPWMs(read_buff);
        break;
      
      case 'V': // get voltage
        writeVoltage(voltage_buff);
        Serial.write('<');
        Serial.write(voltage_buff, VOLTAGE_BUFF_SIZE);
        Serial.write('>');
        break;

      case 'K': // kill all motor PWMs
        killMotors();
        break;
      
      default: // kill all motor PWMs
        killMotors();
        break;
      }
  }
}

/**
 * Reads message from serial following format of read_buff.
 * R/W to global variables:
 *  read_buff[]
 *  new_data
 *  start_marker
 *  end_marker
 * 
 * @return void
 */
void receiveMessage() {

  char recv;                      // received byte
  uint8_t idx = 0;                // current index of message
  bool recv_in_progress = false;  // mid-receive

  // while bytes in receive buffer and the full message has not been received,
  // read the byte: if start or stop marker, discard and start/end message
  //                else, store in message and continue receiving
  while(Serial.available() > 0 && new_data == false) {
    recv = Serial.read();

    if (recv_in_progress == true) {
      if (recv != end_marker) {
        read_buff[idx] = recv;
        idx ++;
      }
      else {
        recv_in_progress = false;
        idx = 0;
        new_data = true;
      }
    }

    else if (recv == start_marker) {
      recv_in_progress = true;
    }
  }
}

/**
 * Runs a single ESC in the corrected forward direction
 * 
 * @param esc (uint8_t esc) esc to test (1-8)
 * @param sec (uint8_t esc) seconds to run esc for
 * @return void
 */

void testESC(uint8_t esc, uint8_t sec) {
  if(esc<1 || esc>8) { return; }
  // run ESC in direction saved as forwards for _ seconds at 15% power
  analogWrite(esc2pin_mapping[esc], (esc_reverse_mapping[esc]==1 ?  .073*32767 : .077*32767));
  delay(sec*1000);
  analogWrite(esc2pin_mapping[esc], stop_pwm);
}

/**
 * Sets motor/esc mapping all motors based on input array in read_buff format
 * 
 * @param byte_array[] array following read_buff format: "< task_byte motor1_byte ... motor8_byte >"
 *                     with each byte the first four bit of each byte corresponding to the which ESC
 *                     the motor is mapped to, and the last bit of the byte corresponding to the 
 *                     direction of the motor (0 for normal; 1 for reversed)
 * @return void
 */
void setMappings(char byte_array[]) {
  // assign ESC and direction for every motor
  for(uint8_t i=1; i<9; i++) {
    uint8_t esc = (byte_array[i] & 0xf0) >> 4; // get ESC number from first four bits of the motor byte
    motor2esc_mapping[i] = esc;
    uint8_t reversed = (byte_array[i] & 0x1); // get reverse bool from last four bits of the motor byte
    esc_reverse_mapping[esc] = reversed;
  }
}

/**
 * Sets PWM values for all motors based on input array in read_buff format
 * 
 * @param byte_array[] array following read_buff format: "< task_byte motor1_byte ... motor8_byte >"
 *                     with each byte mapped from [0, 255] to [-1, 1] then convereted to corresponding PWM values
 * @return void
 */
void setPWMs(char byte_array[]) {
  float prop;
  for(uint8_t i=1; i<9; i++) {
    uint8_t esc = motor2esc_mapping[i];
    prop = ((esc_reverse_mapping[esc]==1 ? 255 - byte_array[i] : byte_array[i]) - 127) / 128.0; // map [0, 255] to [-1, 1], reversing as necessary
    uint16_t pwm = (prop + 1) * (max_pwm - min_pwm) / 2 + min_pwm;                              // map [-1, 1] to [min_pwm, max_pwm]
    analogWrite(esc2pin_mapping[esc], pwm);
  }
}

/**
 * Kills all motors
 * 
 * @return void
 */
void killMotors() {
  for(uint8_t i=1; i<9; i++) {
    uint8_t esc = motor2esc_mapping[i]; 
    analogWrite(esc2pin_mapping[esc], stop_pwm);
  }
}

/**
 * Writes the current voltage to an array in-place
 * 
 * @param byte_array[] array of 2 bytes to store voltage
 * @return void; array assignmet is done in-place
 */
void writeVoltage(char byte_array[]) {
  // ADC reading (16-bit)
  board_voltage_adc_val = analogRead(14);

  // calculate voltage with the decimal shifted three to the right (*10^3)
  uint16_t floating_voltage = board_voltage_adc_val*ten_bit_scaler*corrective_scaler/divider_scaler*1000;

  // send calculated voltage
  byte_array[0] = (floating_voltage & 0x0000ff00) >> 8; // second byte are the last 8 bits
  byte_array[1] = (floating_voltage & 0x000000ff); // second byte are the last 8 bits

}

/**
 * Writes the current motor mappings to an array in-place
 * 
 * @param byte_array[] array of 8 bytes to store mappings in
 * @return void; array assignmet is done in-place
 */
void writeMappings(char byte_array[]) {
  // motor mappings
  for(uint8_t i=0; i<8; i++) {
    // first four bits are the ESC number (1-8) and last bit is 0 for not reversed / 1 for reversed
    byte_array[i] = (motor2esc_mapping[i+1] << 4) | (esc_reverse_mapping[motor2esc_mapping[i+1]] == 1 ? 1 : 0);
  }
}
