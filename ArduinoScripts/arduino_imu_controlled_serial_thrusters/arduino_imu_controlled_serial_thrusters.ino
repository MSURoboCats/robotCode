#include <MS5837.h>

#include <Wire.h>
#include <Servo.h>

MS5837 depth_pressure_sensor;

Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;

int startFlag = 1; //false
int killFlag = 1; //false

int neutral = 1500;
int down = 1600;
int up = 1400;
int reverse = 1750;
int forward = 1250;
int testingDelay = 1000;
int pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
    Serial.begin(115200);
    Wire.begin();
    Serial.println("arduino starting...");
    delay(100);

    // Initialize pressure sensor
    // Returns true if initialization was successful
    // We can't continue with the rest of the program unless we can initialize the sensor
//    while (!sensor.init()) {
//      Serial.println("Blue Robotics Bar02: Init failed");
//      depth_pressure_sensor.setFluidDensity(1.225); // kg/m^3 (1.225 air, 997 freshwater, 1029 for seawater)
//    }

    servo2.attach(2);
    servo3.attach(3);
    servo4.attach(4);
    servo5.attach(5);
    servo6.attach(6);
    servo7.attach(7);
    servo8.attach(8);
    servo9.attach(9);
    neut();
}

void loop() {
    if(startFlag != 0 || killFlag == 0){
        if(Serial.available() > 0) {
          String incomingString = Serial.readStringUntil('\n');
          Serial.print("received: ");
          Serial.println(incomingString);
          if(killFlag == 0) {
            neut();
            Serial.println("status: killed");
            delay(999999999);
          } else if(incomingString == "start" && startFlag == 1 && killFlag == 1){
            startFlag = 0;
            Serial.println("arduino ready");
          } else {
            Serial.println("arduino not started");
            neut();
        }
    } else {
        if (incomingString == "kill") {
          neut();
          killFlag = 0;
          Serial.println("Mega Halted: Power Cycle to restart");
          Serial.println("status: killed");
          servo2.detach();
          servo3.detach();
          servo4.detach();
          servo5.detach();
          servo6.detach();
          servo7.detach();
          servo8.detach();
          servo9.detach();
        else if (incomingString.startsWith("surface")) {
          surface();
        } else if (incomingString.startsWith("driveMotor:")){
          // format: driveMotor:motorNumber:motorPercentage;
          String num_str = incomingString.substring(12,13);
          int num = num_str.toInt();
          String per_str = incomingString.substring(14,incomingString.indexOf(";"));
          int per = per_str.toInt();
          motor(num+1, per);
        } else if (incomingString.startsWith("imuControl:")) {
          // format: imuControl:numberOfMotors;motorNumberX:motorXPercentage;motorNumberY:motorYPercentage;...motorNumberN:motorNPercentage;
          // figure out which motors to control write to them and stop motors not in input string
          Serial.println("command not implemented");
        } else if (incomingString.startsWith("eachMotor:")) {
        // format: eachMotor:motorNumber0:motor0Percentage;motorNumber1:motor1Percentage;...motorNumber8:motor8Percentage;
        } else {
          Serial.println("command not recognized");
          neut();

    }




    if(Serial.available() > 0) {
      String incomingString = Serial.readStringUntil('\n');
      Serial.print("received: ");
      Serial.println(incomingString);
      if(killFlag == 0) {
        neut();
        Serial.println("status: killed");
        delay(999999999);
      } else if(incomingString == "start" && startFlag == 1){
        startFlag = 0;
        Serial.println("arduino ready");
      } else if (startFlag == 0){
        if (incomingString == "kill") {
          neut();
          killFlag = 0;
          Serial.println("Mega Halted: Power Cycle to restart");
          Serial.println("status: killed");
          servo2.detach();
          servo3.detach();
          servo4.detach();
          servo5.detach();
          servo6.detach();
          servo7.detach();
          servo8.detach();
          servo9.detach();
          return;
        } else if (incomingString.startsWith("driveMotor:")){
          String num_str = incomingString.substring(12,13);
          int num = num_str.toInt();
          String per_str = incomingString.substring(14,incomingString.indexOf(";"));
          int per = per_str.toInt();
          motor(num+1, per);
        } else {
          Serial.println("command not recognized");
          neut();
        }
        Serial.println("status: done");
      } else {
          Serial.println("arduino not started");
          neut();
      }
    } else {

    }
}

void neut() {
    //Serial.println("neutral");
    servo2.writeMicroseconds(neutral);
    servo3.writeMicroseconds(neutral);
    servo4.writeMicroseconds(neutral);
    servo5.writeMicroseconds(neutral);
    servo6.writeMicroseconds(neutral);
    servo7.writeMicroseconds(neutral);
    servo8.writeMicroseconds(neutral);
    servo9.writeMicroseconds(neutral);
    delay(500);
}

void motor(int motor_number, int percentage) {
  int microseconds = map(percentage, reverse, forward, -100, 100);
  switch (motor_number) {
    case 1:
      servo2.writeMicroseconds(microseconds);
      break;
    case 2:
      servo3.writeMicroseconds(microseconds);
      break;
    case 3:
      servo2.writeMicroseconds(microseconds);
      break;
    case 4:
      servo2.writeMicroseconds(microseconds);
      break;
    case 5:
      servo2.writeMicroseconds(microseconds);
      break;
    case 6:
      servo2.writeMicroseconds(microseconds);
      break;
    case 7:
      servo2.writeMicroseconds(microseconds);
      break;
    case 8:
      servo2.writeMicroseconds(microseconds);
      break;
  }
}

void surface() {
    //Serial.println("surface");
    servo2.writeMicroseconds(neutral);
    servo3.writeMicroseconds(neutral);
    servo4.writeMicroseconds(neutral);
    servo5.writeMicroseconds(neutral);

    servo6.writeMicroseconds(reverse);
    servo7.writeMicroseconds(forward);
    servo8.writeMicroseconds(forward);
    servo9.writeMicroseconds(reverse);
}
