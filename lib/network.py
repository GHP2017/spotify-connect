import requests as http
import time
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

song_url = 'http://127.0.0.1:5000/get_next_song'

def get_next_song():
    logging.info('getting the next song')
    try:
        response = http.get(song_url)
    except http.exceptions.ConnectionError:
        logging.info('unable to connect, waiting...')
        time.sleep(10)
        return get_next_song()
    logging.info('got a response')
    data = response.json()
    while 'error' in data:
        logging.info(data['error'])
        time.sleep(10)
        response = http.get(song_url)
        data = response.json()
    return data