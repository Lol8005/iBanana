# Source: https://www.youtube.com/watch?v=zsYIw6RXjfM

from flask import Flask, request, jsonify
from flask_cors import CORS
from knn import generate_response
from chatbot import predict_chat

app = Flask(__name__)
CORS(app)

@app.route("/conversation", methods=["POST"])
def convesation():
    # passed data
    data = request.get_json().get("message")

    prediction = predict_chat(data)

    print(data + " -> " + prediction)

    response = {
        "bot_response": prediction
    }

    return jsonify(response), 201

@app.route("/conversation2", methods=["POST"])
def convesation():
    # passed data
    data = request.get_json().get("message")

    prediction = generate_response(data)

    print(data + " -> " + prediction)

    response = {
        "bot_response": prediction
    }

    return jsonify(response), 201


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8888)