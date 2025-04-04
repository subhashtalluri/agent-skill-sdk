# Writing Skills

## @skill Decorator

```python
from agent_skill_sdk import skill

@skill(trigger="on_event", retries=3, backoff="fixed")
def my_skill(context):
    print(context.data)
```

## Context Object

```python
def my_skill(context):
    value = context.get("key")
    context["result"] = value + 1
```