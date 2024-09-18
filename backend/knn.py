import json
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents.json
with open('backend/dataset/intents_cleaned.json', encoding='utf-8') as file:
    intents_data = json.load(file)

intents = intents_data['intents']
patterns = []

# Dictionary to map tags to responses
responses_dict = {}  
tags = []

# Load tags and responses into responses_dict
for intent in intents:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])
    responses_dict[intent['tag']] = intent['responses']

# Load CPU data
cpu_data = pd.read_csv('backend/dataset/CPUData.csv')
# Load Cooler data
cooler_data = pd.read_csv('backend/dataset/CPUCoolerData.csv')
# Load Case data
case_data = pd.read_csv('backend/dataset/CaseData.csv')
# Load GPU data
gpu_data = pd.read_csv('backend/dataset/GPUData.csv')
# Load HDD data
hdd_data = pd.read_csv('backend/dataset/HDDData.csv')
# Load Monitor data
monitor_data = pd.read_csv('backend/dataset/MonitorData.csv')
# Load Motherboard data
motherboard_data = pd.read_csv('backend/dataset/MotherboardData.csv')
# Load PSU data
psu_data = pd.read_csv('backend/dataset/PSUData.csv')
# Load RAM data
ram_data = pd.read_csv('backend/dataset/RAMData.csv')
# Load SSD data
ssd_data = pd.read_csv('backend/dataset/SSDData.csv')

#Remove duplicate
cpu_data.drop_duplicates(inplace=True)
gpu_data.drop_duplicates(inplace=True)
psu_data.drop_duplicates(inplace=True)
ram_data.drop_duplicates(inplace=True)
hdd_data.drop_duplicates(inplace=True)
monitor_data.drop_duplicates(inplace=True)
motherboard_data.drop_duplicates(inplace=True)
cooler_data.drop_duplicates(inplace=True)
case_data.drop_duplicates(inplace=True)


# Vectorize the patterns
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

#To classify the intents, determine which intent it is for the input
def classify_intent(input_text):
    input_vec = vectorizer.transform([input_text])
    similarities = cosine_similarity(input_vec, X).flatten()
    
    # Show full list tags similarities
    #print("Similarities:")
    #for tag, similarity in zip(tags, similarities):
    #    print(f"Tag: {tag}, Similarity: {similarity:.10f}")
    
    # Filter valid neighbors with similarity > 0.5
    threshold = 0.5
    valid_neighbors = [(tags[i], similarities[i]) for i in range(len(similarities)) if similarities[i] > threshold]
    valid_neighbors.sort(key=lambda x: x[1], reverse=True)
    
    # Show full list of valid neighbors
    #print("Similarities and tags of valid neighbors:")
    #for tag, similarity in valid_neighbors:
    #    print(f"Tag: {tag}, Similarity: {similarity:.10f}")
    
    if not valid_neighbors:
        return "nothing"
    
    #number of neighbors
    k=5
    top_k_neighbors = valid_neighbors[:k]
    
    # Count occurrences of each tag among valid neighbors
    tag_counts = {}
    for tag, _ in top_k_neighbors:
        if tag in tag_counts:
            tag_counts[tag] += 1
        else:
            tag_counts[tag] = 1
    
    # Find the tag with the highest count, KNN will choose the neighbor with most count
    predicted_tag = max(tag_counts, key=tag_counts.get)
    
    return predicted_tag

def get_cpu_recommendation():
    # Format CPU recommendations in a more readable format
    recommendations = cpu_data[['Name', 'Producer', 'Price', 'Base Clock', 'Turbo Clock', 'Unlocked Multiplier','Cores','Threads','TDP','Socket','Integrated GPU']].head()
    random_cpu = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_cpu['Name']}</li>"
        f"<li>Producer: {random_cpu['Producer']}</li>"
        f"<li>Price: {random_cpu['Price']}</li>"
        f"<li>Base Clock: {random_cpu['Base Clock']} GHz</li>"
        f"<li>Turbo Clock: {random_cpu['Turbo Clock']} GHz</li>"
        f"<li>Unlocked Multiplier: {'Yes' if random_cpu['Unlocked Multiplier'] else 'No'}</li>"
        f"<li>Cores: {random_cpu['Cores']}</li>"
        f"<li>Threads: {random_cpu['Threads']}</li>"
        f"<li>TDP: {random_cpu['TDP']} watts</li>"
        f"<li>Socket: {random_cpu['Socket']}</li>"
        f"<li>Integrated GPU: {random_cpu['Integrated GPU']}</li></ul>"
    )
    
    return response

