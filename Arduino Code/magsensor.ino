#include <Wire.h>
#include <MechaQMC5883.h>
#include <Stepper.h>

#define STEPS_PER_REVOLUTION 200 // Step motorunun her devirdeki adım sayısı
#define IN1_PIN 8
#define IN2_PIN 9
#define IN3_PIN 10
#define IN4_PIN 11


MechaQMC5883 qmc;
Stepper stepper(STEPS_PER_REVOLUTION, IN1_PIN, IN3_PIN, IN2_PIN, IN4_PIN); // Stepper nesnesini oluştur


float RateRoll, RatePitch, RateYaw;
float AccX, AccY, AccZ;
float AngleRoll, AnglePitch;
float LoopTimer;
void gyro_signals(void) {
  Wire.beginTransmission(0x68);
  Wire.write(0x1A);
  Wire.write(0x05);
  Wire.endTransmission();
  Wire.beginTransmission(0x68);
  Wire.write(0x1C);
  Wire.write(0x10);
  Wire.endTransmission();
  Wire.beginTransmission(0x68);
  Wire.write(0x3B);
  Wire.endTransmission(); 
  Wire.requestFrom(0x68,6);
  int16_t AccXLSB = Wire.read() << 8 | Wire.read();
  int16_t AccYLSB = Wire.read() << 8 | Wire.read();
  int16_t AccZLSB = Wire.read() << 8 | Wire.read();
  Wire.beginTransmission(0x68);
  Wire.write(0x1B); 
  Wire.write(0x8);
  Wire.endTransmission();                                                   
  Wire.beginTransmission(0x68);
  Wire.write(0x43);
  Wire.endTransmission();
  Wire.requestFrom(0x68,6);
  int16_t GyroX=Wire.read()<<8 | Wire.read();
  int16_t GyroY=Wire.read()<<8 | Wire.read();
  int16_t GyroZ=Wire.read()<<8 | Wire.read();
  RateRoll=(float)GyroX/65.5;
  RatePitch=(float)GyroY/65.5;
  RateYaw=(float)GyroZ/65.5;
  AccX=(float)AccXLSB/4096;
  AccY=(float)AccYLSB/4096;
  AccZ=(float)AccZLSB/4096;
  AngleRoll=atan(AccY/sqrt(AccX*AccX+AccZ*AccZ))*1/(3.142/180);
  AnglePitch=-atan(AccX/sqrt(AccY*AccY+AccZ*AccZ))*1/(3.142/180);
}


int startX;
int lastXDegrees = 0;
unsigned long previousMillis = 0;
const long interval = 100; // Okuma aralığı (milisaniye cinsinden)

void setup() 
{
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  Wire.setClock(400000);
  Wire.begin();
  Wire.beginTransmission(0x68);
  delay(250);
  Wire.write(0x6B);
  Wire.write(0x00);
  Wire.endTransmission();
  qmc.init();
  Serial.begin(115200); 
  int x, y, z, azimuth;
  qmc.read(&x, &y, &z, &azimuth);
  startX = x; // Başlangıç pozisyonunu al

  stepper.setSpeed(5); // Stepper motorun hızını ayarla (rpm cinsinden)
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    // Belirlenen aralıkta manyetometre okuması yap
    previousMillis = currentMillis;

    gyro_signals();

    int x, y, z, azimuth;
    qmc.read(&x, &y, &z, &azimuth);
    
    // Başlangıç noktasından itibaren açıyı hesapla
    int xDegrees = map(x - startX, -2048, 2047, -180, 180); // Manyetometrenin çıkışını dereceye dönüştürme

    Serial.print(xDegrees);
    Serial.print(",");
    Serial.println(AccX);

    // Eğer manyetometre verisinde bir değişiklik varsa, hareket ettir
    if (xDegrees != lastXDegrees) {
      int degreeDifference = lastXDegrees - xDegrees; // Önceki derece ile şimdiki derece arasındaki farkı hesapla
      int stepsToMove = degreeDifference * STEPS_PER_REVOLUTION / 90; // 1 derece dönme için gerekli adım sayısı
      stepper.step(stepsToMove); // Step motorunu döndür
      lastXDegrees = xDegrees; // Son dereceyi güncelle
    }
  }
  
}