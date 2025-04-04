from agent_skill_sdk import skill

@skill(trigger="on_temp_high")
def turn_on_fan(context):
    print("[Automation] Turning on fan due to high temperature.")
    context.memory.record_event("fan_on", {"triggered_by": "on_temp_high"})

@skill(trigger="on_temp_low")
def turn_off_heater(context):
    print("[Automation] Turning off heater due to low temperature.")
    context.memory.record_event("heater_off", {"triggered_by": "on_temp_low"})

@skill(trigger="on_light_toggle")
def toggle_light(context):
    state = context.get("state", "on")
    print(f"[Automation] Toggling light to: {state}")
    context.memory.record_event("light_toggle", {"state": state})

@skill(trigger="on_valve_command")
def open_valve(context):
    print("[Automation] Opening valve for flow control.")
    context.memory.record_event("valve_opened", {"source": "on_valve_command"})