def get_cooler_recommendation():
    # Format Cooler recommendations in a more readable format
    recommendations = cooler_data[['Name', 'Price', 'Producer', 'Supported Sockets', 'Height','80mm Fans','92mm Fans','120mm Fans','140mm Fans','200mm Fans', 'Additional Fan Support']].head()
    random_cooler = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_cooler['Name']}</li>"
        f"<li>Price: {random_cooler['Price']}</li>"
        f"<li>Producer: {random_cooler['Producer']}</li>"
        f"<li>Supported Sockets: {random_cooler['Supported Sockets']}</li>"
        f"<li>Height: {random_cooler['Height']}</li>"
        f"<li>Additional Fan Support: ${'Yes' if random_cooler['Additional Fan Support'] else 'No'}</li></ul>"
    )
    
    return response

def get_ram_recommendation():
    # Format RAM recommendations in a more readable format
    recommendations = ram_data[['Name','Price','Producer','Ram Type','Size','Clock','Timings','Sticks']].head()
    random_ram = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_ram['Name']}</li>"
        f"<li>Price: {random_ram['Price']}</li>"
        f"<li>Producer: {random_ram['Producer']}</li>"
        f"<li>RAM Type: {random_ram['Ram Type']}</li>"
        f"<li>Size: {random_ram['Size']}</li>"
        f"<li>Clock: {random_ram['Clock']}</li>"
        f"<li>Timings: {random_ram['Timings']}</li>"
        f"<li>Sticks: {random_ram['Sticks']}</li></ul>"
    )
    
    return response

def get_gpu_recommendation():
    # Format GPU recommendations in a more readable format
    recommendations = gpu_data[['Name','Price','Producer','Length','Slots','8-Pin Connectors','6-Pin Connectors','HDMI','DisplayPort','DVI','Boost Clock','Vram','Memory Clock','TDP']].head()
    random_gpu = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_gpu['Name']}</li>"
        f"<li>Price: {random_gpu['Price']}</li>"
        f"<li>Producer: {random_gpu['Producer']}</li>"
        f"<li>Length: {random_gpu['Length']}</li>"
        f"<li>Slots: {random_gpu['Slots']}</li>"
        f"<li>8-Pin Connectors: {random_gpu['8-Pin Connectors']}</li>"
        f"<li>6-Pin Connectors: {random_gpu['6-Pin Connectors']}</li>"
        f"<li>HDMI: {random_gpu['HDMI']}</li>"
        f"<li>DisplayPort: {random_gpu['DisplayPort']}</li>"
        f"<li>DVI: {random_gpu['DVI']}</li>"
        f"<li>Boost Clock: {random_gpu['Boost Clock']}</li>"
        f"<li>VRAM: {random_gpu['Vram']}</li>"
        f"<li>Memory Clock: {random_gpu['Memory Clock']}</li>"
        f"<li>TDP: {random_gpu['TDP']}</li></ul>"
    )
    
    return response

def get_ssd_recommendation():
    # Format SSD recommendations in a more readable format
    recommendations = ssd_data[['Name','Price','Producer','Form Factor','Protocol','Size','NAND','Controller']].head()
    random_ssd = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_ssd['Name']}</li>"
        f"<li>Price: {random_ssd['Price']}</li>"
        f"<li>Producer: {random_ssd['Producer']}</li>"
        f"<li>Form Factor: {random_ssd['Form Factor']}</li>"
        f"<li>Protocol: {random_ssd['Protocol']}</li>"
        f"<li>Size: {random_ssd['Size']}</li>"
        f"<li>NAND: {random_ssd['NAND']}</li>"
        f"<li>Controller: {random_ssd['Controller']}</li></ul>"
    )
    
    return response

