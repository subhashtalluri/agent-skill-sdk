# Memory and Tracing

- Every skill invocation is logged to memory
- LLM reasoning is traceable with goal, template, result
- Export to JSON or CSV

## Export Example
```python
agent.export_trace("json")
agent.export_trace("csv")
```