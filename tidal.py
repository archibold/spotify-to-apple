import os
from dotenv import load_dotenv
import tidalapi

# import spotify
load_dotenv()

token_type = os.getenv('token_type')
access_token = os.getenv('access_token')
refresh_token = os.getenv('refresh_token')
expiry_time = os.getenv('expiry_time')

session = tidalapi.Session()
session.load_oauth_session(token_type, access_token, refresh_token, expiry_time)

user = session.user

playlist = user.playlists()[0]
# print(playlist.name)
# sp_tracks = spotify.get_all_saved_tracks()
# for sp_items in sp_tracks:
#     sp_track=sp_items['track']
#     td_track = session.search(query=f'{sp_track['artists'][0]['name']} – {sp_track['name']}')
#     if td_track['tracks']:
#         print(f'sp::{sp_track['artists'][0]['name']} – {sp_track['name']}')
#         print(f'ti::{td_track['tracks'][0].artist.name} - {td_track['tracks'][0].name}')
#         playlist.add([td_track['tracks'][0].id])
#     else:
#         print(f'no track for {sp_track['artists'][0]['name']} – {sp_track['name']}')
#     print('******')
# playlist.add()


def save_to_favorite(track_name):
    td_track = session.search(query=f'{track_name}')
    if td_track['tracks']:
        # print(f'sp::{sp_track['artists'][0]['name']} – {sp_track['name']}')
        # print(f'ti::{td_track['tracks'][0].artist.name} - {td_track['tracks'][0].name}')
        playlist.add([td_track['tracks'][0].id])
    else:
        print(f'no track for {track_name}')