#include <Wire.h>  // Arduino IDE 內建
// LCD I2C Library，從這裡可以下載：
// https://bitbucket.org/fmalpartida/new-liquidcrystal/downloads
#include <LiquidCrystal_I2C.h>

// Set the pins on the I2C chip used for LCD connections:
//                    addr, en,rw,rs,d4,d5,d6,d7,bl,blpol
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // 設定 LCD I2C 位址
#include <LiquidCrystal.h>

// 建立 LiquidCrystal 的變數 lcd
//                 LCD 接腳:  rs, enable, d4, d5, d6, d7 
//      對應到 Arduino 接腳:  12,     11,  5,  4,  3,  2

LiquidCrystal lcd2(12, 11, 5, 4, 3, 2);
void setup() {
  lcd2.begin(16, 2);
 
  // 列印 "Hello World" 訊息到 LCD 上
  lcd2.print("Hello, World! Again!");
  
  Serial.begin(115200);  // 用於手動輸入文字
  lcd.begin(16, 2);      // 初始化 LCD，一行 16 的字元，共 2 行，預設開啟背光

  // 閃爍三次
  for(int i = 0; i < 3; i++) {
    lcd.backlight(); // 開啟背光
    delay(250);
    lcd.noBacklight(); // 關閉背光
    delay(250);
  }
  lcd.backlight();

  // 輸出初始化文字
  lcd.setCursor(0, 0); // 設定游標位置在第一行行首
  lcd.print("Hello, world!");
  delay(1000);
  lcd.setCursor(0, 1); // 設定游標位置在第二行行首
  lcd.print("Andrew Wang");
  delay(8000);

  // 告知使用者可以開始手動輸入訊息
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Use Serial Mon");
  lcd.setCursor(0, 1);
  lcd.print("Type to display");
}

void loop() {
  lcd2.setCursor(0, 1);
 
  // 列印 Arduino 重開之後經過的秒數
  lcd2.print(millis()/1000);
  
  // 當使用者手動輸入訊息
  if (Serial.available()) {
    // 等待一小段時間，確認資料都接收下來了
    delay(100);
    // 清除舊訊息
    lcd.clear();
    // 讀取新訊息
    while (Serial.available() > 0) {
      // 將訊息顯示在 LCD 上
      lcd.write(Serial.read());
    }
  }
}
