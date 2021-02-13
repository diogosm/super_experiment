from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import time
from datetime import datetime

string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1301242"
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "TL7LVPPDXRXOFGXG"
# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"
# You can use any username.
mqttUsername = "mwa0000021483824"
# Your MQTT API key from Account > My Profile.
mqttAPIKey = "MVALKEH208WOKAHE"

tTransport = "websockets"
tPort = 80
# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

cont = 0
while(cont<5):
    clientID = ''
    cont += 1

    for x in range(1,16):
        clientID += random.choice(string.alphanum)

    # get data
    date = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    ph   = round(random.uniform(1,15),2)
    temp = round(random.uniform(0,45),2)
    aux  = [random.choice(string.alphanum) for i in range(10)]
    text = ""
    for c in aux:
        text += c

    ## monta o payload
    payload = "field1=" + str(date) + \
        "&field2=" + str(ph) + \
        "&field3=" + str(temp) + \
        "&field4=" + str(text)

    try:
        publish.single(topic, 
                       payload,
                       hostname=mqttHost,
                       transport=tTransport,
                       port=tPort,
                       auth={'username':mqttUsername,'password':mqttAPIKey}
                      )
        print(cont, "# sending data...")
    except Exception as e:
        print ("error: ", e)
        
    time.sleep(30)