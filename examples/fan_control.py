from agent_skill_sdk.decorators import skill

@skill(trigger="on_temperature_high", retries=2, backoff="fixed")
def turn_on_fan(context):
    temp = context.get("temp", "unknown")
    print(f"[Skill] Fan turned ON due to high temperature: {temp}")