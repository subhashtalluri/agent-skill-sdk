from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from agent_skill_sdk import Agent, skill
from examples.fan_control import turn_on_fan
from examples.bedrock_planner import bedrock_planner

app = FastAPI()
agent = Agent()
agent.register(turn_on_fan)
agent.register(bedrock_planner)

@app.get("/", response_class=HTMLResponse)
async def home():
    skills = agent.list_skills()
    html = "<h2>🧠 Agent Dashboard</h2><ul>"
    for name, trigger in skills:
        html += f"<li><b>{name}</b> — Trigger: {trigger}</li>"
    html += "</ul>"

    html += '''
    <form method='post' action='/trigger'>
        <input name='event' placeholder='Event name' />
        <input name='payload' placeholder='JSON payload (optional)' />
        <button type='submit'>Trigger Skill</button>
    </form>
    <p><a href='/trace'>📜 View LLM Trace</a></p>
    '''
    return html

@app.post("/trigger")
async def manual_trigger(event: str = Form(...), payload: str = Form("{}")):
    import json
    try:
        agent.trigger(event, json.loads(payload))
    except Exception as e:
        return HTMLResponse(f"<p>Error: {e}</p>", status_code=400)
    return RedirectResponse("/", status_code=302)

@app.get("/trace", response_class=HTMLResponse)
async def view_trace():
    trace = agent.export_trace("json")
    return f"<h3>Trace Log</h3><pre>{trace}</pre><p><a href='/'>⬅️ Back</a></p>"