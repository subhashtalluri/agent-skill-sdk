from agent_skill_sdk import skill
from agent_skill_sdk.reasoning.bedrock import run_reasoning

@skill(trigger="on_goal_plan_execute")
def plan_and_execute(context):
    goal = context.get("goal", "unknown")
    memory = context.memory.recall_last_n(5)
    template = context.templates.get("goal_plan")

    print(f"[HybridLLM] Planning for goal: {goal}")
    plan = run_reasoning(goal=goal, memory=memory, template=template)

    action = plan.get("action")
    reason = plan.get("reason")

    context.memory.record_event("plan_executed", {
        "goal": goal,
        "action": action,
        "reason": reason,
        "llm_output": plan
    })

    if action:
        print(f"[HybridLLM] Executing action: {action}")
        context.agent.trigger(action, {
            "from_planner": True,
            "reason": reason,
            "goal": goal
        })
    else:
        print("[HybridLLM] No action returned by planner.")