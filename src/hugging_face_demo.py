
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HUGGING_FACE_TOKEN"],
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct-0905",
    messages=[
        {
            "role": "user",
            "content": "Generate a list of 10 interesting facts about space."
        }
    ],
)

print(completion.choices[0].message)