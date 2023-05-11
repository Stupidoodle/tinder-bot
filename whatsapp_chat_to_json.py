import json

conversation = open()

messages = []
lines = conversation.strip.split("\n")

for line in lines:
    parts = line.split("] ")
    if len(parts) == 2:
        role, content = parts[1].split(": ", 1)
        messages.append({"role": role.strip(), "content": content.strip()})

json_data = json.dumps(messages, indent=4)

with open("conversation.json", "w") as file:
    file.write(json_data)
