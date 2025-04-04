from agent_skill_sdk.decorators import skill
from agent_skill_sdk.reasoning.bedrock import run_reasoning

@skill(trigger="on_goal")
def bedrock_planner(context):
    goal = context.get("goal", "No goal provided")
    memory_log = context.memory.recall_last_n(5) if hasattr(context, 'memory') else []
    template_store = getattr(context, "templates", None)
    template = template_store.get("goal_plan") if template_store else None

    print(f"[Planner] Received goal: {goal}")
    llm_output = run_reasoning(goal, memory=memory_log, template=template)

    action = llm_output.get("action")
    reason = llm_output.get("reason")

    print(f"[Planner] LLM suggests action: {action} — Reason: {reason}")

    trace = {
        "goal": goal,
        "template": template,
        "memory_used": memory_log,
        "llm_response": llm_output
    }

    if hasattr(context, "memory"):
        context.memory.record_event("llm_plan", trace)

    if hasattr(context, "agent") and action:
        context.agent.trigger(action, {
            "from_planner": True,
            "goal": goal,
            "reason": reason,
            "llm_plan": llm_output
        })