import boto3
import json
import os

BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")
REGION = os.getenv("AWS_REGION", "us-east-1")
bedrock = boto3.client("bedrock-runtime", region_name=REGION)

def run_reasoning(goal, memory=None, template=None):
    mem_str = "\n".join(str(m) for m in memory) if memory else ""
    prompt = template or f"""
You are an intelligent agent. Your goal is: {goal}
Here is your memory: {mem_str}

Respond in JSON:
{{"action": "skill_name", "reason": "why this helps achieve the goal"}}
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = bedrock.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read().decode())
    return json.loads(result['content'][0]['text'])