import requests as http
import json
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

play_uri = 'https://api.spotify.com/v1/me/player/play'
pause_uri = 'https://api.spotify.com/v1/me/player/pause'
playback_url = 'http://127.0.0.1:5000/playback?state='

class SpotifyConnect:
    
    def __init__(self, token):
        logging.info(token)
        self.token = token

    def play_song(self, track_id):
        logging.info(track_id)
        body = json.dumps({'uris': ['spotify:track:' + track_id]})
        logging.info(body)
        resp = http.put(play_uri, data=body, headers={'Authorization': 'Bearer ' + self.token})
        logging.info(resp.request.body)

    def pause(self):
        http.put(pause_uri, headers={'Authorization': 'Bearer ' + self.token})
        http.get(playback_url + 'paused')

    def resume(self):
        http.put(play_uri, headers={'Authorization': 'Bearer ' + self.token})
        http.get(playback_url + 'resume')