
#include "Impellor.h"

Impellor imp(1, 1500, 1550, 1600, false);


void setup() {
  // put your setup code here, to run once:
  
  imp.set(0.5);
  imp.setNeutral();
  Serial.println(imp.get());
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
