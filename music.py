# from spotify import get_all_saved_tracks
from tidal import save_to_favorite
#
# tracks = get_all_saved_tracks()
#
# for idx, item in enumerate(tracks):
#     track = item['track']
#     print(f"{track['artists'][0]['name']} – {track['name']}")

# 1. reverse file mu
# 2. add tracks to tidal

with open('mu2.txt') as file:
    for line in reversed(list(file)):
        # print(line.rstrip())
        save_to_favorite(line)