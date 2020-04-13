
#include "DHT.h"
DHT dht;
void setup() 
{
    Serial.begin(9600); 
    dht.setup(2);
}

void loop() 
{   

    float humidity = dht.getHumidity();
    float temperature = dht.getTemperature();
    if(humidity>=0){
      Serial.print("{\"Humidity\":"); 
      Serial.print(humidity, 1);
      Serial.print(",\"Temperature\":"); 
      Serial.print(temperature, 1);
      Serial.println("}");// Irms
    }
    delay(1000);
}
