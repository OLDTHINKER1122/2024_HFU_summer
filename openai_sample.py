import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    #api_key="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"
    api_key=os.environ.get("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")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)