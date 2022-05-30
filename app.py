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

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
