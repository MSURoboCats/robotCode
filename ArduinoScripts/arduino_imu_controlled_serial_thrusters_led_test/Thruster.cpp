#include "Arduino.h"
#include "Thruster.h"
#include <Servo.h>

Thruster::Thruster(int pin, int minPWM, int maxPWM, int neutralPWM, bool direction = true) {
  
  // sanity check that our config goes min < neutral < max.
  if (!(minPWM < neutralPWM && neutralPWM < maxPWM))
  {
    return;
  }

  m_pin = pin;
  m_servo.attach(m_pin);

  m_minPWM = minPWM;
  m_maxPWM = maxPWM;
  m_neutralPWM = neutralPWM;

  m_servo.writeMicroseconds(m_neutralPWM);

  m_current_pwm = m_neutralPWM;
  m_current_speed_percentage = 0;

  m_led_pin = pin + 20;
  m_led_state = LOW;

  this->attachLED();

}

void Thruster::attachLED(void) {
  pinMode(m_led_pin, OUTPUT);
  digitalWrite(m_led_pin, LOW);
}

void Thruster::updateLED(void) {
  if (m_current_speed_percentage == 0) {
    m_led_state = LOW;
  } else {
    m_led_state = HIGH;
  }
  digitalWrite(m_led_pin, m_led_state);
}

void Thruster::setThrusterSpeed(float speed_percentatge) {
  if (m_direction == false) {
    speed_percentatge = speed_percentatge * -1;
  }
  m_current_speed_percentage = speed_percentatge;
  int microseconds = map(speed_percentatge, -100, 100, m_minPWM, m_maxPWM);
  m_current_pwm = microseconds;
  m_servo.writeMicroseconds(m_current_pwm);
  this->updateLED();
}

float Thruster::getThrusterSpeed(void) {
  return m_current_speed_percentage;
}

void Thruster::setNeutral(void) {
  m_current_pwm = m_neutralPWM;
  m_current_speed_percentage = 0;
  m_servo.writeMicroseconds(m_neutralPWM);
  this->updateLED();
}

void Thruster::kill(void) {
  this->setNeutral();
  m_servo.detach();
}
