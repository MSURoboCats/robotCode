#include "Impellor.h"
#include <Arduino.h>
#include <Servo.h>



//////////////////////////////////////////////////////
Impellor::Impellor(int pin, int minPWM, int neutralPWM, int maxPWM, bool direction = true)
{

  // sanity check that our config goes min < neutral < max.
  if (!(minPWM < neutralPWM && neutralPWM < maxPWM))
  {
    Serial.print("Impellor Config Error. Failed to pass min < neutral < max for impellor at pin ");
    Serial.print(pin);
    Serial.println(".");
  }

  
  // config servo
  m_servo.attach(pin);

  // save config for motor
  m_minPWM = minPWM;
  m_maxPWM = maxPWM;
  m_direction = direction;

  m_neutralPWM = neutralPWM;

}

//////////////////////////////////////////////////////
void Impellor::set(float speed)
{
  m_speed = max(min(speed, 1), -1); // clamp speed to -1 to 1

  float temp = m_speed;
  
  // if motor output is flipped flip 
  if (!m_direction)
    temp * -1;


  if (temp > 0) // scale speed by space between neutral and max
  {
    m_PWMSpeed = m_neutralPWM + temp * (m_maxPWM - m_neutralPWM);
  }
  else if(temp < 0) // scale speed by space between neutral and min
  {
     m_PWMSpeed = m_neutralPWM + temp * (m_neutralPWM - m_minPWM);
  }
  else
  {
    m_PWMSpeed = m_neutralPWM;
  }
  

  // apply servo power
  m_servo.writeMicroseconds(m_PWMSpeed);
}

//////////////////////////////////////////////////////
void Impellor::setNeutral(void)
{
  // set speed as if we are zero.
  m_speed = 0;
  m_PWMSpeed = m_neutralPWM;

  // apply servo power
  m_servo.writeMicroseconds(m_PWMSpeed);
  
}

//////////////////////////////////////////////////////
float Impellor::get(void)
{
  return m_speed;
}
