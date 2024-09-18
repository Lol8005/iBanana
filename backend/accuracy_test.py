from chatbot import predict_chat
import json

with open('backend/dataset/intents.json', 'r',  encoding='utf-8') as f:
    intents = json.load(f)

correct = total = 0

for intent in intents['intents']:
    for pattern in intent['patterns']:
        result = predict_chat(pattern) 
        if result in intent["responses"]:
            correct += 1
        else:
            print(f"Incorrect: {pattern} -> {result}")

        total += 1

print(f"Bot accuracy: {round(correct / total * 100, 2)}%")