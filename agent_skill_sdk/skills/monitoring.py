from agent_skill_sdk import skill

@skill(trigger="on_temp_reading")
def log_temperature(context):
    temp = context.get("temperature", "unknown")
    print(f"[Monitoring] Logging temperature: {temp}°C")
    context.memory.record_event("temperature_log", {"value": temp})

@skill(trigger="on_temp_check")
def alert_if_threshold_exceeded(context):
    temp = context.get("temperature", 0)
    threshold = context.get("threshold", 30)
    if temp > threshold:
        print(f"[Monitoring] ALERT! Temperature {temp}°C exceeds threshold {threshold}°C")
        context.memory.record_event("temperature_alert", {"value": temp, "threshold": threshold})
    else:
        print(f"[Monitoring] Temperature {temp}°C is within normal limits.")
        context.memory.record_event("temperature_ok", {"value": temp, "threshold": threshold})

@skill(trigger="on_disk_check")
def disk_space_warning(context):
    free_space = context.get("free_gb", 100)
    if free_space < 5:
        print(f"[Monitoring] WARNING! Low disk space: {free_space} GB remaining.")
        context.memory.record_event("disk_low", {"free_gb": free_space})
    else:
        print(f"[Monitoring] Disk space OK: {free_space} GB")
        context.memory.record_event("disk_ok", {"free_gb": free_space})