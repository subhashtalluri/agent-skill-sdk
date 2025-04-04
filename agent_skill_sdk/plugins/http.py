from fastapi import FastAPI, Request
import uvicorn
import threading
import json

class HTTPTrigger:
    def __init__(self, port=9000, route="/trigger", event_name="on_http"):
        self.port = port
        self.route = route
        self.event_name = event_name
        self.agent = None

    def attach(self, agent):
        self.agent = agent
        self.app = FastAPI()

        @self.app.post(self.route)
        async def handle_event(request: Request):
            payload = await request.json()
            print(f"[HTTPTrigger] Event received: {payload}")
            self.agent.trigger(self.event_name, payload)
            return {"status": "triggered"}

        thread = threading.Thread(
            target=lambda: uvicorn.run(self.app, host="0.0.0.0", port=self.port, log_level="warning"),
            daemon=True
        )
        thread.start()
