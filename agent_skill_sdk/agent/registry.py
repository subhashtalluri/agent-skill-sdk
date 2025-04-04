class SkillRegistry:
    def __init__(self):
        self.skills = []

    def add(self, skill_func):
        self.skills.append(skill_func)

    def get_by_trigger(self, trigger_name):
        return [s for s in self.skills if getattr(s, '_trigger', None) == trigger_name]

    def list_skills(self):
        return [(s.__name__, getattr(s, '_trigger', None)) for s in self.skills]