import paho.mqtt.client as mqtt

class MQTTTrigger:
    def __init__(self, broker="localhost", port=1883, topic="agent/events"):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.agent = None

    def attach(self, agent):
        self.agent = agent
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"[MQTT] Connected to {self.broker}:{self.port}, subscribing to '{self.topic}'")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        print(f"[MQTT] Message received: {payload}")
        self.agent.trigger("on_mqtt_message", payload={"topic": msg.topic, "message": payload})