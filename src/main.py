from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)