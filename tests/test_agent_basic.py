from agent_skill_sdk.agent.core import Agent
from agent_skill_sdk.decorators import skill

@skill(trigger="on_test_event")
def test_skill(context):
    print(f"Test skill triggered with: {context.data}")

def test_trigger_and_output(capsys):
    agent = Agent()
    agent.register(test_skill)
    agent.trigger("on_test_event", {"value": 42})
    captured = capsys.readouterr()
    assert "Test skill triggered with: {'value': 42}" in captured.out