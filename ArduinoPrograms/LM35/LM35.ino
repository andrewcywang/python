void setup() 
{
  Serial.begin(9600); 
}

void loop()
{
  float x;
  int n;
  n = analogRead(0);
  x = 500.0 * n /1024.0;
  Serial.print(x, 4);
  Serial.print("\t"); 
  Serial.print(n*1000, 5);
  Serial.print("\n"); 
  delay(5000);
}
