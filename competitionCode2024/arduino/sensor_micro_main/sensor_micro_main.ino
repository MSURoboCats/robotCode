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
#include <avr/power.h>

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
sensors_event_t humid, temp;
uint8_t n = 0; // counter for sending hull data only every 16 iterations

//-------------------------------------------------------------------------------

void setup() {
//-- Set to run at 8MHz since we are running on 3.3V
  //clock_prescale_set(clock_div_2);

//-- Serial setup
  Serial.begin(115200);       // baud rate set at 115.2kHz //(multiply by two because MCU is slowed down by 2)
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

  writeData();

}

/**
 * Print orientation x/y/z, angular velocity x/y/z, and acceleration x/y/z, external pressure,
 * temperature, hull pressure, and humidity values over Serial on a single line in that order.
 * 
 * @return void
 */
void writeData() {
  // read data from the BNO055
  sensors_event_t angVelocityData , linearAccelData;
  imu::Quaternion orientationData = bno.getQuat();
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);

  // read data from the BAR02
  sensor.read();
  
  // every 16 loops, read hull data
  if(n%16 == 0) {
    n = 1;
    //BMP388
    if (!bmp.performReading()) {
          // send string over serial with error info
          // error flag is "!"
          // message would look like: "! <error info here>\n"
          return;
    }

    //SHT45
    sht4.getEvent(&humid, &temp);
  }

  // write each number into 10 chars with a single space (11 total per)
  // 154 bytes total
  char float_buff[10];

  dtostrf(orientationData.x(), 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(orientationData.y(), 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(orientationData.z(), 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(orientationData.w(), 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(angVelocityData.gyro.x, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(angVelocityData.gyro.y, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(angVelocityData.gyro.z, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(linearAccelData.acceleration.x, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(linearAccelData.acceleration.y, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(linearAccelData.acceleration.z, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(sensor.pressure(), 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(temp.temperature, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(bmp.pressure/100.0, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write(' ');

  dtostrf(humid.relative_humidity, 10, 4, float_buff);
  Serial.write(float_buff);
  Serial.write('\n');

  n++;

  return;
}