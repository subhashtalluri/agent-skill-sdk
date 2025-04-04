# 🧠 Agent Skill SDK

A lightweight, event-driven framework for building intelligent agents with modular skills, real-world triggers, memory, and LLM-based planning using Amazon Bedrock.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)

---

## 🚀 Features

- ✅ Modular `@skill`-based programming model
- 🔁 Retry, backoff, and fallback support
- 🧠 LLM reasoning via **Amazon Bedrock**
- 📡 Event triggers: Timer, MQTT, HTTP, Cron, File Watcher, CoAP, AWS IoT Core
- 💡 Edge-ready: Runs on Raspberry Pi, Jetson Nano, AWS Greengrass
- 📜 Memory tracing and export (CSV/JSON)
- 🧪 FastAPI dashboard + CLI support

---

## 📦 Installation

```bash
pip install agent-skill-sdk
```

---

## 🔧 Define a Skill

You can write reactive skills that trigger from events:

```python
from agent_skill_sdk import skill

@skill(trigger="on_temperature_high", retries=2, backoff="fixed")
def turn_on_fan(context):
    temp = context.get("temp")
    print(f"[Skill] Fan turned ON due to high temperature: {temp}")
```

---

## 🧠 LLM Reasoning with Amazon Bedrock

Use `run_reasoning()` to generate intelligent plans based on a goal and memory.

### 📄 Define a Planner Skill

```python
from agent_skill_sdk import skill
from agent_skill_sdk.reasoning.bedrock import run_reasoning

@skill(trigger="on_goal")
def bedrock_planner(context):
    goal = context.get("goal", "unknown")
    memory_log = context.memory.recall_last_n(5)
    template = context.templates.get("goal_plan")

    response = run_reasoning(goal, memory=memory_log, template=template)

    action = response.get("action")
    reason = response.get("reason")

    context.memory.record_event("llm_plan", {
        "goal": goal,
        "template": template,
        "llm_response": response
    })

    if action:
        context.agent.trigger(action, {
            "from_planner": True,
            "goal": goal,
            "reason": reason
        })
```

### 🧠 Example Prompt Template

```python
agent.templates.register("goal_plan", '''
You are solving the goal: {goal}
Memory:
{memory}
Return: { "action": "skill_name", "reason": "why this action" }
''')
```

---

## 📡 Available Triggers

| Trigger       		| Plugin File              | Description                        |
|-----------------------|--------------------------|------------------------------------|
| Timer         		| `timer.py`               | Interval-based triggers            |
| MQTT          		| `mqtt.py`                | IoT messages over MQTT             |
| HTTP/Webhook  		| `http.py`                | POST to trigger skills             |
| Cron          		| `cron.py`                | Cron-based scheduling              |
| File Watcher  		| `file_watcher.py`        | Watch for file changes             |
| CoAP          		| `coap.py`                | UDP-based IoT messaging            |
| AWS IoT Core  		| `aws_iot_core.py`        | Secure MQTT via Amazon IoT Core    |
| AWS IoT Greengrass    | `greengrass/adapter.py`  | Offline agent support on AWS Edge  |

---

## 🧠 Traceable Memory

Every skill and reasoning plan is logged:
```python
trace_json = agent.export_trace("json")
trace_csv = agent.export_trace("csv")
```

---

## 🧪 Dashboard

```bash
uvicorn dashboard.app:app --reload
```

Visit `http://localhost:8000` to:
- View skills
- Trigger events
- Inspect memory/LLM traces

---

## 🧱 Edge Deployment

Supports Raspberry Pi, Jetson Nano, and AWS Greengrass.

Run locally with:
```bash
python app.py
```

Deploy to Greengrass with:
- `greengrass/adapter.py`
- `greengrass/recipe.json`

---

## 📚 Documentation

Full docs: [https://subhashtalluri.github.io/agent-skill-sdk/](https://subhashtalluri.github.io/agent-skill-sdk)

---

## 📜 License

MIT – do anything, just give credit ✨