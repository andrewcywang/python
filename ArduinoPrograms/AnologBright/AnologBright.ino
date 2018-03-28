// Andrew 修改成類比
int bright=0;
int fade=5;
int ledPin=9; //设定控制LED的数字IO脚
void setup()
{
  pinMode(ledPin,OUTPUT);//设定数字IO口的模式，OUTPUT 为输出
}

void loop()
{  
  analogWrite(ledPin,bright);   //bright 一開始是0
  bright += fade;

  if (bright==0 || bright==255) {
    fade = -fade;
  }
  
  delay(30); //设定延时时间，1000 = 1秒
} 
