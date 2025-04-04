import argparse
import json
import importlib
from agent_skill_sdk.agent.core import Agent

agent = Agent()

def load_skill(path):
    module_path, _, func_name = path.rpartition(".")
    module = importlib.import_module(module_path)
    skill = getattr(module, func_name)
    agent.register(skill)
    print(f"[CLI] Registered skill: {func_name}")

def main():
    parser = argparse.ArgumentParser(description="Agent Skill SDK CLI")
    subparsers = parser.add_subparsers(dest="command")

    reg = subparsers.add_parser("register")
    reg.add_argument("path", help="Python import path to skill")

    trig = subparsers.add_parser("trigger")
    trig.add_argument("event", help="Trigger name")
    trig.add_argument("--data", help="JSON string payload", default="{}")

    args = parser.parse_args()

    if args.command == "register":
        load_skill(args.path)

    elif args.command == "trigger":
        data = json.loads(args.data)
        agent.trigger(args.event, payload=data)

    else:
        parser.print_help()