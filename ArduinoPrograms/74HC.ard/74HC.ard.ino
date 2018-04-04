const byte dataPin = 2;     // 74HC595序列腳接數位2
const byte latchPin = 3;    // 74HC595暫存器時脈腳接數位3
const byte clockPin = 4;    // 74HC595序列時脈腳接數位4
byte index = 0;             // 七段顯示器的數字索引
const byte LEDs[10] = {
           B01111110,
           B00110000,
           B01101101,
           B01111001,
           B00110011,
           B01011011,
           B01011111,
           B01110000,
           B01111111,
           B01111011,
} ;  

void setup() {
  // put your setup code here, to run once:
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, LEDs[index]);
  digitalWrite(latchPin, HIGH);
  delay(500);
  index ++;
  if(index == 10){
    index = 0;
  }
}
