#include <SoftwareSerial.h>
SoftwareSerial ESP8266(3,2); // RX, TX
void setup()
{
  Serial.begin(9600);
  ESP8266.begin(9600);
}
void loop() 
{
  if(ESP8266.available())
    Serial.write(ESP8266.read()); 
  else if(Serial.available())
    ESP8266.write(Serial.read());    
}   
