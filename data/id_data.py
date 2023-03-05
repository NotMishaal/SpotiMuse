import requests
import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# url = "https://accounts.spotify.com/api/token"
# data = {
#     "grant_type": "authorization_code",
#     "code": config.code,
#     "redirect_uri": config.redirect_uri,
#     "client_id": config.client_id,
#     "client_secret": config.client_secret
# }
#
# response = requests.post(url, data=data)
# access_token = response.json()["access_token"]
#
# headers = {
#     f"Authorization: Bearer {access_token}"
# }

client_credentials_manager = SpotifyClientCredentials(config.client_id, config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = "5oqCWuHcpkcf9be6WqL3n8"

results = sp.playlist_tracks(playlist_id)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Get track IDs
track_ids = [track['track']['id'] for track in tracks if track['track']]
print(track_ids)

# song_ids = []
# url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
# params = {
#     "fields": "items(tracks(id))",
#     "limit": 100
# }
#
# while url:
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()
#     tracks = data["items"]
#     for track in tracks:
#         song_id = track["track"]["id"]
#         song_ids.append(song_id)
#     url = data["next"]

# print(song_ids)
