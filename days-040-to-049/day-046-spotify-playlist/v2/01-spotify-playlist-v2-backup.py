# --- Import the required libraries / modules:
from bs4 import BeautifulSoup
import datetime
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# =======================================================================================
# =                               Web scraping section                                  =
# =======================================================================================

# --- Defince required variables:
base_url_to_scrap = "https://www.billboard.com/charts/hot-100"
# date_to_use = "2012-02-23"

# --- Ask the user which date they would like to look up:
def get_date_to_use():
    date_correct = False
    while date_correct is False:
        date_format = "%Y-%m-%d"
        date_from_user = input("Which year you would like to travel to in? YYYY-MM-DD: ")
        try:
            datetime.datetime.strptime(date_from_user, date_format)
            date_correct = True
            return date_from_user
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")

date_to_use = get_date_to_use()

# --- Define a variable to join the base_url)to_scrape and the date_to_use to give the complete URL:
full_url_to_scrape = f"{base_url_to_scrap}/{date_to_use}"

# A little message to show the full URL:
print(f"\nScraping Top 100 songs from: {full_url_to_scrape}\n")

# --- Open the site and assign it to a variable:
site_response = requests.get(full_url_to_scrape)

# --- Parse the page using BeautifulSoupL:
soup = BeautifulSoup(site_response.text, "html.parser")

# --- Find all h3 tags with a class of lrv-u-font-size-16. They will be added to a list:
top_100_songs = soup.select(selector="h3" ".lrv-u-font-size-16")

# --- get the song names only and strip out the \n's:
songs = []
for song in top_100_songs:
    songs.append(song.getText("h3").strip("\n"))


# =======================================================================================
# =                                  Spotify section                                    =
# =======================================================================================

# --- Define the variables required for authentication. These are acquired from env. variables:
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
client_redirect_url = os.environ.get("SPOTIPY_REDIRECT_URI")

# --- Define a name for the playlist:
playlist_name = print(f"Top-100-{date_to_use}")

# Scope details: https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private
# --- Use the Spotify API scope that allows for private playlist modifications:
scope = "playlist-modify-private"

# --- Authenticate against the API and get an oauth2 token:
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret = client_secret, redirect_uri = client_redirect_url, scope=scope))

# --- Get the current username for use later on:
current_user = sp.current_user()["id"]
# print(current_user)

# --- Create a new playlist and get its ID for use later on:
create_test_playlist = sp.user_playlist_create(user = current_user, name = playlist_name, description="Test", public=False)
create_test_playlist_id = create_test_playlist["id"]
create_test_playlist_name = create_test_playlist["name"]
print(create_test_playlist)

print(f"\nAdding Songs To Playlist: {create_test_playlist_name}\n========================================================\n")

# --- Search for each song in the songs list, get the Spotify ID for it and add it to the songs_to_add list:
for song in songs:
    # --- Create / clear a list to add the song ID to:
    song_to_add = []
    
    # --- Search for a song and if it can't be found, error out:
    try:
        spotify_song = sp.search(song,limit=1, type = "track")
    except IndexError:
        print("Song could not be found")
    
    # --- If the song is found, add it to the song_to_add list and add it to the playlist:
    else:
        spotify_song_id = spotify_song['tracks']['items'][0]['id']
        song_to_add.append(spotify_song_id)
        print(f"Adding {spotify_song['tracks']['items'][0]['name']} by {spotify_song['tracks']['items'][0]['artists'][0]['name']}")
        sp.user_playlist_add_tracks(user=current_user, playlist_id = create_test_playlist_id, tracks = song_to_add)

# --- Print out a friendly message with the URL for the playlist:
print(f"Your playlist, {playlist_name}, is available to listen to at:\n{create_test_playlist['external_urls']['spotify']}")