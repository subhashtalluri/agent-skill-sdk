# Triggers

## Timer Trigger
```python
from agent_skill_sdk.plugins import TimerTrigger
TimerTrigger(interval=10, event_name="on_timer").attach(agent)
```

## MQTT Trigger
```python
from agent_skill_sdk.plugins import MQTTTrigger
MQTTTrigger(topic="agent/test").attach(agent)
```

## HTTP Trigger
```bash
curl -X POST http://localhost:9000/trigger -d '{"hello": "world"}'
```

## Cron Trigger
```python
from agent_skill_sdk.plugins.cron import CronTrigger
CronTrigger("10", event_name="on_cron").attach(agent)
```

## File Watcher
```python
from agent_skill_sdk.plugins.file_watcher import FileWatcherTrigger
FileWatcherTrigger("/tmp/watch.txt").attach(agent)
```

## CoAP Trigger
```python
from agent_skill_sdk.plugins.coap import CoAPTrigger
CoAPTrigger("trigger").attach(agent)
```