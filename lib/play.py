from lib.network import get_next_song
import time
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

def play_loop(queue, spotify):
    logging.info('starting up')
    # establish a connection
    data = get_next_song()
    logging.info(data)
    duration = data['duration'] / 1000.0
    start_time = time.time()
    spotify.play_song(data['track_id'])
    skip = False
    paused = False
    paused_at = time.time()
    pause_time = 0

    # main loop
    while True:
        if not queue.empty():
            user_input = queue.get_nowait()
            if user_input == 'pause':
                # pause the playback
                spotify.pause()
                paused = True
                paused_at = time.time()
            if user_input == 'resume':
                # resume the playback
                spotify.resume()
                paused = False
                pause_time = time.time() - paused_at
            if user_input == 'skip':
                # skip to next song
                skip = True
                pause_time = 0
                paused = False
            else:
                print('given command not understood')

        if (time.time() - start_time + pause_time >= duration and not paused) or skip:
            data = get_next_song()
            duration = data['duration'] / 1000.0
            spotify.play_song(data['track_id'])
            print('Playing ' + data['name'])
            start_time = time.time()
            pause_time = 0
            skip = False
