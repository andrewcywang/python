int photocellPin = 2;   //定义变量 photocellsh=2，为电压读取端口。
int ledPin = 12;    //定义变量 ledPin=12，为 led 电平输出端口
int val = 0;      //定义 val 变量的起始值


void setup() {
  pinMode(ledPin, OUTPUT); //使 ledPin 为输出模式
}

void loop() {
  val = analogRead(photocellPin); //从传感器读取值
  if(val<=512){
    //512=2.5V，想让传感器敏感一些的时候，把数值调高，想让传感器迟钝的时候把数值调低。
    digitalWrite(ledPin, HIGH); //当 val 小于 512(2.5V)的时候，led 亮。
  }
  else{
    digitalWrite(ledPin, LOW);
  }
}
