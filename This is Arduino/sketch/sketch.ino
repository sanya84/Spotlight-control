#include <SoftwareSerial.h>

// Правильно: SoftwareSerial(RX_пин, TX_пин)
// RX_пин = 10 (принимает от RO)
// TX_пин = 11 (передает к DI)
// Пин 10 (RX) ← RO (RS485) ← RS485 передаёт ← Arduino принимает (зелёный)
// Пин 11 (TX) → DI (RS485) → Arduino передаёт → RS485 принимает (оранжевый)
SoftwareSerial RS485_Serial(10, 11);

// DE and RE pins (RS485 module) to pin 8 arduino digital
const int RS485_DE_RE_PIN = 8;

// Relay control pin to pin 6 arduino digital
const int RELAY_CONTROL_PIN = 6;

class State 
{
public:
    void send_state() 
    {
      // 1. Считываем состояние пина 6 и сохраняем его в переменную
      int pinState = digitalRead(6); 

      // 2. Проверяем считанное состояние
      if (pinState == HIGH) {
        // Выполняем действия, если пин в состоянии HIGH
        // Serial.println("Пин 7: HIGH"); 
        RS485_Serial.println("1");
        // Ждем окончания передачи
        delayMicroseconds(50); // правильно
      } else {
        // Выполняем действия, если пин в состоянии LOW
        // Serial.println("Пин 7: LOW");
        RS485_Serial.println("0");
      }
    }
};


class Control 
{
public:
    void handler_command(String command) 
    {
      // Настраиваем пин для управления реле  (Relay)
      pinMode(RELAY_CONTROL_PIN, INPUT);
      // Считываем состояние пина 6 и сохраняем его в переменную
      int pinState = digitalRead(6);

      // Проверяем считанное состояние
      if (command == "1") {
        Serial.println("command  == 1");
        // Настраиваем пин для управления реле  (Relay)
        pinMode(RELAY_CONTROL_PIN, OUTPUT);
        digitalWrite(RELAY_CONTROL_PIN, HIGH);
        delayMicroseconds(50); // правильно
      }

     // Проверяем считанное состояние
      if (command == "0") {
        Serial.println("command  == 0");
        // Настраиваем пин для управления реле  (Relay)
        pinMode(RELAY_CONTROL_PIN, OUTPUT);
        digitalWrite(RELAY_CONTROL_PIN, LOW);
        delayMicroseconds(50); // правильно
      }
    }
};


void setup() {
  // Инициализируем аппаратный серийный порт для отладки
  Serial.begin(9600);
  
  // Инициализируем программный серийный порт для RS485
  RS485_Serial.begin(9600);

  // Настраиваем пин для управления передачей (DE/RE)
  pinMode(RS485_DE_RE_PIN, OUTPUT);

  // Настраиваем пин для управления реле  (Relay)
  pinMode(RELAY_CONTROL_PIN, INPUT);

  Serial.println("Arduino готов к работе...");

  // Включаем передачу к PC-RS485
  digitalWrite(RS485_DE_RE_PIN, HIGH);
  RS485_Serial.println("Arduino is ready to go...");
  
  // Ждем окончания передачи
  delayMicroseconds(50); // правильно

  // Включаем прием от PC-RS485
  // digitalWrite(RS485_DE_RE_PIN, LOW);
  // Включаем прием от PC-RS485
  digitalWrite(RS485_DE_RE_PIN, HIGH);
  // Ждем окончания передачи
  delayMicroseconds(50); // правильно
}

State state;
Control control;

void loop() {
  // Читаем данные, пришедшие от PC-RS485
  if (RS485_Serial.available()) {
    Serial.println("Доступны данные для чтения...");
    String command = RS485_Serial.readString();
    Serial.println("Получена команда от PC-RS485: " + command);
    control.handler_command(command);
  }

  digitalWrite(RS485_DE_RE_PIN, HIGH);
  state.send_state();
  digitalWrite(RS485_DE_RE_PIN, LOW);
  delay(150); // правильно
}
