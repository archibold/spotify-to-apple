import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
scope = "user-library-read"


def get_all_saved_tracks(limit_step=5):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    tracks = []
    for offset in range(0, 5, limit_step):
        print('###########################################')
        response = sp.current_user_saved_tracks(
            limit=limit_step,
            offset=offset,
        )
        if len(response) == 0:
            break
        tracks += response['items']


    return tracks




