import openai, os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_TOKEN")

def response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    response = response['choices'][0]['message']['content']
    return response