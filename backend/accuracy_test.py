from chatbot import predict_chat
import json
import time

with open('backend/dataset/intents.json', 'r',  encoding='utf-8') as f:
    intents = json.load(f)

correct = total = 0
start_pred = time.time()

for intent in intents['intents']:
    for pattern in intent['patterns']:
        (result, tag) = predict_chat(pattern) 
        if tag == intent["tag"]:
            correct += 1

            print(f"")
        else:
            print(f"Incorrect: {tag} -> Correct: {intent["tag"]}")

        total += 1

print(f"Bot accuracy: {round(correct / total * 100, 2)}%")
print(f"Total Prediction time: {time.time() - start_pred:} seconds")