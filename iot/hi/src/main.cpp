//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "sai1729" // Add your network credentials
#define STAPSK  "sai1792r"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

int X=2,Y=3,Z=4,W=5;
int F=8;

void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

void setup(){
  OTAsetup();


	   pinMode(2, INPUT);
	   pinMode(3, INPUT);
	   pinMode(4, INPUT);
           pinMode(5, INPUT);
	   pinMode(8, OUTPUT);
  //-------------------//
  // Custom setup code //
  //-------------------//
}

void loop() {
  OTAloop();
  delay(10);  // If no custom loop code ensure to have a delay in loop
  //-------------------//
  // Custom loop code  //
  //-------------------//
  
  X=digitalRead(2);
	   Y=digitalRead(3);
	   Z=digitalRead(4);
           W=digitalRead(5);
           F=((!X&&!Z)||(!Y&&!Z)||(!X&&Y)||(X&&Z&&W));
	   digitalWrite(8,F);
}
}