def get_hdd_recommendation():
    # Format HDD recommendations in a more readable format
    recommendations = hdd_data[['Name','Price','Producer','Form Factor','Size','RPM','Cache','Product Page']].head()
    random_hdd = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_hdd['Name']}</li>"
        f"<li>Price: {random_hdd['Price']}</li>"
        f"<li>Producer: {random_hdd['Producer']}</li>"
        f"<li>Form Factor: {random_hdd['Form Factor']}</li>"
        f"<li>Size: {random_hdd['Size']}</li>"
        f"<li>RPM: {random_hdd['RPM']} RPM</li>"
        f"<li>Cache: {random_hdd['Cache']}</li></ul>"
    )
    
    return response

def get_psu_recommendation():
    # Format PSU recommendations in a more readable format
    recommendations = psu_data[['Name','Price','Producer','Watt','Size','Efficiency Rating']].head()
    random_psu = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_psu['Name']}</li>"
        f"<li>Price: {random_psu['Price']}</li>"
        f"<li>Producer: {random_psu['Producer']}</li>"
        f"<li>Watt: {random_psu['Watt']}W</li>"
        f"<li>Size: {random_psu['Size']}</li>"
        f"<li>Efficiency Rating: {random_psu['Efficiency Rating']}</li></ul>"
    )
    
    return response

def get_case_recommendation():
    # Format Case recommendations in a more readable format
    recommendations = case_data[['Name','Price','Producer','Width','Depth','Height','Motherboard','Power Supply','Primary Color(s)','Window','Dust Filter','Cable Management','Noise Isolation']].head()
    random_case = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_case['Name']}</li>"
        f"<li>Price: {random_case['Price']}</li>"
        f"<li>Producer: {random_case['Producer']}</li>"
        f"<li>Width: {random_case['Width']}</li>"
        f"<li>Depth: {random_case['Depth']}</li>"
        f"<li>Height: {random_case['Height']}</li>"
        f"<li>Motherboard Compatibility: {random_case['Motherboard']}</li>"
        f"<li>Power Supply Compatibility: {random_case['Power Supply']}</li>"
        f"<li>Primary Color(s): {random_case['Primary Color(s)']}</li>"
        f"<li>Window: {'Yes' if random_case['Window'] == 'TRUE' else 'No'}</li>"
        f"<li>Dust Filter: {'Yes' if random_case['Dust Filter'] == 'TRUE' else 'No'}</li>"
        f"<li>Cable Management: {'Yes' if random_case['Cable Management'] == 'TRUE' else 'No'}</li>"
        f"<li>Noise Isolation: {'Yes' if random_case['Noise Isolation'] == 'TRUE' else 'No'}</li></ul>"
    )
    
    return response

def get_monitor_recommendation():
    # Format Monitor recommendations in a more readable format
    recommendations = monitor_data[['Name','Price','Producer','Resolution','Refresh Rate','Size','Panel','Response Time','HDMI','DisplayPort','DVI','VGA','Speaker','Curved','Adjustable Height','Sync','Product Page']].head()
    random_monitor = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_monitor['Name']}</li>"
        f"<li>Price: {random_monitor['Price']}</li>"
        f"<li>Producer: {random_monitor['Producer']}</li>"
        f"<li>Resolution: {random_monitor['Resolution']}</li>"
        f"<li>Refresh Rate: {random_monitor['Refresh Rate']}</li>"
        f"<li>Size: {random_monitor['Size']}</li>"
        f"<li>Panel: {random_monitor['Panel']}</li>"
        f"<li>Response Time: {random_monitor['Response Time']}</li>"
        f"<li>HDMI Ports: {random_monitor['HDMI']}</li>"
        f"<li>DisplayPort: {random_monitor['DisplayPort']}</li>"
        f"<li>DVI Ports: {random_monitor['DVI']}</li>"
        f"<li>VGA Ports: {random_monitor['VGA']}</li>"
        f"<li>Speakers: {'Yes' if random_monitor['Speaker'] == 1 else 'No'}</li>"
        f"<li>Curved: {'Yes' if random_monitor['Curved'] == 'TRUE' else 'No'}</li>"
        f"<li>Adjustable Height: {'Yes' if random_monitor['Adjustable Height'] == 'TRUE' else 'No'}</li>"
        f"<li>Sync Technology: {'Yes' if random_monitor['Sync'] == 'TRUE' else 'No'}</li></ul>"
    )
    
    return response

