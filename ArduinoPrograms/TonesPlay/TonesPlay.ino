int speakerPin = 10;
// 依照數字簡譜1-7，高音1用8代替，0代表休止符
// 每個音階的拍子，寫在一起方便對照
int notes[] = {1,1,5,5,6,6,5,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,5,5,6,6,5,4,4,3,3,2,2,1,0};
int beats[] = {1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,8}; 
// 利用 sizeof()，算出總共要多少音符
int length = sizeof(notes)/sizeof(notes[0]); 
// 決定一拍多長，這邊一拍 300 ms
int tempo = 300;

void setup() {
  pinMode(speakerPin, OUTPUT);
  pinMode(2,OUTPUT);  //燈號Do
  pinMode(3,OUTPUT);  //燈號Re
  pinMode(4,OUTPUT);  //燈號Mi
  pinMode(5,OUTPUT);  //燈號Fa
  pinMode(6,OUTPUT);  //燈號So
  pinMode(7,OUTPUT);  //燈號La
  pinMode(8,OUTPUT);  //燈號Si
  pinMode(9,OUTPUT);  //燈號Do
}

void loop() {
  // 利用 for 來播放我們設定的歌曲，一個音一個音撥放
  for (int i = 0; i < length; i++) {
    // 如果是0的話，不撥放音樂
    if (notes[i] == 0) {
      delay(beats[i] * tempo); // rest
    } else {
      // 呼叫 palyNote() 這個 function，將音符轉換成訊號讓蜂鳴器發聲
      playNote(speakerPin,notes[i], beats[i] * tempo);
    } 
    // 讓每個音符之間停頓一下
    delay(tempo/10); 
  }
}

void playNote(int OutputPin, int note, int duration) {
   // 音符字元與對應的頻率由兩個矩陣表示
  int names[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
  int tones[] = { 261, 294, 330, 349, 392, 440, 494, 523 };
  int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
  // 播放音符對應的頻率
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      tone(OutputPin,tones[i], duration);
      //讓燈號亮起來
      digitalWrite(leds[i], HIGH);
      //下方的 delay() 及 noTone ()，一定要有這兩行
      delay(duration);
      noTone(OutputPin);
      digitalWrite(leds[i], LOW);
    }
  }
}
