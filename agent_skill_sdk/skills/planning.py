from agent_skill_sdk import skill
from agent_skill_sdk.reasoning.bedrock import run_reasoning

@skill(trigger="on_summarize_logs")
def summarize_logs(context):
    logs = context.memory.recall_last_n(10)
    summary_prompt = f"Summarize the following logs:\n{logs}"
    response = run_reasoning(goal="summarize_logs", memory=logs, template=summary_prompt)
    print("[Planning] Log summary:", response.get("summary", "N/A"))
    context.memory.record_event("logs_summarized", response)

@skill(trigger="on_generate_report")
def generate_report(context):
    report_goal = context.get("goal", "Generate system health report")
    memory = context.memory.recall_last_n(10)
    report = run_reasoning(goal=report_goal, memory=memory)
    print("[Planning] Generated report:", report)
    context.memory.record_event("report_generated", report)

@skill(trigger="on_recommend_action")
def recommend_action(context):
    state = context.get("system_state", {})
    goal = context.get("goal", "decide what to do next")
    recommendation = run_reasoning(goal=goal, memory=[state])
    action = recommendation.get("action")
    reason = recommendation.get("reason")
    print(f"[Planning] Recommending action: {action} — {reason}")
    context.memory.record_event("action_recommended", recommendation)
    if action:
        context.agent.trigger(action, {"from_planning": True, "reason": reason})