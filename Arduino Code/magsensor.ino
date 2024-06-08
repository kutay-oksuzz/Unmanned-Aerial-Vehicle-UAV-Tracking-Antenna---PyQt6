
#include <Wire.h>

#define HMC5883_ADDRESS 0x1E // 0011110b, HMC5883'ün I2C 7 bit adresi

const int x_offset = 30;
const int y_offset = 128;

// TB6600 Pin Bağlantıları
#define STEP_PIN 3
#define DIR_PIN 2

int motorStepDelay = 1000; // Motor adım gecikmesi (mikrosaniye)
String receivedData = ""; // Python'dan gelen veriyi saklamak için
char incomingData[50]; // Gelen veriyi saklamak için bir dizi
int dataIndex = 0; // Dizideki mevcut indeks

void setup() {
  Serial.begin(115200); // Seri iletişimi başlat
  Wire.begin(); // I2C iletişimini başlat

  // HMC5883 IC'yi doğru çalışma moduna ayarla
  Wire.beginTransmission(HMC5883_ADDRESS); // HMC5883 ile iletişimi başlat
  Wire.write(0x02); // mod register'ı seç
  Wire.write(0x00); // sürekli ölçüm modu
  Wire.endTransmission();
  delay(300); // Sensörün başlaması için kısa bir gecikme

  // TB6600 Pinlerini çıkış olarak ayarla
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
}

void loop() {
  // HMC5883'den veri oku
  int x, y, z; // üç eksen verisi
  double currentAngle;
  Wire.beginTransmission(HMC5883_ADDRESS);
  Wire.write(0x03); // 3. register'ı seç, X MSB register'ı
  Wire.endTransmission();
  Wire.requestFrom(HMC5883_ADDRESS, 6);

  if (6 <= Wire.available()) {
    x = Wire.read() << 8 | Wire.read();
    z = Wire.read() << 8 | Wire.read();
    y = Wire.read() << 8 | Wire.read();
  }

  currentAngle = atan2(y + y_offset, x + x_offset) * (180 / 3.141592654);
  if (currentAngle < 0) {
    currentAngle += 360;
  }

  // Mevcut açıyı seri porta yazdır
  Serial.print("Current Angle: ");
  Serial.println(currentAngle);

  // Python'dan gelen veriyi oku
  while (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte == '\n') {
      incomingData[dataIndex] = '\0'; // Diziyi sonlandır
      receivedData = String(incomingData); // Diziyi String'e dönüştür
      processReceivedData(currentAngle); // Veriyi işle
      dataIndex = 0; // Diziyi sıfırla
    } else {
      incomingData[dataIndex++] = incomingByte; // Gelen karakteri diziye ekle
      if (dataIndex >= 50) { // Dizi sınırını kontrol et
        dataIndex = 0; // Sınır aşılırsa sıfırla
      }
    }
  }
  delay(1000); // Her saniyede bir okuma ve gönderme
}

void processReceivedData(double currentAngle) {
  if (receivedData.startsWith("H:")) {
    float targetAngle = receivedData.substring(2).toFloat();
    Serial.print("Target Angle: ");
    Serial.println(targetAngle);
    adjustMotorToTargetAngle(currentAngle, targetAngle);
  } else if (receivedData.startsWith("V:")) {
    float targetVerticalAngle = receivedData.substring(2).toFloat();
    Serial.print("Target Vertical Angle: ");
    Serial.println(targetVerticalAngle);
    // Burada dikey motor kontrolü işlemini yapabilirsiniz.
  }
}

void adjustMotorToTargetAngle(double currentAngle, float targetAngle) {
  while (true) {
    // Açı farkını hesapla
    double angleDifference = targetAngle - currentAngle;

    // Açı farkını -180 ile 180 arasına getirmek için
    if (angleDifference > 180) {
      angleDifference -= 360;
    } else if (angleDifference < -180) {
      angleDifference += 360;
    }

    // Tolerans içinde ise döngüden çık
    if (abs(angleDifference) <= 1) {
      break;
    }

    // Yönü belirle
    int direction = (angleDifference > 0) ? -1 : 1;

    // Motoru döndür
    stepMotor(direction);

    // Motorun her adımda mevcut açıya ulaşması için güncel veriyi oku
    int x, y, z;
    Wire.beginTransmission(HMC5883_ADDRESS);
    Wire.write(0x03); // 3. register'ı seç, X MSB register'ı
    Wire.endTransmission();
    Wire.requestFrom(HMC5883_ADDRESS, 6);

    if (6 <= Wire.available()) {
      x = Wire.read() << 8 | Wire.read();
      z = Wire.read() << 8 | Wire.read();
      y = Wire.read() << 8 | Wire.read();
    }

    currentAngle = atan2(y + y_offset, x + x_offset) * (180 / 3.141592654);
    if (currentAngle < 0) {
      currentAngle += 360;
    }

    // Mevcut açıyı seri porta yazdır
    Serial.print("Current Angle: ");
    Serial.println(currentAngle);

    delay(50); // Motorun dönmesi için kısa bir gecikme
  }
  stopMotor();
}

void stepMotor(int direction) {
  digitalWrite(DIR_PIN, direction > 0 ? HIGH : LOW);
  digitalWrite(STEP_PIN, HIGH);
  delayMicroseconds(motorStepDelay);
  digitalWrite(STEP_PIN, LOW);
  delayMicroseconds(motorStepDelay);
}

void stopMotor() {
  // Motoru durdurmak için herhangi bir işlem gerekmiyor, çünkü adımları durdurduğumuzda motor durur.
}
