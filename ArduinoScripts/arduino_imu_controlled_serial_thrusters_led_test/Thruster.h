#include <Servo.h>

class Thruster{

  private:

    int m_minPWM;
    int m_maxPWM;
    int m_neutralPWM;

    bool m_direction;

    Servo m_servo;
    int m_pin;

    float m_speed;

    int m_current_pwm;
    float m_current_speed_percentage;

    int m_led_pin;
    bool m_led_state;

    void updateLED(void);
    void attachLED(void);

  public:

    Thruster(int pin, int minPWM, int maxPWM, int neutralPWM, bool direction);

    void setThrusterSpeed(float speed_percentatge);

    float getThrusterSpeed(void);

    void setNeutral(void);

    void kill(void);
};
