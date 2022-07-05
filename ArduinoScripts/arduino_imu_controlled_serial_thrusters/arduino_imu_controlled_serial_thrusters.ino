#include <Wire.h>
#include <Servo.h>

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
int numberOfThrusters = sizeof(pins)/sizeof(pins[0]);

void neut();
void surface();
void motor(int, int);

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
        servo2.detach();
        servo3.detach();
        servo4.detach();
        servo5.detach();
        servo6.detach();
        servo7.detach();
        servo8.detach();
        servo9.detach();
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
  //int microseconds = map(percentage, reverse, forward, -100, 100);
  int microseconds = map(percentage, -100, 100, reverse, forward);
  switch (motor_number) {
    case 1:
      servo2.writeMicroseconds(microseconds);
      break;
    case 2:
      servo3.writeMicroseconds(microseconds);
      break;
    case 3:
      servo4.writeMicroseconds(microseconds);
      break;
    case 4:
      servo5.writeMicroseconds(microseconds);
      break;
    case 5:
      servo6.writeMicroseconds(microseconds);
      break;
    case 6:
      servo7.writeMicroseconds(microseconds);
      break;
    case 7:
      servo8.writeMicroseconds(microseconds);
      break;
    case 8:
      servo9.writeMicroseconds(microseconds);
      break;
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