def get_motherboard_recommendation():
    # Format Motherboard recommendations in a more readable format
    recommendations = motherboard_data[['Name','Price','Producer','Socket','Chipset','Unlocked','Form Factor','Memory Type','Memory Capacity','RAM Slots','SATA','VGA','DVI','Display Port','HDMI','WiFi','Integrated Graphics']].head()
    random_motherboard = recommendations.sample().iloc[0]
    
    response = (
        f"<br><ul><li>Name: {random_motherboard['Name']}</li>"
        f"<li>Price: {random_motherboard['Price']}</li>"
        f"<li>Producer: {random_motherboard['Producer']}</li>"
        f"<li>Socket: {random_motherboard['Socket']}</li>"
        f"<li>Chipset: {random_motherboard['Chipset']}</li>"
        f"<li>Unlocked: {'Yes' if random_motherboard['Unlocked'] == 'TRUE' else 'No'}</li>"
        f"<li>Form Factor: {random_motherboard['Form Factor']}</li>"
        f"<li>Memory Type: {random_motherboard['Memory Type']}</li>"
        f"<li>Memory Capacity: {random_motherboard['Memory Capacity']}</li>"
        f"<li>RAM Slots: {random_motherboard['RAM Slots']}</li>"
        f"<li>SATA Ports: {random_motherboard['SATA']}</li>"
        f"<li>VGA Ports: {random_motherboard['VGA']}</li>"
        f"<li>DVI Ports: {random_motherboard['DVI']}</li>"
        f"<li>Display Port: {random_motherboard['Display Port']}</li>"
        f"<li>HDMI Ports: {random_motherboard['HDMI']}</li>"
        f"<li>WiFi: {'Yes' if random_motherboard['WiFi'] == 'TRUE' else 'No'}</li>"
        f"<li>Integrated Graphics: {'Yes' if random_motherboard['Integrated Graphics'] == 'TRUE' else 'No'}</li></ul>"
    )
    
    return response

def generate_response(user_input):
    # Pre-processing
    user_input = user_input.lower().strip()  # Convert to lowercase and remove any extra spaces
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))
    intent = classify_intent(user_input)
    
    # View predicted intent
    #print(f"Predicted intent: {intent}")
    
    # If it is a valid intent, then a random response will be selected from the available response of the tag
    if intent in responses_dict:
        response = np.random.choice(responses_dict[intent])
        if intent=="cpu_recommendation":
            response+=get_cpu_recommendation()
        if intent=="cpu_cooler_recommendation":
            response+=get_cooler_recommendation()
        if intent=="gpu_recommendation":
            response+=get_gpu_recommendation()
        if intent=="ssd_recommendation":
            response+=get_ssd_recommendation()
        if intent=="hdd_recommendation":
            response+=get_hdd_recommendation()
        if intent=="psu_recommendation":
            response+=get_psu_recommendation()
        if intent=="ram_recommendation":
            response+=get_ram_recommendation()
        if intent=="case_recommendation":
            response+=get_case_recommendation()
        if intent=="monitor_recommendation":
            response+=get_monitor_recommendation()
        if intent=="motherboard_recommendation":
            response+=get_motherboard_recommendation()    
    else:
        response = "Sorry, I didn't understand that."
    
    # Return response
    return response

print("KNN run successfully!")
# Test the chatbot
#test_inputs = [
#    "recommend ssd",
#    "best hdd?",
#    "what is the best cooler for gaming? recommend one",
#    "recommend hdd"
#    "what is the best cpu for gaming? recommend one",
#    "recommend motherboard",
#    "recommend monitor",
#    "recommend psu",
#    "recommend case",
#    "recommend gpu"
#]

# for user_input in test_inputs:
#     response = generate_response(user_input)
#     print(f"You: {user_input}")
#     print(f"Chatbot: {response}\n")
