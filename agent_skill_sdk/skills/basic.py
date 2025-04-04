from agent_skill_sdk.decorators import skill

@skill(trigger="on_ping")
def echo_ping(context):
    print("[Basic Skill] Pong!")

@skill(trigger="on_log")
def log_payload(context):
    print(f"[Basic Skill] Logging payload: {context.data}")

@skill(trigger="on_noop")
def noop(context):
    pass