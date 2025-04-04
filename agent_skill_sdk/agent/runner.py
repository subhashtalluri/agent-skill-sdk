import time

class SkillRunner:
    def __init__(self, logger=None):
        self.logger = logger

    def run(self, skill, context):
        retries = getattr(skill, "_retries", 1)
        backoff = getattr(skill, "_backoff", "none")

        for attempt in range(retries):
            try:
                skill(context)
                return
            except Exception as e:
                if self.logger:
                    self.logger.error(f"[SkillRunner] Error in '{skill.__name__}': {e}")
                else:
                    print(f"[SkillRunner] Error in '{skill.__name__}': {e}")

                if attempt < retries - 1:
                    if backoff == "fixed":
                        time.sleep(1)
                    elif backoff == "exponential":
                        time.sleep(2 ** attempt)