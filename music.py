from spotify import get_all_saved_tracks

tracks = get_all_saved_tracks()

for idx, item in enumerate(tracks):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])