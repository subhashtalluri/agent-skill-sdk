from agent_skill_sdk import skill
import time
import random

@skill(trigger="on_health_check")
def check_sensor_health(context):
    sensor_id = context.get("sensor_id", "sensor_01")
    healthy = random.choice([True, True, False])  # simulate check
    if healthy:
        print(f"[EdgeOps] {sensor_id} is healthy.")
        context.memory.record_event("sensor_healthy", {"sensor_id": sensor_id})
    else:
        print(f"[EdgeOps] {sensor_id} FAILED health check.")
        context.memory.record_event("sensor_failure", {"sensor_id": sensor_id})

@skill(trigger="on_device_ping")
def ping_device(context):
    device_ip = context.get("ip", "192.168.1.100")
    print(f"[EdgeOps] Pinging device at {device_ip}...")
    time.sleep(0.5)  # simulate latency
    success = random.choice([True, False])
    if success:
        print(f"[EdgeOps] Device at {device_ip} is online.")
        context.memory.record_event("ping_success", {"ip": device_ip})
    else:
        print(f"[EdgeOps] Device at {device_ip} is unreachable.")
        context.memory.record_event("ping_failure", {"ip": device_ip})