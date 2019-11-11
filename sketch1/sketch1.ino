int counter = 1;

void setup(){
  Serial.begin(9600);
}
void loop(){
  if(counter == 1){
    Serial.println("123456789");
    delay(100);
    counter++;
  }
  delay(1000);
  while(Serial.available()){
    delay(30);
    if(counter == 2){
      String print1 = Serial.readStringUntil('\n');
      Serial.println(print1);
      delay(1000);
      counter++;
    }
  }
}
