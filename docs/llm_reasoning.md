# LLM Reasoning with Amazon Bedrock

## 🧠 Planner Skill
```python
@skill(trigger="on_goal")
def bedrock_planner(context):
    response = run_reasoning(goal, memory=context.memory.recall_last_n(5))
    action = response.get("action")
    if action:
        context.agent.trigger(action)
```

## Prompt Template Store

```python
agent.templates.register("goal_plan", "You are solving: {goal}\nMemory: {memory}")
```

## Fallback Logic

- Auto retries LLM if action missing
- Fallbacks to "noop" after max attempts