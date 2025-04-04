# Example Gallery

## Fan Control
```python
@skill(trigger="on_temperature_high")
def turn_on_fan(context):
    print("Fan ON")
```

## Webhook Response
```python
@skill(trigger="on_http")
def handle_webhook(context):
    print(context.data)
```

## LLM Planning
```python
@skill(trigger="on_goal")
def decide_action(context):
    response = run_reasoning(context.get("goal"))
    context.agent.trigger(response["action"])
```