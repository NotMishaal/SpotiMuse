import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# sets up the credentials
client_credentials_manager = SpotifyClientCredentials(config.client_id, config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# get playlist_id from user
def get_playlist():
    while True:
        url = input("Enter Playlist URL > \n")
        playlist_id = url.split('/')[-1].split('?')[0]
        if playlist_id:
            print(playlist_id)
            return playlist_id
        else:
            print("Invalid input. Please enter a valid playlist URL.")


# gets all the tracks in the playlist
def get_tracks(playlist_id):
    tracks = []
    try:
        results = sp.playlist_items(playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
    except Exception as e:
        print("Error occurred while fetching playlist tracks:", e)
    return tracks


# gets all the track IDs
def get_track_ids(tracks):
    track_ids = [track['track']['id'] for track in tracks if track['track'] and track['track']['id']]
    print(track_ids)
    print(len(track_ids))
    return track_ids


# get audio features of the tracks
def get_audio_features(track_ids):
    audio_features = []
    try:
        for i in range(0, len(track_ids), 50):
            features = sp.audio_features(track_ids[i:i + 50])
            audio_features.extend(features)
    except Exception as e:
        print("Error occurred while fetching audio features:", e)
    return audio_features


# create new df using audio features
def new_df(audio_features, type):
    df = pd.DataFrame.from_records(audio_features)
    if type == 0:  # good songs
        df.to_csv('good_songs.csv', index=False)
    else:  # bad songs
        df.to_csv('bad_songs.csv', index=False)


# add to existing list (good/bad)
def existing_df(audio_features, type):
    if type == 0:
        file_path = 'good_songs.csv'
    else:
        file_path = 'bad_songs.csv'

    try:
        df = pd.read_csv(file_path)
        df = df.append(audio_features, ignore_index=True)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print("Error occurred while updating existing DataFrame:", e)


if __name__ == "__main__":
    playlist_id = get_playlist()
    tracks = get_tracks(playlist_id)
    track_ids = get_track_ids(tracks)
    audio_features = get_audio_features(track_ids)
    new_df(audio_features, 0)  # create new df for good songs
