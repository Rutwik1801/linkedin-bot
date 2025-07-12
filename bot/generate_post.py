import os
import datetime
from openai import OpenAI
from prompts.templates import get_prompt_for_day

def generate_linkedin_post():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    day = datetime.datetime.today().strftime('%A')
    prompt = get_prompt_for_day(day)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response.choices[0].message.content
