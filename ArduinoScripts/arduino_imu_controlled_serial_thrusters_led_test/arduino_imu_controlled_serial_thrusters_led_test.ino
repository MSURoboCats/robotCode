#include <Wire.h>
#include "Thruster.h"

int startFlag = 1; //false
int killFlag = 1; //false

int neutral = 1500;
int down = 1600;
int up = 1400;
int reverse = 1750;
int forward = 1250;
int testingDelay = 1000;
int pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
int numberOfThrusters = sizeof(pins)/sizeof(pins[0]);

void neut();
void surface();
void motor(int, int);

Thruster thruster2(2, forward, reverse, neutral, false);
Thruster thruster3(3, forward, reverse, neutral, false);
Thruster thruster4(4, forward, reverse, neutral, false);
Thruster thruster5(5, forward, reverse, neutral, false);
Thruster thruster6(6, forward, reverse, neutral, false);
Thruster thruster7(7, forward, reverse, neutral, false);
Thruster thruster8(8, forward, reverse, neutral, false);
Thruster thruster9(9, forward, reverse, neutral, false);

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

  neut();

  delay(100);
}

void loop() {
  if (startFlag != 0 || killFlag == 0) {
    if (Serial.available() > 0) {
      String incomingString = Serial.readStringUntil('\n');
      Serial.print("received: ");
      Serial.println(incomingString);
      if (killFlag == 0) {
        neut();
        Serial.println("status: killed");
        delay(999999999);
      } else if (incomingString == "start" && startFlag == 1 && killFlag == 1) {
        startFlag = 0;
        Serial.println("arduino ready");
      } else {
        Serial.println("arduino not started");
        neut();
      }
    }
  } else {
    if (Serial.available() > 0) {
      String incomingString = Serial.readStringUntil('\n');
      Serial.print("received: ");
      Serial.println(incomingString);
      if (incomingString == "kill") {
        neut();
        killFlag = 0;
        Serial.println("Mega Halted: Power Cycle to restart");
        Serial.println("status: killed");
        thruster2.kill();
        thruster3.kill();
        thruster4.kill();
        thruster5.kill();
        thruster6.kill();
        thruster7.kill();
        thruster8.kill();
        thruster9.kill();
      } else if (incomingString.startsWith("neutral")) {
        neut();
      } else if (incomingString.startsWith("surface")) {
        surface();
      } else if (incomingString.startsWith("driveMotor:")) {
        // format: driveMotor:motorNumber>motorPercentage;
        String num_str = incomingString.substring(11, 12);
        int num = num_str.toInt();
        String per_str = incomingString.substring(14, incomingString.indexOf(";"));
        int per = per_str.toInt();
        motor(num, per);
      } else if (incomingString.startsWith("imuControl:")) {
        // format: imuControl:numberOfMotors;motorNumberX:motorXPercentage;motorNumberY:motorYPercentage;...motorNumberN:motorNPercentage;
        // figure out which motors to control write to them and stop motors not in input string. If a motor is not set it will be set to neutral
        // imuControl:5>4:-70;3:90;1:-100;7:100;5:0;
        int motorNumber, motorNumberIndex;
        int motorsModified[8] = {0, 0, 0, 0, 0, 0, 0, 0};
        int numberOfMotors = incomingString.substring(incomingString.indexOf(":")+1, incomingString.indexOf(">")).toInt();
        String motorString = incomingString.substring(incomingString.indexOf(">")+1);
        for(motorNumberIndex=0;motorNumberIndex<numberOfMotors;motorNumberIndex++) {
          motorNumber = motorString.substring(0, 1).toInt();
          motorsModified[motorNumber-1] = 1;
          int percentage = motorString.substring(2, motorString.indexOf(";")).toInt();
          motor(motorNumber, percentage);
          motorString = motorString.substring(motorString.indexOf(";")+1);
        }
        for(motorNumberIndex=0;motorNumberIndex<numberOfThrusters;motorNumberIndex++) {
          if (motorsModified[motorNumberIndex] == 0) {
            motor(motorNumberIndex+1, 0);
          } 
        }
      } else if (incomingString.startsWith("eachMotor:")) {
        // format: eachMotor:motor0Percentage;motor1Percentage;...motor8Percentage;
        // eachMotor:20;30;40;50;60;70;80;90;
        int motorNumber;
        String motorString = incomingString.substring(incomingString.indexOf(":")+1);
        for(motorNumber=1;motorNumber<(numberOfThrusters+1);motorNumber++){
          int percentage = motorString.substring(0, motorString.indexOf(";")).toInt();
          motor(motorNumber, percentage);
          motorString = motorString.substring(motorString.indexOf(";")+1);
        }
      } else {
        Serial.println("command not recognized");
        neut();
      }
    }
  }
}



void motor(int motor_number, int percentage) {
  switch (motor_number) {
    case 1:
      thruster2.setThrusterSpeed(percentage);;
      break;
    case 2:
      thruster3.setThrusterSpeed(percentage);
      break;
    case 3:
      thruster4.setThrusterSpeed(percentage);
      break;
    case 4:
      thruster5.setThrusterSpeed(percentage);
      break;
    case 5:
      thruster6.setThrusterSpeed(percentage);
      break;
    case 6:
      thruster7.setThrusterSpeed(percentage);
      break;
    case 7:
      thruster8.setThrusterSpeed(percentage);
      break;
    case 8:
      thruster9.setThrusterSpeed(percentage);
      break;
  }
}

void neut() {
  //Serial.println("neutral");
  thruster2.setThrusterSpeed(0);
  thruster3.setThrusterSpeed(0);
  thruster4.setThrusterSpeed(0);
  thruster5.setThrusterSpeed(0);
  thruster6.setThrusterSpeed(0);
  thruster7.setThrusterSpeed(0);
  thruster8.setThrusterSpeed(0);
  thruster9.setThrusterSpeed(0);
}


void surface() {
  //Serial.println("surface");
  thruster2.setThrusterSpeed(0);
  thruster3.setThrusterSpeed(0);
  thruster4.setThrusterSpeed(0);
  thruster5.setThrusterSpeed(0);
  
  thruster6.setThrusterSpeed(-100);
  thruster7.setThrusterSpeed(100);
  thruster8.setThrusterSpeed(100);
  thruster9.setThrusterSpeed(-100);
}
