#include <Servo.h>


Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;

//----------------------------------------------------Motor Speed Varibles---------------------------------------------//
int neutral = 1500;
int down = 1600;
int up = 1400;
int reverse = 1750;
int forward = 1250;
int testingDelay = 1000;
//--------------------------------------------------------------------------------------------------------------------//

void setup() {
//---------------------------------------------------Motor Pin Assignments-------------------------------------------//
	servo2.attach(2);
  servo3.attach(3);
  servo4.attach(4);
  servo5.attach(5);
  servo6.attach(6);
  servo7.attach(7);
  servo8.attach(8);
  servo9.attach(9);
//------------------------------------------------------------------------------------------------------------------//

	// send "stop" signal to ESC.
  servo2.writeMicroseconds(neutral);
  servo3.writeMicroseconds(neutral);
  servo4.writeMicroseconds(neutral);
  servo5.writeMicroseconds(neutral);
  servo6.writeMicroseconds(neutral);
  servo7.writeMicroseconds(neutral);
  servo8.writeMicroseconds(neutral);
  servo9.writeMicroseconds(neutral);

	delay(7000); // delay to allow the ESC to recognize the stopped signal

  
  //------------------------------------------------Enter Testing Code Here----------------------------------------//
  
  servo5.writeMicroseconds(up); // Example-- Run motor 5 up for 3 seconds and stop 
  delay(3000);
  servo5.writeMicroseconds(neutral);

  surface(); // Example-- Call surface command

  //--------------------------------------------------------------------------------------------------------------//

  

  //send "stop" signal to all ESCs.
  servo2.writeMicroseconds(neutral);
  servo3.writeMicroseconds(neutral);
  servo4.writeMicroseconds(neutral);
  servo5.writeMicroseconds(neutral);
  servo6.writeMicroseconds(neutral);
  servo7.writeMicroseconds(neutral);
  servo8.writeMicroseconds(neutral);
  servo9.writeMicroseconds(neutral);
  
}

void loop() {
}

//---------------------------------------------Commands from main program------------------------------------------//
//You can call these in the test code to test motor pin assignment and functionality 
//Example-- When runing "surface" command the 4 upwards thrusters should all run in the same direction. If they do not swap motor wires or change pin assignments/pwm values in code (make sure you update main code as well as the test code).

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

void hoverSpin() {
    //Serial.println("hover spin");
    servo2.writeMicroseconds(forward);
    servo3.writeMicroseconds(forward);
    servo6.writeMicroseconds(forward+25);
    servo7.writeMicroseconds(reverse-25);
    servo8.writeMicroseconds(reverse-25);
    servo9.writeMicroseconds(forward+25);
    delay(1000);
}

void hoverForward() {
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

//----------------------------------------------------------------------------------------------------------------------------------------------//