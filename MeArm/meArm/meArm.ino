#include <Servo.h>
// AndrewPythonArduino：
// http://andrewpythonarduino.blogspot.tw/
Servo  myservo1; //底部伺服馬達
Servo  myservo2; //左側伺服馬達(四邊形側板為左側)
Servo  myservo3; //右側伺服馬達(五邊形側板為右側)
Servo  myservo4; //爪子的伺服馬達

const int VERT1 = A1;   // 搖桿1垂直(左邊)
const int HORIZ1 = A2;  // 搖桿1水平
const int VERT2 = A3;   // 搖桿2垂直(右邊)
const int HORIZ2 = A4;  // 搖桿2水平

int offset = 15;
int servoVal1 = 90-offset;
int servoVal2 = 90;
int servoVal3 = 60;     // 退到後面
int servoVal4 = 0;      // 爪子全開

void setup()
{
  myservo1.attach(9);         // 連結pin9到底部伺服馬達
  myservo1.write(servoVal1);  // 一開始先置中90度
  myservo2.attach(10);        // 連結pin10到左側伺服馬達
  myservo2.write(servoVal2);  // 一開始先置中90度
  myservo3.attach(11);        // 連結pin11到右側伺服馬達
  myservo3.write(servoVal3);  // 一開始退到後面，30度
  myservo4.attach(6);         // 連結pin6到爪子的伺服馬達
  myservo4.write(servoVal4);  // 一開始鉗爪全開，0度
  delay(3000);

  Serial.begin(9600);
}

void loop() 
{
  int L_R, U_D, F_B, O_C;
  // 從搖桿讀取數值
  U_D = analogRead(VERT1);        // will be 0-1023 控制上下
  L_R = analogRead(HORIZ1);       // will be 0-1023 左右轉
  F_B = analogRead(VERT2);        // will be 0-1023 控制前後
  O_C = analogRead(HORIZ2);       // will be 0-1023 控制開合
           
  servoVal1 = map(L_R, 0, 1023, 20, 140); //右=0, 左=1023，向右調整 20 度
  myservo1.write(servoVal1);

  servoVal2 = map(U_D, 0, 1023, 50, 130); //下=0, 上=1023
  myservo2.write(servoVal2);

  servoVal3 = map(F_B, 0, 1023, 40, 140); //下=0, 上=1023
  myservo3.write(servoVal3);

  servoVal4 = map(O_C, 0, 1023, 0, 90);   //右=0, 左=1023
  myservo4.write(servoVal4);
   
  Serial.print("L_R: ");
  Serial.print(L_R);
  Serial.print(" U_D: ");
  Serial.print(U_D);
  Serial.print(" F_B: ");
  Serial.print(F_B);
  Serial.print(" O_C: ");
  Serial.println(O_C);
} 

