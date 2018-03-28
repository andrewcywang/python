// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(7,INPUT);
  digitalWrite(7,HIGH);       // 上拉電阻
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(7) == HIGH) {
    digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  } else {                    
    digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  }
}
