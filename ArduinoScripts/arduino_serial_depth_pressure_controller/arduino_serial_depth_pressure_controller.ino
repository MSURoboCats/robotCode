#include <Wire.h>
#include "MS5837.h"

MS5837 sensor;

int startFlag = 1; //false
int killFlag = 1; //false

int forward = 1250;
int testingDelay = 1000;

void setup() {
    Serial.begin(9600);
    Serial.println("arduino starting...");
    Wire.begin();
    
    // Initialize pressure sensor
    // Returns true if initialization was successful
    // We can't continue with the rest of the program unless we can initialize the sensor
    while (!sensor.init()) {
      Serial.println("Blue Robotics Bar02: Init failed");
      sensor.setFluidDensity(1.225); // kg/m^3 (1.225 air, 997 freshwater, 1029 for seawater)
    }
}

void loop() {
    if(Serial.available() > 0) {
      String incomingString = Serial.readStringUntil('\n');
      Serial.print("received: ");
      Serial.println(incomingString);
      if(killFlag == 0) {
        Serial.println("status: killed");
        return;
      } else if(incomingString == "start" && startFlag == 1){
        startFlag = 0;
        Serial.println("arduino ready");
      } else if (startFlag == 0){
        if (incomingString == "kill") {
          killFlag = 0;
          Serial.println("Uno Halted: Power Cycle to restart");
          Serial.println("status: killed");
          return;
        } else if(incomingString == "pressure"){
          Serial.println(sensor.pressure());
        } else if (incomingString == "temp") {
          Serial.println(sensor.temperature());
        } else if (incomingString == "altitude") {
          Serial.println(sensor.altitude());
        } else if (incomingString == "depth") {
          Serial.println(sensor.depth());
        } else if (incomingString == "measures") {
          Serial.print(“pressure: “ + sensor.pressure() + “, depth: “ + sensor.depth() + “, altitude: “ + sensor.altitude() + “, temp: “ + sensor.temperature());
        } else {
          Serial.println("command not recognized");
        }
        Serial.println("status: done");
      } else {
          Serial.println("arduino not started");
      }
    }
}
