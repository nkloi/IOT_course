import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"   # Public test broker
port = 1883
topic = "raspi/demo"

client = mqtt.Client()
client.connect(broker, port, 60)

print("Publishing messages...")
try:
    while True:
        message = "Hello MQTT!"
        client.publish(topic, message)
        print("Sent:", message)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopped by User")
finally:
    client.disconnect()