#include <Servo.h>

Servo doorServo;
const int buzzerPin = 10;
const int servoPin = 9;
bool doorOpen = false;

void setup() {
  Serial.begin(9600);
  doorServo.attach(servoPin);
  pinMode(buzzerPin, OUTPUT);
  doorServo.write(0);  // Puerta cerrada inicialmente
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'O') {  // Abrir puerta
      doorServo.write(90);
      tone(buzzerPin, 1000, 200);  // Beep corto
      delay(2000);
      doorServo.write(0);
    } 
    else if (command == 'A') {  // Alarma
      for (int i = 0; i < 3; i++) {
        tone(buzzerPin, 1500, 500);
        delay(500);
      }
    }
  }
}