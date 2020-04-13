
import serial
import time
import paho.mqtt.publish as publish
 
serial = serial.Serial('/dev/ttyUSB0',9600 , timeout = 2)
def readandpub(serial):
    print('read')
    response = serial.readline()
    if response != '':
        publish.single("Sensor/DHT22", payload=response,
                        qos=0, hostname="127.0.0.1", port=1883)
        status = 1
    else:
        status = reconnect(serial)
    return status
def reconnect(serial):
    print('re')
    try:
        serial.close()
        serial.open()
        status = 1
        return status
    except:
        status = 0
        return status




while True:
    try:
        status = readandpub(serial)
        time.sleep(1)
    except:
        status = 0
        while(status == 0):
            status = reconnect(serial)
            print("Arduino is reconnect")
