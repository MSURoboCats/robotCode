#pragma once
#include <Arduino.h>
#include <Servo.h>


class Impellor
{

private:

  // how to run the impellor

  // these represent the min middle(neutral)and max values for the PWM signal.
  // which correspond to full reverse, neutral, and full forward respectively.
  //
  // Technically speaking neutral is redundant because it should just be the
  // average of min and max but having a distinct value makes it harder to 
  // accidently make impellors that don't know how to stop moving. 
  //
  // Additionally, set(); is setup to be able to scale properly even
  // if the min or max is farthur from neutral than the other extrema. So you 
  // could configure the motor to have a faster speed in reverse vs forward etc.
  int m_minPWM;
  int m_maxPWM;
  int m_neutralPWM; // the no power value of the motor

  // easy var to flip direction of motor in config
  bool m_direction;

  // ref to arduino servo to interact with impellor
  Servo m_servo; 

  // [-1, 1] range value to represent speed between the\
  // min and max pwm signal configs.
  float m_speed;

  // the speed in terms of pwm signal
  int m_PWMSpeed;

public:
  // constructor!
  // @param pin the pin of the impellor
  // @param minPWM the minimum PWM signal (max speed one way)
  // @param neutralPWM the neutral PWM signal. (not moving) 
  // @param maxPWM the maximum PWM signal (max speed the other way)
  // @param direction if true then the more positive the speed the closer
  //                  to the max PWM. if false the more positive the speed
  //                  the closer to minPWM.
  Impellor(int pin, int minPWM, int neutralPWM, int maxPWM, bool direction);

  // sets the impellor speed
  // @param speed a -1 to 1 input for motor speed.
  void set(float speed);

  // get the impellor speed
  // @return the speed in decimal format
  float get(void);

  // just sets everything to not move
  void setNeutral(void);
};
