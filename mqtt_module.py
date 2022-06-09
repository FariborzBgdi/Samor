import paho.mqtt.client as mqtt

USERNAME = "samor"
PASSWORD = "haw"
TOPIC_MECANUM = "mecanum"
TOPIC_MANIPULATOR = "manipulator"
BROKER_ADDRESS = "192.168.0.1"
PORT = 1883
QOS = 1

client = mqtt.Client()

def connect_to_broker():
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(BROKER_ADDRESS, PORT)
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)


def publish(topic, message):
    client.publish(topic, message, qos=QOS)
    client.loop()
