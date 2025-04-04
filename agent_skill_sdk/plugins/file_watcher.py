import os
import time
import threading

class FileWatcherTrigger:
    def __init__(self, watch_path, event_name="on_file_change", interval=2):
        self.watch_path = watch_path
        self.event_name = event_name
        self.interval = interval
        self.agent = None
        self._last_mtime = None

    def attach(self, agent):
        self.agent = agent
        thread = threading.Thread(target=self._watch_loop, daemon=True)
        thread.start()

    def _watch_loop(self):
        print(f"[FileWatcherTrigger] Watching: {self.watch_path}")
        while True:
            if os.path.exists(self.watch_path):
                mtime = os.path.getmtime(self.watch_path)
                if self._last_mtime is None:
                    self._last_mtime = mtime
                elif mtime != self._last_mtime:
                    self._last_mtime = mtime
                    self.agent.trigger(self.event_name, {"path": self.watch_path})
            time.sleep(self.interval)