import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883
topic = "raspi/demo"

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic)

# Callback when message received
def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()