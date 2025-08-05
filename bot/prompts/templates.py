import json
import os

with open(os.path.join(os.path.dirname(__file__), '../../content/schedule.json')) as f:
    schedule = json.load(f)

def get_prompt_for_day(day):
    base_prompt = schedule.get(day, "Share something useful for frontend developers.")
    return f"You are a helpful frontend mentor. {base_prompt} Make it: 1.Start with a strong hook (question, bold statement, or relatable sentence) 2.Include a short personal story, lesson learned, or honest insight 3.Use a casual, human tone — no corporate or robotic voice 4.Keep paragraphs short for readability on mobile 5.Use emojis if they feel natural, not forced 6.End with a friendly question that invites comments 7.Audience: Other frontend developers (mid-level and beginner friendly) 8.Tone: Honest, relatable, and helpful"

