void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(A0,INPUT_PULLUP);
  pinMode(A1,INPUT_PULLUP);
  pinMode(7,INPUT_PULLUP);
  pinMode(10,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.write('s');
  Serial.write('t');
  Serial.write('r');
  Serial.write('t');
  Serial.write(digitalRead(7));
  Serial.write(digitalRead(10));
  Serial.write(analogRead(A0)>>2);
  Serial.write(analogRead(A1)>>2);
  Serial.write('e');
  Serial.write('n');
  Serial.write('d');
  delay(50);
}