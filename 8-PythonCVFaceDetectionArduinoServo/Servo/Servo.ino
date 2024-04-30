#include "cvzone.h"
#include "Servo.h"

Servo servo;
SerialData data(1,3);
int value[1];

void setup () {
  data.begin(9600);
  servo.attach(5);
}

void loop () {
  data.Get(value);
  servo.write(value[0]);
  
  delay(30);
}