import requests as http
from lib.connect import SpotifyConnect
from lib.network import get_next_song
from multiprocessing import Process, Queue
from subprocess import Popen
from lib.play import play_loop
import time
import os
import sys

os.environ['TOKEN'] = ''
Popen(['python', 'server.py'])
url = 'http://127.0.0.1:5001/info'

print('spotify connection extension for Auxilia booting up')
print('visit ' + url.strip('info') + ' to login to spotify')

token = ''

while token == '':
    print('waiting for user login...')
    time.sleep(5)
    resp = http.get(url).json()
    token = resp.get('token', '')

print('user logged in')
print('playback started.')
print('available commands are pause, resume, and skip.')
spotify = SpotifyConnect(token)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=play_loop, args=(q, spotify))
    p.start()
    while True:
        q.put(input())