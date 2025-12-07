# Nakshatra-Automation-MQTT-Assignment

Full Name: Karthick V
Register Number: 42733038
MQTT Topic Used: Lightweight and Case-sensitive
Explanation of Extra Sensor:
The extra sensor I used is a Light sensor. The light sensor value represents the brightness level in the environment. It is useful in smart home applications to detect lighting conditions and trigger automations, such as switching lights on when the room becomes dark.
Steps to be Followed :
•	I first wrote a Python script that publishes three values using MQTT—temperature, humidity, and light—along with my full name, register number, and a unique topic.
•	Next, I created a Dockerfile so the script could run inside a Docker container. 
•	After that, I installed the Mosquitto MQTT broker through Docker and configured it to accept incoming sensor data. 
•	Then, I built and ran my Python MQTT publisher container alongside the Mosquitto broker using docker-compose. 
•	Once both containers were running, I verified that the sensor values were being published correctly every five seconds to my unique MQTT topic. 
•	Finally, I connected Home Assistant to the MQTT broker and confirmed that all sensor readings appeared successfully inside Home Assistant, completing the assignment requirements.
