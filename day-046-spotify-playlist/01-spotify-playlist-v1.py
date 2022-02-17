# --- Import the required libraries / modules:
from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# =======================================================================================
# =                               Web scraping section                                  =
# =======================================================================================

# --- Defince required variables:
base_url_to_scrap = "https://www.billboard.com/charts/hot-100"

# --- Ask the user which date they would like to look up:
date_to_use = input("Which year you would like to travel to in? YYYY-MM-DD: ")

# --- Define a vaviable to join the base_url)to_scrape and the date_to_use to give the complete URL:
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

# Scope details: https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private
# --- Use the Spotify API scope that allows for private playlist modifications:
scope = "playlist-modify-private"

# --- Authenticate against the API and get an oauth2 token:
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret = client_secret, redirect_uri = client_redirect_url, scope=scope))

# --- Get the current username for use later on:
current_user = sp.current_user()

# --- Create a new playlist and get its ID for use later on:
create_test_playlist = sp.user_playlist_create(user = current_user, name = f"Top-100-{date_to_use}", description="Test", public=False)
create_test_playlist_id = create_test_playlist["id"]
create_test_playlist_name = create_test_playlist["name"]

# --- Create a blank list to add the song ID's to:
songs_to_add = []

# --- Search for each song in the songs list, get the Spotify ID for it and add it to the songs_to_add list:
for song in songs:
    spotify_song = sp.search(song,limit=1, type = "track")
    spotify_song_id = spotify_song['tracks']['items'][0]['id']
    songs_to_add.append(spotify_song_id)
    # **** move the list into the for loop.
    # **** add the print to show the track being added
    # **** add the song to the list (only one song at a time)
    # **** Add the list / song to the playlist
    
# --- Add the songs to the playlist:
print(f"Adding Songs To Playlist: {create_test_playlist_name}")
sp.user_playlist_add_tracks(user=current_user, playlist_id = create_test_playlist_id, tracks = songs_to_add)