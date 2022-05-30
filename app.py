from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/callback', methods=['POST'])
def callback_post_request():
    print(json.dumps(request.json))
    return json.dumps(request.json), 200


@app.route('/')
def home():
    return "EENVEST CALLBACK POST REQUEST"


app.run()
