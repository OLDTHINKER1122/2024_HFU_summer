from openai import OpenAI
import os

def chat_with_chatgpt(user_message, openai_api_key):
    #利用OpenAI類別，建立一個可以
    client = OpenAI(api_key=openai_api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )

    response = chat_completion.choices[0].message.content
    return response
if __name__ == '__main__':

    user_message = '我愛喝波蜜果菜汁，你說你愛不愛。'
    api_key = os.getenv("OPENAI_API_KEY", None)
    if api_key and user_message:
        response = chat_with_chatgpt(user_message, api_key)
        print(response)
    else:
        print("api key not found: ", api_key)