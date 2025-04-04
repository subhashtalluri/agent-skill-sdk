from .registry import SkillRegistry
from .context import AgentContext
from .runner import SkillRunner

class Agent:
    def __init__(self, logger=None):
        self.registry = SkillRegistry()
        self.runner = SkillRunner(logger=logger)

    def register(self, skill_func):
        self.registry.add(skill_func)

    def trigger(self, event_name, payload=None):
        context = AgentContext(payload)
        matched_skills = self.registry.get_by_trigger(event_name)

        if not matched_skills:
            print(f"[Agent] No skills found for trigger: '{event_name}'")
            return

        for skill in matched_skills:
            self.runner.run(skill, context)

    def list_skills(self):
        return self.registry.list_skills()