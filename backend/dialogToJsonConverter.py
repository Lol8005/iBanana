import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load the dataset
def load_dataset(file_path):
    data = pd.read_csv(file_path, delimiter="\t", names=["question", "answer"])
    return data

# Function to assign a relevant tag based on both the question and answer
def generate_tags(questions, num_clusters=10):
    # Vectorize the questions using TF-IDF for clustering
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(questions)
    
    # Apply KMeans to cluster questions into `num_clusters` groups
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    # Create tags based on the clusters
    tags = [f"intent_{i}" for i in kmeans.labels_]
    return tags

# Group the data by intent tags
def create_intent_structure(data, tags):
    intents = {}
    
    for i, row in data.iterrows():
        question = row['question']
        answer = row['answer']
        tag = tags[i]
        
        if tag not in intents:
            intents[tag] = {
                "tag": tag,
                "patterns": [],
                "responses": []
            }
        
        if question not in intents[tag]["patterns"]:
            intents[tag]["patterns"].append(question)
        
        intents[tag]["responses"].append(answer)
    
    return list(intents.values())

# Save the intents structure to a JSON file
def save_to_json(intents, file_path):
    with open(file_path, 'w') as f:
        json.dump({"intents": intents}, f, indent=4)

# Main function to convert the dataset to intent-based format
def convert_to_intent_based_format(input_file, output_file, num_clusters=10):
    # Step 1: Load dataset
    data = load_dataset(input_file)
    
    # Step 2: Generate tags using clustering on questions
    tags = generate_tags(data['question'], num_clusters)
    
    # Step 3: Create intents structure
    intents = create_intent_structure(data, tags)
    
    # Step 4: Save the intents to JSON file
    save_to_json(intents, output_file)

# Example usage:
input_file = 'dataset/dialogs.txt'
output_file = 'dataset/intents.json'
convert_to_intent_based_format(input_file, output_file, 3000)
