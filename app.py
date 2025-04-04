from agent_skill_sdk import Agent, skill
from agent_skill_sdk.plugins import TimerTrigger, FileWatcherTrigger
from examples.fan_control import turn_on_fan
from examples.bedrock_planner import bedrock_planner

agent = Agent()
agent.register(turn_on_fan)
agent.register(bedrock_planner)

# Optional template for LLM
agent.templates.register("goal_plan", '''
You are solving the goal: {goal}
Memory: {memory}
Respond with: { "action": "skill_name", "reason": "why" }
''')

# Trigger setup
TimerTrigger(interval=10, event_name="on_timer").attach(agent)
FileWatcherTrigger(watch_path="/tmp/input.txt", event_name="on_file_change").attach(agent)

print("🧠 Agent is running on edge...")

import time
while True:
    time.sleep(60)