import paho.mqtt.client as mqtt

USERNAME = "samor"
PASSWORD = "haw"
TOPIC_MECANUM = "mecanum"
TOPIC_MANIPULATOR = "manipulator"
BROKER_ADDRESS = "192.168.0.1"
PORT = 1883
QOS = 1

client = mqtt.Client()
client.connected = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker: " + BROKER_ADDRESS)
        client.connected = True


def connect_to_broker():
    client.username_pw_set(USERNAME, PASSWORD)
    try:
        client.connect(BROKER_ADDRESS, PORT)
        client.loop_start()
    except:
        print("Connection to MQTT Broker failed")


def publish(topic, message):
    if client.connected == True:
        client.publish(topic, message, qos=QOS)
        client.loop_start()


client.on_connect = on_connect