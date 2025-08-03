import json
import os

with open(os.path.join(os.path.dirname(__file__), '../../content/schedule.json')) as f:
    schedule = json.load(f)

def get_prompt_for_day(day):
    base_prompt = schedule.get(day, "Share something useful for frontend developers.")
    return f"You are a helpful frontend mentor. {base_prompt} Make it engaging, viral, and end with a question. Also include relevant hashtags in the end. Give it a human like feel."

