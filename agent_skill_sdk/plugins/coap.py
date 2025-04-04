from aiocoap import resource, Context
import asyncio
import threading

class CoAPTrigger:
    def __init__(self, path="trigger", event_name="on_coap"):
        self.path = path
        self.event_name = event_name
        self.agent = None

    def attach(self, agent):
        self.agent = agent
        threading.Thread(target=self._start_server, daemon=True).start()

    def _start_server(self):
        class TriggerResource(resource.Resource):
            async def render_post(self, request):
                payload = request.payload.decode("utf-8")
                print(f"[CoAPTrigger] Received: {payload}")
                self.agent.trigger(self.event_name, {"payload": payload})
                return aiocoap.Message(code=aiocoap.CONTENT, payload=b"ACK")

        async def main():
            root = resource.Site()
            root.add_resource(('.well-known', 'core'), resource.WKCResource(root.get_resources_as_linkheader))
            root.add_resource((self.path,), TriggerResource())
            await Context.create_server_context(root)
            await asyncio.get_event_loop().create_future()  # run forever

        asyncio.run(main())