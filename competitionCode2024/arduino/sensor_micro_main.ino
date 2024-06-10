// Written for Metro Mini v2 (set board to Arduino Uno in Arduino IDE)
// David Jensen
// June 2024

// Packages:
//   Adafruit BMP3XX Library:2.1.4
//   Adafruit BNO055:1.6.3
//   Adafruit SHT4x Library:1.0.4
//   BlueRobotics MS5837:1.1.1


//-----------------------------------------------------
// LIBRARIES
//-----------------------------------------------------
#include <Wire.h>
#include <Adafruit_Sensor.h>

// BNO055
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// BMP388
#include "Adafruit_BMP3XX.h"

// SHT45
#include "Adafruit_SHT4x.h"

// BAR02-SENSOR-R2-RP
#include "MS5837.h"


//-----------------------------------------------------
// SENSOR CONSTANTS
//-----------------------------------------------------
// I2C pins
const static int SCL_PIN = 5;
const static int SDA_PIN = 4;

// BNO055
const static int BNO055_I2C_ADDR = 0x28;

// BMP388
const static int BMP388_I2C_ADDR = 0x77;
const static float SEALEVELPRESSURE_HPA = 1013.25;

// SHT45
const static int SHT45_I2C_ADDR = 0x44;


//-----------------------------------------------------
// SERIAL CONSTANTS
//-----------------------------------------------------
// read message setup
// has format: "< task_byte >"
char start_marker = '<';
char end_marker = '>';
const int READ_BUFF_SIZE = 1;
char read_buff[READ_BUFF_SIZE];
bool new_data = false;

//-----------------------------------------------------
// INITIALIZATIONS
//-----------------------------------------------------
Adafruit_BNO055 bno = Adafruit_BNO055(55, BNO055_I2C_ADDR, &Wire);
Adafruit_BMP3XX bmp;
Adafruit_SHT4x sht4 = Adafruit_SHT4x();
MS5837 sensor;

//-------------------------------------------------------------------------------

void setup() {
//-- Serial setup
  Serial.begin(115200);       // baud rate set at 115.2kHz
  while(!Serial);             // wait for serial connection to be established
  Serial.setTimeout(100000);  // serial input timeout after 100 seconds

//-- check for BNO055 connection
  if (!bno.begin()) {
    // send string over serial with error info
    // error flag is "!"
    // message would look like: "! <error info here>\n"
  }
//-- BNO055 setup

//-- check for BMP388 connection
  if (!bmp.begin_I2C(BMP388_I2C_ADDR, &Wire)) {
    // send string over serial with error info
    // error flag is "!"
    // message would look like: "! <error info here>\n"
  }
//-- BMP388 setup (oversampling and filter)
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);

//-- Check for SHT45 connection
  if (!sht4.begin()) {
    // send string over serial with error info
    // error flag is "!"
    // message would look like: "! <error info here>\n"
  }
//-- SHT45 setup
  // higher = longer: SHT4X_HIGH_PRECISION, SHT4X_MED_PRECISION, SHT4X_LOW_PRECISION
  sht4.setPrecision(SHT4X_LOW_PRECISION);
  // hotter = longer/more power: SHT4X_NO_HEATER, SHT4X_HIGH_HEATER_1S, SHT4X_HIGH_HEATER_100MS,
  //                                              SHT4X_MED_HEATER_1S, SHT4X_MED_HEATER_100MS,
  //                                              SHT4X_LOW_HEATER_1S, SHT4X_LOW_HEATER_100MS
  sht4.setHeater(SHT4X_NO_HEATER);

//-- Check for BAR02 connection
  if (!sensor.init()) {
    // send string over serial with error info
    // error flag is "!"
    // message would look like: "! <error info here>\n"
  }
//-- BAR02 setup
  sensor.setModel(MS5837::MS5837_02BA);
  sensor.setFluidDensity(997); // kg/m^3 (freshwater, 1029 for seawater)
}

void loop() {

  // read standard message from serial to read buffer
  receiveMessage();

  // if a full message has been received, reset and act on message
  if (new_data == true) {
    new_data = false;

    // determine action based off task_byte (char):
    //  C: get control data (gyro/acc/orientation)
    //  E: get environmental data (temp, pressure, humidity)
    switch (read_buff[0]) {
      
      case 'C': // send data used for controls (oreintation, gyro, acc)
        writeControlData();
        break;

      case 'E':
        writeEnvironmentData();
        break;

      default: // explanation
        break;
      }
  }
  delay(5);
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
 * Print orientation x/y/z, angular velocity x/y/z, and acceleration x/y/z, and depth values
 * over Serial on a single line in that order. Message flag sent first: "C"
 * 
 * @return void
 */
void writeControlData() {
  // read data from the BNO055
  sensors_event_t orientationData , angVelocityData , linearAccelData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);

  // read data from the BAR02
  sensor.read();

  Serial.print("C ");
  Serial.print(orientationData.orientation.x);
  Serial.print(" ");
  Serial.print(orientationData.orientation.y);
  Serial.print(" ");
  Serial.print(orientationData.orientation.z);
  Serial.print(" ");
  Serial.print(angVelocityData.gyro.x);
  Serial.print(" ");
  Serial.print(angVelocityData.gyro.y);
  Serial.print(" ");
  Serial.print(angVelocityData.gyro.z);
  Serial.print(" ");
  Serial.print(linearAccelData.acceleration.x);
  Serial.print(" ");
  Serial.print(linearAccelData.acceleration.y);
  Serial.print(" ");
  Serial.print(linearAccelData.acceleration.z);
  Serial.print(" ");
  Serial.print(sensor.depth());
  Serial.print("\n");

  return;
}

/**
 * Print temperature, pressure, altitude, and huididty values over Serial on a single line in that order.
 * Message flag sent first: "E" 
 *
 * @return void
 */

void writeEnvironmentData() {
  // read data from the sensors
  //BMP388
  if (!bmp.performReading()) {
        // send string over serial with error info
        // error flag is "!"
        // message would look like: "! <error info here>\n"
        return;
  }
  //SHT45
  sensors_event_t humid, temp;
  sht4.getEvent(&humid, &temp);
  // BAR02
  sensor.read();

  Serial.print("E ");
  Serial.print(temp.temperature);
  Serial.print(" ");
  Serial.print(bmp.pressure/100.0);
  Serial.print(" ");
  Serial.print(humid.relative_humidity);
  Serial.print("\n");

  return;
}