import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def diagnose_issue(pod_description: str, pod_logs: str):
    prompt = f"""
    You are a Kubernetes expert.
    Based on the following pod description and logs, identify the root cause of failure and suggest a fix.
    
    Pod Description:
    {pod_description}

    Pod Logs:
    {pod_logs}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful DevOps assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']