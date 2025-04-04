# Getting Started

## 📦 Installation

```bash
pip install agent-skill-sdk
```

## 🧱 Folder Structure
```
agent_skill_sdk/
├── agent/
├── plugins/
├── skills/
├── cli/
├── config/
├── examples/
├── tests/
└── dashboard/
```

## 🧪 First Run

```python
from agent_skill_sdk import Agent
from examples.fan_control import turn_on_fan

agent = Agent()
agent.register(turn_on_fan)
agent.trigger("on_temperature_high", {"temp": 36})
```