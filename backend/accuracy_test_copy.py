from knn import classify_intent
import json
import time

with open('backend/dataset/intents_cleaned.json', 'r',  encoding='utf-8') as f:
    intents = json.load(f)

correct = total = 0

start_pred = time.time()
for intent in intents['intents']:
    for pattern in intent['patterns']:
        result = classify_intent(pattern) 
        if result in intent["tag"]:
            correct += 1
        else:
            print(f"Incorrect: {pattern} -> {result}")

        total += 1
end_pred = time.time()

print(f"Bot accuracy: {round(correct / total * 100, 2)}%")
print(f"Total Prediction time: {end_pred - start_pred:.6f} seconds")