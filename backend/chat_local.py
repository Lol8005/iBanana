from chatbot import predict_chat

print("Let's chat! (type 'quit' to exit)")

while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    print(predict_chat(sentence))