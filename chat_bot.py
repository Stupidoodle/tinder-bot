import openai
import keys
import json

openai.api_key = keys.openai_api_key

with open("conversation.json", "r") as file:
    conversation = json.load(file)

model = "text-davinci-002"

response = openai.Completion.create(
    engine = model,
    messages = conversation,
    max_tokens = 30,
    n = 1,
    temperature = 0.8,
    prompt = "You: Wie geht es dir?\nChatGPT:"
)

reply = response.choices[0].text.strip()
print(reply)