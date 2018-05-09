#include <Servo.h>

// MeArm範例程式，傑森提供
// 傑森創工，粉絲團：
// https://www.facebook.com/geeksfans/

// 傑森創工露天賣場：
// http://goo.gl/1231oE


Servo  myservo;  //底部伺服馬達
Servo  myservo2; //右側伺服馬達
Servo  myservo3; //左側伺服馬達
Servo  myservo4; //爪子的伺服馬達

const int VERT = A1; // 搖桿1垂直
const int HORIZ = A2; // 搖桿1水平
const int VERT2 = A3; // 搖桿2垂直
const int HORIZ2 = A4; // 搖桿2水平

int servoVal = 90;
int servoVal2 = 90;
int servoVal3 = 90;
int servoVal4 = 120;



void setup()
{
  myservo.attach(9); // 連結pin9到底部伺服馬達
  myservo.write(90); // 一開始先置中90度
  myservo2.attach(10); // 連結pin10到右側伺服馬達
  myservo2.write(90); // 一開始先置中90度
  myservo3.attach(11); // 連結pin11到左側伺服馬達
  myservo3.write(90); // 一開始先置中90度
  myservo4.attach(6); // 連結pin6到爪子的伺服馬達
  myservo4.write(150); // 一開始先置中90度
  delay(3000);

  Serial.begin(9600);
}

void loop() 
{
  int vertical, horizontal,vertical2, horizontal2, select;
  
  // 從搖桿讀取數值
  
  vertical = analogRead(VERT); // will be 0-1023
  horizontal = analogRead(HORIZ); // will be 0-1023
  vertical2 = analogRead(VERT2); // will be 0-1023
  horizontal2 = analogRead(HORIZ2); // will be 0-1023
  
         
  servoVal = map(vertical, 0, 1023, 30, 150); 
  myservo.write(servoVal);

  servoVal2 = map(horizontal, 0, 1023, 60, 120); 
  myservo2.write(servoVal2);

  servoVal3 = map(vertical2, 100, 900, 40, 140); 
  myservo3.write(servoVal3);

  servoVal4 = map(horizontal2, 0, 1023, 70, 150); 
  myservo4.write(servoVal4);
  
  
  Serial.print("vertical: ");
  Serial.print(vertical);
  Serial.print(" horizontal: ");
  Serial.print(horizontal);
  Serial.print("vertical2: ");
  Serial.print(vertical2);
  Serial.print(" horizontal2: ");
  Serial.print(horizontal2);
  Serial.print(" select: ");
  if(select == HIGH)
    Serial.println("not pressed");
  else
    Serial.println("PRESSED!!!!!");
} 
