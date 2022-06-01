from flask import Flask, render_template, request
import json
import os

app = Flask(__name__, static_folder='static')


@app.route('/jobstatus/<jobuuid>', methods=['POST'])
def callback(jobuuid):
    print({"msg": f"job id {jobuuid} is done!"})
    f = open("static/status.txt", "a")
    f.write(f"{jobuuid}\n\r")
    f.close()
    return {"msg": f"job id {jobuuid} is done!"}


@app.route('/jobCreate/<jobuuid>', methods=['POST'])
def callbackCreate(jobuuid):
    print({"msg": f"job id {jobuuid} is created!"})
    f = open("static/job.txt", "a")
    f.write(f"{jobuuid}\n\r")
    f.close()
    return {"msg": f"job id {jobuuid} is created!"}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/callback', methods=['POST'])
def callback_post_request():
    f = open("static/body.txt", "w")
    f.write(json.dumps(request.json))
    f.close()
    print(json.dumps(request.json))
    return json.dumps(request.json)


@app.route('/reset', methods=['GET'])
def reset_get_request():
    f = open("static/body.txt", "w")
    f.write(json.dumps("{}"))
    f.close()
    print(json.dumps(request.json))
    return json.dumps(request.json)

@app.route('/test', methods=['POST'])
def test():
    import requests
    url = "https://gl-web-04.iesve.com/iCIM-QA06/cim/action/callback/ae0e0b4e-2c91-44b0-9fae-fdd0d811494a"
    payload = json.dumps({"test": 1})
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        print(response.status_code)
        return response.text,200
    except Exception as e:
        print(e)
        return str(e),500
    

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
