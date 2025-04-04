# 🧠 Agent Skill SDK

Build modular, intelligent agents with event triggers, retry logic, memory, LLM planning (Amazon Bedrock), and a live dashboard.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)

---

## 🚀 Features

- ✅ Skill-based programming with `@skill` decorators
- 🔁 Retry, backoff, and fallback on skill failure
- 🧠 LLM reasoning via Amazon Bedrock
- 🧩 Triggers: Timer, MQTT, HTTP, Cron, File Watcher, CoAP
- 📜 Memory tracing + export (CSV/JSON)
- ⚙️ CLI and 🧪 FastAPI-based dashboard
- 📚 Full developer documentation with MkDocs

---

## 📦 Install

```bash
pip install agent-skill-sdk
```

---

## 🧪 Example: Define a Skill

```python
from agent_skill_sdk import skill

@skill(trigger="on_temp_high", retries=2, backoff="exponential")
def turn_on_fan(context):
    print("Turning on fan:", context.get("location"))
```

---

## ⚡ Trigger from CLI

```bash
agent register examples.fan_control.turn_on_fan
agent trigger on_temp_high --data '{"location": "lab"}'
```

---

## 🧠 LLM Planning (Amazon Bedrock)

```python
@skill(trigger="on_goal")
def bedrock_planner(context):
    response = run_reasoning(context.get("goal"))
    action = response.get("action")
    context.agent.trigger(action)
```

Supports:
- Prompt templates
- Memory recall
- Fallback actions

---

## 🌐 Dashboard

```bash
uvicorn dashboard.app:app --reload
```

Visit [http://localhost:8000](http://localhost:8000) to:
- View registered skills
- Trigger events manually
- Inspect LLM trace logs

---

## 🔌 Trigger Plugins

| Trigger       | File                      | Event             |
|---------------|---------------------------|-------------------|
| Timer         | `timer.py`                | `on_timer`        |
| MQTT          | `mqtt.py`                 | `on_mqtt_message` |
| HTTP/Webhook  | `http.py`                 | `on_http`         |
| Cron          | `cron.py`                 | `on_cron`         |
| File Watcher  | `file_watcher.py`         | `on_file_change`  |
| CoAP (IoT)    | `coap.py`                 | `on_coap`         |

---

## 📚 Documentation

Visit your deployed docs here:  
➡️ [https://subhashtalluri.github.io/agent-skill-sdk/](https://subhashtalluri.github.io/agent-skill-sdk)

Or build locally:
```bash
mkdocs serve
```

---

## 📤 Deployment

Use Docker or deploy with Uvicorn:

```bash
uvicorn dashboard.app:app --host 0.0.0.0 --port 8000
```

---

## 🧠 Trace Export

```python
agent.export_trace("json")
agent.export_trace("csv")
```

---

## 🧩 Contributions Welcome

Build a trigger plugin, skill library, or submit a PR!

---

## 📜 License

MIT – do anything, just give credit ✨