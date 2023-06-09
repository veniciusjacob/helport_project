import openai

openai.api_key = 'token_here'

def generate_response(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=2040,
        n=1,
        stop=None,
        temperature=0.7
    )

    reply = response.choices[0].text.strip()

    return reply
