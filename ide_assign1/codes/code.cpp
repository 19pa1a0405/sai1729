#include <Arduino.h>
#include <Wire.h>
int X=2,Y=3,Z=4,W=5;
int F=8;

void setup()
{
   pinMode(2, INPUT);
   pinMode(3, INPUT);
   pinMode(4, INPUT);
   pinMode(5, INPUT);
   pinMode(8, OUTPUT);
}
void loop()
{
   X=digitalRead(2);
   Y=digitalRead(3);
   Z=digitalRead(4);
   W=digitalRead(5);
   F=((!X&&!Z)||(!Y&&!Z)||(!X&&Y)||(X&&Z&&W));
   digitalWrite(8,F);
}
