# SpotiMuse

## About
This project is a Spotify recommendation system that predicts whether a user will like a new song/playlist. It uses the Spotify API to extract data about the user's playlists and the audio features of each track in the playlist. This data is then used to train a machine learning model to create a prediction of whether a user will like a new song/playlist.

---
## Table of Contents
1. [Project Description](#desc) <br>
2. [Getting Started](#start) <br>
3. [Usage](#usage) <br>
4. [Data](#data) <br> 
5. [Modelling](#model) <br>
6. [Results](#results) <br>
7. [Contributing](#contribution) <br>
8. [License](#license)


<a name="desc"/></a>
## Project Description
SpotiMuse is a Spotify recommendation system that uses machine learning to identify songs you'll like based on your listening habits. By analyzing songs you've liked in the past, SpotiMuse will recommened new songs that appeal to you.

<a name="start"/></a>
## Getting Started
To get started with this project, you will need to have a Spotify Developer account and be authorized to access the Spotify API. You will also need to have Python 3 installed on your machine.

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command in your terminal:
<br>```pip install -r requirements.txt```
3. Create a config.py file in the data directory of the project and add your Spotify API credentials as follows:
    ```
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'your_redirect_uri'
    ```
4. Run the main.py file in your terminal to start the program.

<a name="usage"/></a>
## Usage
When you run the main.py file, the program will prompt you to enter your Spotify username. Once you enter your username, the program will access your Spotify account using the Spotify API and retrieve information about your playlists.

It will then extract the track IDs for each song in the playlist and use these IDs to retrieve the audio features for each track from the Spotify API. This data is added to a pandas dataframe and used to train a machine learning model.

The machine learning model predicts whether you will like a new song/playlist based on the audio features of the tracks in your existing playlists. You can use this model to get recommendations for new songs/playlists that you might like.

<a name="data"/></a>
## Data
To get the song IDs from a playlist:
https://developer.spotify.com/console/get-playlist-tracks/

<a name="model"/></a>
## Modelling

<a name="results"/></a>
## Results

<a name="contribution"/></a>
## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open an issue if you encounter any problems or have any suggestions for improving the project.

<a name="license"/></a>
## License
This project is licensed under the MIT License. See the LICENSE file for details.