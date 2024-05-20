from typing import TypedDict
from openai import OpenAI

class openai(TypedDict):
    api_key: str
    organization_id: str
    

def main(resource: openai, prompt: str):
    client = OpenAI(api_key=resource['api_key'])

    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )

    return chat_completion.choices[0].message.content
