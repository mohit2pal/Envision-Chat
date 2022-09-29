from flask import Flask, request, render_template, jsonify
import json

import os

# from Sol_prob import get_response

app = Flask(__name__)

@app.route('/')
def login():
    return "Got To the Route"
    
# @app.route('/predict', methods=['POST'])
# def predict():
#     text = request.get_json().get("message")
#     response = get_response(text)
#     print(response)
#     print(type(response))
#     message = {"answer": response}
#     return jsonify(message)

@app.route('/user1_chat')
def chat1():
    return render_template('index.html')

@app.route('/user2_chat')
def chat2():
    return render_template('index2.html')


@app.route('/user1', methods=['POST'])
def user1():
    text = request.get_json().get("message")
    message = {"name": "User", "message": text}
    return jsonify(message)

@app.route('/user2', methods=['POST'])
def user2():
    text = request.get_json().get("message")
    message = {"answer": text}
    return jsonify(message)
    
if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)