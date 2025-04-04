import json

class GreengrassAgentAdapter:
    def __init__(self, agent):
        self.agent = agent

    def handle_input(self, event):
        '''
        Handles input from Greengrass Lambda or container component.

        Expected format:
        {
            "trigger": "event_name",
            "payload": {...}
        }
        '''
        try:
            trigger_name = event.get("trigger")
            payload = event.get("payload", {})
            print(f"[GreengrassAdapter] Received trigger: {trigger_name}")
            self.agent.trigger(trigger_name, payload)
            return {
                "status": "success",
                "triggered": trigger_name
            }
        except Exception as e:
            print(f"[GreengrassAdapter] Error: {e}")
            return {
                "status": "error",
                "message": str(e)
            }