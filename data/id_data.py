import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# sets up the credentials
client_credentials_manager = SpotifyClientCredentials(config.client_id, config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# get playlist_id from user
def get_playlist():
    url = input("Enter Playlist URL > \n")
    playlist_id = url.split('/')[-1].split('?')[0]
    print(playlist_id)
    return playlist_id


# gets all the tracks in the playlist
def get_tracks(playlist_id):
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# gets all the track IDs
def get_track_ids(tracks):
    track_ids = []
    for track in tracks:
        if track['track']:
            track_id = track['track']['id']
            track_ids.append(track_id)

    print(track_ids)
    print(len(track_ids))
    return track_ids


# get audio features of the tracks
def get_audio_features(track_ids):
    audio_features = sp.audio_features(track_ids)
    print(audio_features)
    return audio_features


# create new df using audio features
def new_df(audio_features, type):
    df = pd.DataFrame.from_records(audio_features)
    if type == 0:  # good songs
        df.to_csv('data/good_songs.csv')
    else:  # bad songs
        df.to_csv('data/bad_songs.csv')


# add to existing list (good/bad)
def existing_df(audio_features, type):
    if type == 0:
        df = pd.read_csv('data/good_songs.csv')
    else:
        df = pd.read_csv('data/bad_songs.csv')

    df = df.append(audio_features, ignore_index=True)

    if type == 0:  # good songs
        df.to_csv('data/good_songs.csv')
    else:  # bad songs
        df.to_csv('data/bad_songs.csv')
