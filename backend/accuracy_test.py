from chatbot import predict_chat
import json

with open('backend/dataset/intents.json', 'r',  encoding='utf-8') as f:
    intents = json.load(f)

correct = total = 0

for intent in intents['intents']:
    for pattern in intent['patterns']:
        (result, tag) = predict_chat(pattern) 
        if tag == intent["tag"]:
            correct += 1
        else:
            print(f"Incorrect: {tag} -> Correct: {intent["tag"]}")

        total += 1

print(f"Bot accuracy: {round(correct / total * 100, 2)}%")