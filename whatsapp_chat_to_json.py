import json
import string

#supported_chars = set(string.printable + ''.join(chr(i) for i in range(0x10000) if chr(i).isprintable()))

with open("_chat.txt", encoding = "utf-8-sig", errors = "ignore") as file:
    content = file.read()

clean = "".join(c for c in content)

conversation = clean

messages = []
lines = conversation.strip().split("\n")

for line in lines:
    parts = line.split("] ")
    if len(parts) == 2:
        role, content = parts[1].split(": ", 1)
        messages.append({"role": role.strip(), "content": content.strip()})

json_data = json.dumps(messages, indent=4)

with open("conversation.json", "w") as file:
    file.write(json_data)

print("Done!")