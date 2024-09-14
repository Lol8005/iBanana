# Source: https://www.youtube.com/watch?v=zsYIw6RXjfM

from flask import Flask, render_template, request, jsonify
from chatbot import predict_chat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/conversation", methods=["POST"])
def convesation():
    # passed data
    data = request.get_json()

    prediction = predict_chat(data["user_response"])

    print(data["user_response"] + " -> " + prediction)

    response = {
        "bot_response": prediction
    }

    return jsonify(response), 201


if __name__ == "__main__":
    app.run(debug=True, port=8888)