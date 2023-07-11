#!/usr/bin/python

import paho.mqtt.client as mqtt
import ssl

host = 'cmengineering.org'
port = 8883

clientCert = './cert/cert.pem'
clientKey = './cert/privkey.pem'

#Edit the topic and message for your target
topic = "devc_control_vol"
message = '{"Meeting": "Start", "value" : 1}'

def on_connect(client, userdata, flags, respons_code):
    print('connected. status {0}'.format(respons_code))
    client.publish(topic, message)
    print(f"sent message topic={topic} message={message}")
def on_publish(client, userdata, mid):
    client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.tls_set(
        certfile = clientCert,
        keyfile = clientKey,
        tls_version = ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)

    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(host, port=port, keepalive=60)
    client.loop_forever()
