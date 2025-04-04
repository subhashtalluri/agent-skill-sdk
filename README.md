# 🧠 Agent Skill SDK

A modular, event-driven agent framework for building reactive, intelligent systems with pluggable skills, trigger handlers, retry logic, memory, and LLM-ready infrastructure.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)

---

## ✨ Features

- ✅ **Skill-Based Programming**: Register Python functions as event-driven skills
- 🔁 **Retry & Backoff**: Automatic retries on failure with fixed or exponential delays
- 🧠 **Context Object**: Carry structured input between plugins and skills
- ⏲️ **Trigger Plugins**: Timer, MQTT, and custom protocol handlers
- 🧪 **Testable Core**: Modular architecture with pytest-based test suite
- 🔌 **Extendable**: Add your own skills, triggers, memory, or LLM integration
- ⚙️ **CLI Tools**: Trigger skills, run agents, and debug from terminal
- 📦 **Packaged & Deployable**: PyPI-ready with Docker and CLI entrypoint

---

## 🚀 Quickstart

### 📦 Install
```bash
pip install agent-skill-sdk
```

### 🔧 Define a Skill
```python
from agent_skill_sdk import skill

@skill(trigger="on_temp_high", retries=2, backoff="fixed")
def turn_on_fan(context):
    print(f"Turning on fan at {context['location']}")
```

### ⚡ Run Agent via CLI
```bash
agent register examples.fan_control.turn_on_fan
agent trigger on_temp_high --data '{"location": "kitchen"}'
```

---

## 📁 Folder Structure

```
agent_skill_sdk/
├── agent/          # Core runtime, registry, context
├── skills/         # Built-in skills (noop, echo, log)
├── plugins/        # MQTT, Timer, CoAP, etc.
├── cli/            # Command-line tools
├── config/         # Config loading from env/.env
├── examples/       # Sample skill files
├── tests/          # Pytest test suite
```

---

## 🔌 Plugins

### 🕒 Timer Trigger
Run skills on an interval:
```python
from agent_skill_sdk.plugins import TimerTrigger

TimerTrigger(interval=10, event_name="on_timer").attach(agent)
```

### 📡 MQTT Trigger
Respond to IoT messages:
```python
from agent_skill_sdk.plugins import MQTTTrigger

MQTTTrigger(topic="agent/events").attach(agent)
```

---

## 🧪 Testing
```bash
pytest tests/
```

---

## 📚 Documentation
Coming soon to ReadTheDocs & GitHub Pages

---

## 📜 License
MIT – do anything, just give credit ✨

---

## 💡 Ideas?
File an issue, submit a skill, or join the community. Your agents are waiting!