import requests as http
from lib.connect import SpotifyConnect
from lib.network import get_next_song
import time
import os

os.environ['TOKEN'] = ''
app.run(host='0.0.0.0')

while os.environ['TOKEN'] == '':
    time.sleep(5)

spotify = SpotifyConnect(os.environ['TOKEN'])
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
        m.play_song(data['track_id'])
        start_time = time.time()
        pause_time = 0
        skip = False
        playing = True


