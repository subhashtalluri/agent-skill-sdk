import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.mqtt_broker = os.getenv("MQTT_BROKER", "localhost")
        self.mqtt_port = int(os.getenv("MQTT_PORT", 1883))
        self.mqtt_topic = os.getenv("MQTT_TOPIC", "agent/events")
        self.timer_interval = int(os.getenv("TIMER_INTERVAL", 10))

    def as_dict(self):
        return {
            "mqtt_broker": self.mqtt_broker,
            "mqtt_port": self.mqtt_port,
            "mqtt_topic": self.mqtt_topic,
            "timer_interval": self.timer_interval
        }

settings = Settings()