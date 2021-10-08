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

void setup() {  //looks like this attaches the servos with a delay, the comment below this was original, maybe initializes something. -ZW
    Serial.begin(115200);
    Serial.println("arduino starting...");
    delay(3000);
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

void loop() {  //seems to be a method that tests all of the different ways the robot could move. -ZW
    if(Serial.available() > 0) {
      String incomingString = Serial.readStringUntil('\n');
      Serial.print("recieved: ");
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
          return;
        } else if(incomingString == "forward"){
          moveForward();
          neut();
        } else if (incomingString == "reverse") {
          moveReverse();
          neut();
        } else if (incomingString == "neutral") {
          neut();
        } else if (incomingString == "dive") {
          dive();
          neut();
        } else if (incomingString == "hoverForward") {
          hoverforward();
          neut();
        } else if (incomingString == "hoverSpin") {
          hoverspin();
          neut();
        } else if (incomingString == "all") {
          all();
          neut();
        } else if (incomingString == "seqTest") {
          sequentialTestAll();
          neut();
        } else {
          Serial.println("command not recognized");
          neut();
        }
        Serial.println("status: done");
      } else {
          Serial.println("arduino not started");
          neut();
      }
    }
    
    
}

void surface() {
    //Serial.println("surface");
    servo6.writeMicroseconds(reverse);
    servo7.writeMicroseconds(forward);
    servo8.writeMicroseconds(forward);
    servo9.writeMicroseconds(reverse);
    delay(6000);
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

void moveForward() {
    //Serial.println("forward");
    servo2.writeMicroseconds(reverse);
    servo3.writeMicroseconds(forward);
    delay(3000);
}

void moveReverse() {
    //Serial.println("reverse");
    servo2.writeMicroseconds(forward);
    servo3.writeMicroseconds(reverse);
    delay(3000);
}

void dive() {
    //Serial.println("drive");
    servo6.writeMicroseconds(forward+25);
    servo7.writeMicroseconds(reverse-25);
    servo8.writeMicroseconds(reverse-25);
    servo9.writeMicroseconds(forward+25);
    delay(3000);
}

void diveForward() {
    //Serial.println("dive forward");
    servo6.writeMicroseconds(forward);
    servo7.writeMicroseconds(reverse-50);
    servo8.writeMicroseconds(reverse-50);
    servo9.writeMicroseconds(forward);
    servo2.writeMicroseconds(reverse);
    servo3.writeMicroseconds(forward);
    delay(6000);   
}

void spin() {
    //Serial.println("spin");
    servo2.writeMicroseconds(forward);
    servo3.writeMicroseconds(forward);
    delay(3000);
}

void hoverspin() {
    //Serial.println("hover spin");
    servo2.writeMicroseconds(forward);
    servo3.writeMicroseconds(forward);
    servo6.writeMicroseconds(forward+25);
    servo7.writeMicroseconds(reverse-25);
    servo8.writeMicroseconds(reverse-25);
    servo9.writeMicroseconds(forward+25);
    delay(1000);
}

void hoverforward() {
    //Serial.println("hover forward");
    servo2.writeMicroseconds(reverse);
    servo3.writeMicroseconds(forward);
    servo6.writeMicroseconds(forward+25);
    servo7.writeMicroseconds(reverse-25);
    servo8.writeMicroseconds(reverse-25);
    servo9.writeMicroseconds(forward+25);
    delay(3500);
}

void all() {
    servo2.writeMicroseconds(reverse);
    servo3.writeMicroseconds(reverse);
    servo4.writeMicroseconds(reverse);
    servo5.writeMicroseconds(reverse);
    servo6.writeMicroseconds(reverse);
    servo7.writeMicroseconds(reverse);
    servo8.writeMicroseconds(reverse);
    servo9.writeMicroseconds(reverse);
    delay(3500);
}

void sequentialTestAll(){
  testMotor1();
  neut();
  testMotor2();
  neut();
  testMotor3();
  neut();
  testMotor4();
  neut();
  testMotor5();
  neut();
  testMotor6();
  neut();
  testMotor7();
  neut();
  testMotor8();
  neut();
}

void testMotor1() {
  Serial.println("Testing Motor 1");
  servo2.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo2.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor2() {
  Serial.println("Testing Motor 2");
  servo3.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo3.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor3() {
  Serial.println("Testing Motor 3");
  servo4.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo4.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor4() {
  Serial.println("Testing Motor 4");
  servo5.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo5.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor5() {
  Serial.println("Testing Motor 5");
  servo6.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo6.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor6() {
  Serial.println("Testing Motor 6");
  servo7.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo7.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor7() {
  Serial.println("Testing Motor 7");
  servo8.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo8.writeMicroseconds(reverse);
  delay(testingDelay);
}

void testMotor8() {
  Serial.println("Testing Motor 8");
  servo9.writeMicroseconds(forward);
  delay(testingDelay);
  neut();
  delay(testingDelay);
  servo9.writeMicroseconds(reverse);
  delay(testingDelay);
}
