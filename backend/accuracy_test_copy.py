from knn import classify_intent
import json
import time

with open('backend/dataset/intents_cleaned.json', 'r',  encoding='utf-8') as f:
    intents = json.load(f)

correct = total = 0
print("\n")
print(f"{'Predicted Intent (x)':<30} | {'User Input':<50}| {'Expected Intent (y)':<30}")
print("-" * 110)
start_pred = time.time()
for intent in intents['intents']:
    for pattern in intent['patterns']:
        result = classify_intent(pattern) 
        if result in intent["tag"]:
            correct += 1
            print(f"{result:<30} | {pattern:<50}| {intent["tag"]:<30}")
        else:
            print(f"{result:<30} | {pattern:<50}| {intent["tag"]:<30} -->Incorrect!")
        total += 1
end_pred = time.time()
print("Accuracy and time taken based on trained data:")
print(f"Bot accuracy: {round(correct / total * 100, 2)}%")
print(f"Total Prediction time: {end_pred - start_pred:.6f} seconds")

#Test Plan Results
test_data = [
    "hi", "hello", "hey", "good morning", "good afternoon", "is anyone there?", "what's up?", "greetings",
    "thanks", "thank you", "that's helpful", "thanks for the help", "I appreciate it", "thanks a lot", 
    "thank you very much", "thanks for your assistance", "much appreciated", "bye", "goodbye", "see you later", 
    "talk to you soon", "farewell", "take care", "catch you later", "see you", "have a nice day",
    
    "what is cpu", "definition of cpu", "meaning of cpu", "what is central processing unit", 
    "definition of central processing unit", "meaning of central processing unit", "what is processor", 
    "definition of processor", "meaning of processor", "cpu explanation", "cpu purpose", "recommend a cpu", 
    "best cpu for gaming", "cpu for video editing", "recommend a central processing unit", 
    "best central processing unit for gaming", "central processing unit for video editing", 
    "recommend a processor", "best processor for gaming", "processor for video editing", 
    "top cpu for gaming", "cpu suggestions",
    
    "what is cpu cooler", "definition of cpu cooler", "meaning of cpu cooler", "cpu cooler function", 
    "why do I need a cpu cooler", "recommend a cpu cooler", "best cpu cooler for gaming", 
    "cpu cooler for video editing", "top cpu coolers", "cpu cooler suggestions",
    
    "what is case", "definition of case", "meaning of case", "what is a computer case", 
    "computer case purpose", "recommend a case", "suggest a case", "best computer case", 
    "top cases for PCs",
    
    "what is gpu", "definition of gpu", "meaning of gpu", "what is graphics processing units", 
    "definition of graphics processing units", "meaning of graphics processing units", "gpu purpose", 
    "gpu functionality", "recommend a gpu", "best gpu for gaming", "gpu for video editing", 
    "recommend a graphics processing units", "best graphics processing units for gaming", 
    "graphics processing units for video editing", "top gpu for gaming", "gpu suggestions",
    
    "what is hdd", "definition of hdd", "meaning of hdd", "what is hard disk drive", 
    "definition of hard disk drive", "meaning of hard disk drive", "hdd function", "hdd purpose", 
    "recommend a hdd", "suggest a hdd", "recommend a hard disk drive", "suggest a hard disk drive", 
    "best hdd for storage", "top hard drives",
    
    "what is ssd", "definition of ssd", "meaning of ssd", "what is solid-state drive", 
    "definition of solid-state drive", "meaning of solid-state drive", "ssd function", "ssd purpose", 
    "recommend a ssd", "suggest a ssd", "recommend a solid-state drive", "suggest a solid-state drive", 
    "best ssd for performance", "top solid-state drives",
    
    "what is ram", "definition of ram", "meaning of ram", "what is random access memory", 
    "definition of random access memory", "meaning of random access memory", "ram function", "ram purpose", 
    "recommend a ram", "suggest a ram", "recommend a random access memory", "suggest a random access memory", 
    "best ram for gaming", "top ram options",
    
    "what is psu", "definition of psu", "meaning of psu", "what is power supply unit", 
    "definition of power supply unit", "meaning of power supply unit", "psu function", "psu purpose", 
    "recommend a psu", "suggest a psu", "recommend a power supply unit", "suggest a power supply unit", 
    "best psu for gaming", "top power supply units",
    
    "what is monitor", "definition of monitor", "meaning of monitor", "computer monitor purpose", 
    "monitor function", "recommend a monitor", "suggest a monitor", "best monitor for gaming", 
    "top monitor options", "monitor suggestions",
    
    "what is motherboard", "definition of motherboard", "meaning of motherboard", "motherboard function", 
    "motherboard purpose", "recommend a motherboard", "suggest a motherboard", "best motherboard for gaming", 
    "top motherboard options",
    
    "how to build a PC", "assemble a custom PC system", "build a personal computer from scratch", 
    "develop a computer for specialized tasks", "steps to build a PC", "what do I need to build a computer?", 
    "how to assemble a PC", "DIY PC building guide", "guide to building a PC", "custom PC assembly instructions",
    
    "how could you help me", "what could you do", "what could you do to assist me", "what you can do", 
    "what help you provide", "how you can be helpful", "what support is offered", "how can you assist me", 
    "what services do you offer",
    
    "fuck you", "stupid"
]
correct_intent=[
  "greeting",
  "greeting",
  "greeting",
  "greeting",
  "greeting",
  "greeting",
  "greeting",
  "greeting",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "thanks",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "goodbye",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "definition_cpu",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "cpu_recommendation",
  "definition_cooler",
  "definition_cooler",
  "definition_cooler",
  "definition_cooler",
  "definition_cooler",
  "cpu_cooler_recommendation",
  "cpu_cooler_recommendation",
  "cpu_cooler_recommendation",
  "cpu_cooler_recommendation",
  "cpu_cooler_recommendation",
  "definition_case",
  "definition_case",
  "definition_case",
  "definition_case",
  "definition_case",
  "case_recommendation",
  "case_recommendation",
  "case_recommendation",
  "case_recommendation",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "definition_gpu",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "gpu_recommendation",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "definition_hdd",
  "hdd_recommendation",
  "hdd_recommendation",
  "hdd_recommendation",
  "hdd_recommendation",
  "hdd_recommendation",
  "hdd_recommendation",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "definition_ssd",
  "ssd_recommendation",
  "ssd_recommendation",
  "ssd_recommendation",
  "ssd_recommendation",
  "ssd_recommendation",
  "ssd_recommendation",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "definition_ram",
  "ram_recommendation",
  "ram_recommendation",
  "ram_recommendation",
  "ram_recommendation",
  "ram_recommendation",
  "ram_recommendation",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "definition_psu",
  "psu_recommendation",
  "psu_recommendation",
  "psu_recommendation",
  "psu_recommendation",
  "psu_recommendation",
  "psu_recommendation",
  "definition_monitor",
  "definition_monitor",
  "definition_monitor",
  "definition_monitor",
  "definition_monitor",
  "monitor_recommendation",
  "monitor_recommendation",
  "monitor_recommendation",
  "monitor_recommendation",
  "monitor_recommendation",
  "definition_motherboard",
  "definition_motherboard",
  "definition_motherboard",
  "definition_motherboard",
  "definition_motherboard",
  "motherboard_recommendation",
  "motherboard_recommendation",
  "motherboard_recommendation",
  "motherboard_recommendation",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "question_build_pc",
  "options",
  "options",
  "options",
  "options",
  "options",
  "options",
  "options",
  "options",
  "options",
  "nothing",
  "nothing"
]

correct_count = 0
total = len(correct_intent)
print("\n")
print(f"{'Predicted Intent (x)':<30} | {'User Input':<50}| {'Expected Intent (y)':<30}")
print("-" * 110)
start_pred = time.time()
for i in range(total):
    # Check if prediction matches the actual intent and if it's a valid intent
    predicted=classify_intent(test_data[i].lower().strip())
    if predicted == correct_intent[i]:
        correct_count += 1
        print(f"{predicted:<30} | {test_data[i]:<50}| {correct_intent[i]:<30}")
    else:
        print(f"{predicted:<30} | {test_data[i]:<50}| {correct_intent[i]:<30} --> Incorrect!")
end_pred = time.time()
accuracy = correct_count / total * 100
print("\nAccuracy and Time taken for test plan data:")
print(f"Bot accuracy: {round(accuracy, 2)}%")
print(f"Total Prediction time: {end_pred - start_pred:.6f} seconds")
