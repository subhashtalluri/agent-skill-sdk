import threading
import time

class TimerTrigger:
    def __init__(self, interval=5, event_name="on_timer"):
        self.interval = interval
        self.event_name = event_name
        self.agent = None
        self._running = False

    def attach(self, agent):
        self.agent = agent
        self._running = True
        thread = threading.Thread(target=self._run_loop, daemon=True)
        thread.start()

    def _run_loop(self):
        while self._running:
            time.sleep(self.interval)
            self.agent.trigger(self.event_name)