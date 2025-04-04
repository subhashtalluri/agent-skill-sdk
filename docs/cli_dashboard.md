# CLI and Dashboard

## 🔧 CLI
```bash
agent register examples.fan_control.turn_on_fan
agent trigger on_temperature_high --data '{"temp": 36}'
```

## 🧠 Dashboard
```bash
uvicorn dashboard.app:app --reload
```

Open `http://localhost:8000` to:
- View skills
- Trigger manually
- View trace