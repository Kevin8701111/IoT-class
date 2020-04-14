import paho.mqtt.client as mqtt
import json
# import pymongo
 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
 
# mycol = mydb["sites"]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Sensor/DHT22")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.payload)
    data = json.loads(str(msg.payload.decode('ascii')))
    print(data)
    # print(type(data))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.138", 1883)
client.loop_forever()