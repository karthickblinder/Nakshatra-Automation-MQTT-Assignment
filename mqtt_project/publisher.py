import time
import paho.mqtt.client as mqtt

# -----------------------------
# Assignment Required Information
# -----------------------------
student_name = "Karthick V"
unique_id = "42733038"
topic = "home/karthickv-2025/sensor"
# -----------------------------

broker = "mosquitto"   # Docker container name of broker
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    data = {
        "temperature": 25,
        "humidity": 60,
        "light": 300
    }

    for key, value in data.items():
        client.publish(f"{topic}/{key}", value)
        print(f"Published {key} = {value} to {topic}/{key}")

    time.sleep(5)
