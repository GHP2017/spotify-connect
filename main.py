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


token = ''

while token == '':
    print('waiting...')
    time.sleep(5)
    resp = http.get(url).json()
    token = resp.get('token', '')

spotify = SpotifyConnect(token)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=play_loop, args=(q, spotify))
    p.start()
    while True:
        a = input()
        if a == 'stop':
            p.join()
            sys.exit()
        else:
            q.put(a)