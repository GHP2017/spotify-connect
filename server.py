from flask import Flask, redirect, request
import os
import requests as http
import json
import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)

auth_server = Flask(__name__)
client_id = 'f3b0c51df1124cc985fd4012b6d55d95'
client_secret = 'e54ca2e0bf394944a1247830443dba3c'
redirect_uri = 'http://127.0.0.1:5001/callback'
authorize_uri = 'https://accounts.spotify.com/authorize'
token_uri = 'https://accounts.spotify.com/api/token'

@auth_server.route('/')
def landing():
    return auth_server.send_static_file('index.html')

@auth_server.route("/callback")
def callback():
    code = request.args.get('code')
    result = http.post(token_uri, data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    })
    logging.info('token result')
    logging.info(result.json())
    dict = result.json()

    token = dict['access_token']
    os.environ['TOKEN'] = token

    return 'success'

@auth_server.route("/authenticate")
def authenticate():
    return redirect(authorize_uri + '?client_id=' + client_id + \
                    '&response_type=code&redirect_uri=' + redirect_uri + '&scope=user-library-read user-modify-playback-state')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@auth_server.route('/info', methods=['GET'])
def shutdown():
    if os.environ['TOKEN'] != '':
        shutdown_server()
        return json.dumps({'token': os.environ['TOKEN']})
    else:
        return json.dumps({'msg': 'not ready'})

if __name__ == "__main__":
    auth_server.run(port=5001)