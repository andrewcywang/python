#include <SoftwareSerial.h>
#include <dht11.h>
dht11 DHT11;
#define DHTPIN 7
#define LMPIN 0
#define SSID "HuskyStudio24" 
#define PASSWD "29445030"
#define IP "184.106.153.149"     //thingspeak.com

SoftwareSerial ESP8266(3,2);      //RX, TX
const int WIFIled=13;
boolean FAIL_8266 = false;
String cmd;
int i;
unsigned long realtime=0;
float lastT=0;
float lastH=0;

void setup() 
{ 
  pinMode(WIFIled,OUTPUT); 
  digitalWrite(WIFIled,LOW);   
  ESP8266.begin(9600);
  Serial.begin(9600);         //把訊息顯示在 Serial
  for(i=0;i<3;i++)
  {  
    digitalWrite(WIFIled,HIGH);
    delay(200);
    digitalWrite(WIFIled,LOW);
    delay(200);
  }
  do
  { 
    sendESP8266cmd("AT+RST",2000);
    Serial.println("reset 8266...");    
    if(ESP8266.find("OK"))
    {
      Serial.println("OK");
      if(connectWiFi(10))           //連線AP
      {
        FAIL_8266=false;
        Serial.println("connect success");
      }  
      else
      {
        FAIL_8266=true;
        Serial.println("connect fail");
      }  
    }
    else
    {
      delay(500);
      FAIL_8266=true;
      Serial.println("no response");
    }      
  }while(FAIL_8266);  
  digitalWrite(WIFIled,HIGH);
}
void loop()
{
  if((millis()-realtime)>=30000)    //兩分鐘 Update一次
  {
    realtime=millis();
    if(!FAIL_8266)
    {  
      float x,x1,x2,y,z,z1;
      int n;
      n = analogRead(LMPIN);
      x = 500.0 * n /1024.0;
      int chk = DHT11.read(DHTPIN);
      x1 = DHT11.temperature;
      z1 = DHT11.humidity;
      x2 = x;
      x -= 4;
      Serial.println(x);
      if(abs(x-x1)>1) {
        x = x1;
      }
      if(lastT == 0){
        y = (x * 0.4 + x1 * 0.6);
      } else {
        y = (lastT * 0.4 + x * 0.3 + x1 * 0.3);
      }
      lastT = y;
      if(lastH == 0){
        z = z1;
      } else {
        z = lastH * 0.4 + z1 * 0.6;
      }
      lastH = z;
      updateDHT(String(y,2),String(z,2),String(x1),String(x2,2));
    }      
  }
}
void updateDHT(String T,String H,String T1,String T2)
{
  String cmd="AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  sendESP8266cmd(cmd,2000);
  if(ESP8266.find("OK"))
  {
    Serial.println("TCP OK"); 
    cmd="GET /update?api_key=MSFPC7MCUNU9K2KN"; 
    cmd+="&field1=" + T + "&field2=" + H + "&field3=" + T1 + "&field4=" + T2 + "\r\n";
    ESP8266.print("AT+CIPSEND=");
    ESP8266.println(cmd.length());
    if(ESP8266.find(">"))
    {
      ESP8266.print(cmd);
      Serial.println(cmd);      //把命令顯示出來
      if(ESP8266.find("OK"))
      {
        Serial.println("update OK");
      }
      else
      {
        Serial.println("update error");        
      }
    }
  }
  else
  {
    cmd="field1=" + T + "&field2=" + H + "&field3=" + T1 + "&field4=" + T2 + "\r\n";
    Serial.println(cmd);      //把字串顯示出來
    Serial.println("TCP error"); 
    sendESP8266cmd("AT+CIPCLOSE",1000);      
  }  
}
boolean connectWiFi(int timeout)
{
  sendESP8266cmd("AT+CWMODE=1",2000);                //Set station MODE  
  Serial.println("WiFi mode:STA");      
  do
  {   
    String cmd="AT+CWJAP=\"";
    cmd+=SSID;
    cmd+="\",\"";
    cmd+=PASSWD;
    cmd+="\"";   
    sendESP8266cmd(cmd,1000);
    Serial.println("join AP..."); 
    if(ESP8266.find("OK"))
    { 
      Serial.println("OK");
      sendESP8266cmd("AT+CIPMUX=0",1000);               
      return true;
    }
  }while((timeout--)>0); 
  return false; 
} 
void sendESP8266cmd(String cmd, int waitTime)
{
  Serial.println(cmd);
  ESP8266.println(cmd);
  delay(waitTime);
}

