import random
import json
import torch

from model import NeuralNetwork
from nltk_utils import bag_of_words, tokenize
from textblob import TextBlob

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('backend/dataset/intents_cleaned.json', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "backend/dataset/trained_data.pth"
data = torch.load(FILE, weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# NN = 0.75, NN2 = 0.5
accept_probability = 0.4

import re
from nltk.corpus import stopwords

def clean_text(text):
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Optionally remove stopwords
    stop_words = set(stopwords.words('english'))
    
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text


def predict_chat(sentence: str):
    sentence = tokenize(clean_text(str(TextBlob(sentence.lower()).correct()))) # spelling correction before tokenize

    # vectorize word
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)

    prob = probs[0][predicted.item()]
    
    if prob.item() > accept_probability:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])

                from knn import get_cpu_recommendation, get_cooler_recommendation, get_gpu_recommendation, get_ssd_recommendation, get_hdd_recommendation, get_psu_recommendation, get_ram_recommendation, get_case_recommendation, get_monitor_recommendation, get_motherboard_recommendation

                if intent['tag']=="cpu_recommendation":
                    response+=get_cpu_recommendation()
                elif intent['tag']=="cpu_cooler_recommendation":
                    response+=get_cooler_recommendation()
                elif intent['tag']=="gpu_recommendation":
                    response+=get_gpu_recommendation()
                elif intent['tag']=="ssd_recommendation":
                    response+=get_ssd_recommendation()
                elif intent['tag']=="hdd_recommendation":
                    response+=get_hdd_recommendation()
                elif intent['tag']=="psu_recommendation":
                    response+=get_psu_recommendation()
                elif intent['tag']=="ram_recommendation":
                    response+=get_ram_recommendation()
                elif intent['tag']=="case_recommendation":
                    response+=get_case_recommendation()
                elif intent['tag']=="monitor_recommendation":
                    response+=get_monitor_recommendation()
                elif intent['tag']=="motherboard_recommendation":
                    response+=get_motherboard_recommendation() 

                return (response, intent["tag"])
    else:
        return ("Sorry, I can't understand you", "Failed");

    