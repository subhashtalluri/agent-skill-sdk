from .registry import SkillRegistry
from .context import AgentContext
from .runner import SkillRunner
from ..logs.memory import MemoryStore
from ..reasoning.templates import TemplateStore

class Agent:
    def __init__(self, logger=None):
        self.registry = SkillRegistry()
        self.runner = SkillRunner(logger=logger)
        self.memory = MemoryStore()
        self.templates = TemplateStore()

    def register(self, skill_func):
        self.registry.add(skill_func)

    def trigger(self, event_name, payload=None):
        context = AgentContext(payload)
        context.memory = self.memory
        context.templates = self.templates
        context.agent = self
        matched_skills = self.registry.get_by_trigger(event_name)

        if not matched_skills:
            print(f"[Agent] No skills found for trigger: '{event_name}'")
            return

        for skill in matched_skills:
            self.runner.run(skill, context)

    def list_skills(self):
        return self.registry.list_skills()

    def export_trace(self, format="json"):
        return self.memory.export(format)