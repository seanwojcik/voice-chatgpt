import openai


def chat_gpt(messages, api_key=None, description=None):
    if api_key is not None:
        openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0].message["content"]


def extract_message(response):
    return response.split(":")[-1].strip()
