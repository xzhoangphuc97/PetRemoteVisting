#!/usr/bin/python

import paho.mqtt.client as mqtt
import ssl

host = 'cmengineering.org'
port = 8883

clientCert = './cert/cert.pem'
clientKey = './cert/privkey.pem'

#Edit the topic for your target
topic = 'connect'

def on_connect(client, userdata, flags, respons_code):
    print('connected. status {0}'.format(respons_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"topic:[{msg.topic}] payload:[{str(msg.payload)}]",flush=True)

if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.tls_set(
        certfile = clientCert,
        keyfile = clientKey,
        tls_version = ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)
    client.loop_forever()

