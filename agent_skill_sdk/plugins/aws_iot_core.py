from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

class AWSIoTCoreTrigger:
    def __init__(self, client_id, endpoint, topic, cert_path, key_path, root_ca_path, port=8883, event_name="on_aws_iot"):
        self.client_id = client_id
        self.endpoint = endpoint
        self.topic = topic
        self.cert_path = cert_path
        self.key_path = key_path
        self.root_ca_path = root_ca_path
        self.port = port
        self.event_name = event_name
        self.agent = None

    def attach(self, agent):
        self.agent = agent
        mqtt_client = AWSIoTMQTTClient(self.client_id)
        mqtt_client.configureEndpoint(self.endpoint, self.port)
        mqtt_client.configureCredentials(self.root_ca_path, self.key_path, self.cert_path)

        # Optional: configure timeouts and reconnection
        mqtt_client.configureAutoReconnectBackoffTime(1, 32, 20)
        mqtt_client.configureOfflinePublishQueueing(-1)  # Infinite queue
        mqtt_client.configureDrainingFrequency(2)  # Draining: 2 Hz
        mqtt_client.configureConnectDisconnectTimeout(10)  # 10 sec
        mqtt_client.configureMQTTOperationTimeout(5)  # 5 sec

        def message_callback(client, userdata, message):
            try:
                payload = json.loads(message.payload.decode())
                print(f"[AWS IoT Core] Message received on topic '{message.topic}': {payload}")
                self.agent.trigger(self.event_name, payload)
            except Exception as e:
                print(f"[AWS IoT Core] Error handling message: {e}")

        mqtt_client.connect()
        mqtt_client.subscribe(self.topic, 1, message_callback)
        print(f"[AWS IoT Core] Subscribed to topic: {self.topic}")