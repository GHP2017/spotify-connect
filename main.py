import requests as http
from lib.connect import SpotifyConnect
from lib.network import get_next_song
from server import auth_server
from subprocess import Popen
import time
import os

os.environ['TOKEN'] = ''
proc = Popen(['python server.py'], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
#auth_server.run(host='0.0.0.0')

while os.environ['TOKEN'] == '':
    print('got here?')
    time.sleep(5)

##TODO:
# get token from server. make it a shutdown endpoint that returns the token

spotify = SpotifyConnect(token)

# establish a connection
data = get_next_song()
duration = data['duration'] / 1000.0
start_time = time.time()
spotify.play_song(data['track_id'])
playing = True

# main loop
while True:
    if time.time() - start_time >= duration:
        data = get_next_song()
        duration = data['duration'] / 1000.0
        spotify.play_song(data['track_id'])
        start_time = time.time()
        pause_time = 0
        skip = False
        playing = True


