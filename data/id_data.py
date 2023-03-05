import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# sets up the credentials
client_credentials_manager = SpotifyClientCredentials(config.client_id, config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# get playlist_id from user
def get_playlist():
    url = input("Enter Playlist URL > \n")
    playlist_id = url.split('/')[-1].split('?')[0]
    print(playlist_id)
    # playlist_id = "5oqCWuHcpkcf9be6WqL3n8"
    return playlist_id


# gets all the tracks in the playlist
playlist_id = get_playlist()
results = sp.playlist_items(playlist_id)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# gets all the track IDs
track_ids = []
for track in tracks:
    if track['track']:
        track_id = track['track']['id']
        track_ids.append(track_id)
print(track_ids)
print(len(track_ids))
