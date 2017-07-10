import requests as http

play_uri = 'https://api.spotify.com/v1/me/player/play'
pause_uri = 'https://api.spotify.com/v1/me/player/pause'

class SpotifyConnect:
    
    def __init__(self, token):
        pass

    def play_song(self, track_id):
        resp = http.put(play_uri, headers={'Authorization': 'Bearer ' + os.environ['TOKEN']})
        print(resp.text)