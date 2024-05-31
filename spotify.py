import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
scope = "user-library-read"


def get_all_saved_tracks(limit_step=50):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    tracks = []
    o_num = 0
    try:
        for offset in range(0, 1000000, limit_step):
            o_num = offset
            response = sp.current_user_saved_tracks(
                limit=limit_step,
                offset=offset,
            )
            if len(response) == 0:
                break
            tracks += response['items']
            # for idx, item in enumerate(response['items']):
            #     track = item['track']
            #     print(f"{track['artists'][0]['name']} – {track['name']}")
            time.sleep(3)
        return tracks
    except:
        print(f'::{o_num}')




