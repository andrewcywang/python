// 動手做9-4：製作數位溫濕度顯示器
// 詳細的程式說明，請參閱第九章，9-19頁。

#include <dht11.h>

dht11 DHT11;
const byte dataPin = 7;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int chk = DHT11.read(dataPin);
  Serial.print("Humidity (%): ");
  Serial.println((float)DHT11.humidity, 2);
  Serial.print("Temperature (oC): ");
  Serial.println((float)DHT11.temperature, 2);

  delay(2000);
}
