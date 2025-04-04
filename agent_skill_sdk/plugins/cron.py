import schedule
import time
import threading

class CronTrigger:
    def __init__(self, schedule_expr, event_name="on_cron"):
        self.schedule_expr = schedule_expr
        self.event_name = event_name
        self.agent = None

    def attach(self, agent):
        self.agent = agent
        getattr(schedule.every(), self.schedule_expr).seconds.do(self._trigger)
        thread = threading.Thread(target=self._run_loop, daemon=True)
        thread.start()

    def _trigger(self):
        self.agent.trigger(self.event_name)

    def _run_loop(self):
        while True:
            schedule.run_pending()
            time.sleep(1)