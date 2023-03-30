int ledPin = 9;

int ledValue = 0;
char data;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    //read incoming byte
    data = Serial.read();
    Serial.print(data);
  }

  if (data == '1') {
    digitalWrite(ledPin, HIGH);
  } else if (data == '0') {
    digitalWrite(ledPin, LOW);
  }
}

