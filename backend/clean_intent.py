import json
import re
from nltk.corpus import stopwords

# Load the intents.json file
with open('backend/dataset/intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

def clean_text(text):
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Optionally remove stopwords
    stop_words = set(stopwords.words('english'))
    
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Clean the patterns and responses in the intents file
for intent in intents['intents']:
    intent['patterns'] = [clean_text(pattern) for pattern in intent['patterns']]

# Save the cleaned file
with open('backend/dataset/intents_cleaned.json', 'w') as f:
    json.dump(intents, f, indent=4)
