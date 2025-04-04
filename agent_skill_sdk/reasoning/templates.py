class TemplateStore:
    def __init__(self):
        self.templates = {}

    def register(self, name, template):
        self.templates[name] = template

    def get(self, name, default=""):
        return self.templates.get(name, default)