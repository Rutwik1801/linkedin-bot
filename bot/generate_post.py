import os
import datetime
from openai import OpenAI

from prompts.templates import get_prompt_for_day

def generate_linkedin_post():
    print(os.getenv("OPENAI_API_KEY"))
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    day = datetime.datetime.today().strftime('%A')
    prompt = get_prompt_for_day(day)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=300
    )
    return response.choices[0].message.content