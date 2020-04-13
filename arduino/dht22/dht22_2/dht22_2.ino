#include "DHT.h"

DHT dht;

void setup()
{
  Serial.begin(9600);

  dht.setup(2); // data pin 2
}

void loop()
{
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();
  if(dht.getStatusString() == "OK"){
    Serial.print("{\"Humidity\":"); 
    Serial.print(humidity, 1);
    Serial.print(",\"Temperature\":");
    Serial.print(temperature, 1);
    Serial.print("}\n");
  }
  else{
    Serial.print("sensor error");
  }
  delay(1000);
  
}
