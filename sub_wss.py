# python 3.6

import logging
import random
import time
import json
import ssl
from paho.mqtt import client as mqtt_client
from controlMain import controlMain
import screen_brightness_control as sbc

BROKER = 'cmengineering.org'
PORT = 8883
TOPIC1 = "devc_control_vol"
TOPIC2 = "devc_control_bright"
TOPIC3 = "meeting_yyyy"
# generate client ID with pub prefix randomly
CLIENT_ID = f'python-mqtt-wss-sub-{random.randint(0, 1000)}'
clientCert = './cert/cert.pem'
clientKey = './cert/privkey.pem'

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

FLAG_EXIT = False


def on_connect(client, userdata, flags, rc):
    if rc == 0 and client.is_connected():
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC1)
        client.subscribe(TOPIC2)
        client.subscribe(TOPIC3)
    else:
        print(f'Failed to connect, return code {rc}')


def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            logging.info("Reconnected successfully!")
            return
        except Exception as err:
            logging.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)
    global FLAG_EXIT
    FLAG_EXIT = True


def on_message(client, userdata, msg):
    # print(f'Received `{msg.payload.decode()}` from `{msg.topic}` topic')
    data = json.loads(msg.payload.decode())
    if(msg.topic == TOPIC3):
        controlMain(msg.topic, data['Meeting'])
    else: 
        controlMain(msg.topic,data['value'])

def connect_mqtt():
    client = mqtt_client.Client(protocol=mqtt_client.MQTTv311)
    client.tls_set(certfile = clientCert,keyfile = clientKey,tls_version = ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, keepalive=3)
    client.on_disconnect = on_disconnect
    return client


def run():
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
    client = connect_mqtt()
    client.loop_forever()


if __name__ == '__main__':
    run()
