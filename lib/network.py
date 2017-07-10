import requests as http
import time

song_url = '127.0.0.1:5000/get_next_song'

def get_next_song():
    try:
        response = http.get(song_url)
    except http.exceptions.ConnectionError:
        print('unable to connect, waiting...')
        time.sleep(10)
        return get_next_song()
    data = response.json()
    while 'error' in data:
        print(data['error'])
        time.sleep(10)
        response = http.get(song_url)
        data = response.json()
    return data