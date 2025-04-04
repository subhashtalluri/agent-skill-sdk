import json
import csv
import io

class MemoryStore:
    def __init__(self):
        self.events = []

    def record_event(self, event_name, payload):
        self.events.append({
            "event": event_name,
            "payload": payload
        })

    def recall_last_n(self, n=5):
        return self.events[-n:]

    def recall_all(self):
        return self.events

    def export(self, format="json"):
        if format == "json":
            return json.dumps(self.events, indent=2)
        elif format == "csv":
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=["event", "payload"])
            writer.writeheader()
            for e in self.events:
                writer.writerow({
                    "event": e["event"],
                    "payload": json.dumps(e["payload"])
                })
            return output.getvalue()