from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

def create_spotify_playlist(songs: list, date_to_use: str):
    
    """This function will create a Spotify playlist and add the songs in the songs list.
    Required arguments: songs (list) and date_to_use (string in the format YYYY-MM-DD)."""
    
    # --- Define the variables required for authentication. They are acquired from env. variables:
    client_id = os.environ.get("SPOTIPY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
    client_redirect_url = os.environ.get("SPOTIPY_REDIRECT_URI")
    
    # --- Define a name for the playlist:
    playlist_name = f"Top-100-{date_to_use}"

    # Scope details: https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private
    # --- Use the Spotify API scope that allows for private playlist modifications:
    scope = "playlist-modify-private"

    # --- Authenticate against the API and get an oauth2 token:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id,
                                                   client_secret = client_secret, 
                                                   redirect_uri = client_redirect_url, 
                                                   scope=scope))

    # --- Get the current username for use later on:
    current_user = sp.current_user()["id"]

    # --- Create a new playlist and get its ID for use later on:
    create_test_playlist = sp.user_playlist_create(user = current_user, 
                                                   name = playlist_name, 
                                                   description="Test", 
                                                   public=False)
    
    create_test_playlist_id = create_test_playlist["id"]
    create_test_playlist_name = create_test_playlist["name"]
    create_test_playlist_url = create_test_playlist['external_urls']['spotify']

    print(f"\nAdding Songs To Playlist: \033[1;32;40m{create_test_playlist_name}\n\033[1;37;40m========================================================\n")

    # --- Search for each song in the songs list, get the Spotify ID for it and add it to the songs_to_add list:
    for song in songs:
        # --- Create / clear a list to add the song ID to:
        song_to_add = []
        
        # --- Search for a song and if it can't be found, error out:
        try:
            spotify_song = sp.search(song,limit=1, type = "track")
        
        # --- If the song is not found, print out a message to that effect:
        except:
            print(f"\033[1;31;40mERROR\033[1;37;40m:Song could not be found.")
        
        # --- If the song is found, add it to the song_to_add list and add it to the playlist:
        else:
            spotify_song_id = spotify_song['tracks']['items'][0]['id']
            spotify_song_name = spotify_song['tracks']['items'][0]['name']
            spotify_song_artist = spotify_song['tracks']['items'][0]['artists'][0]['name']
            song_to_add.append(spotify_song_id)
            
            try:
                sp.user_playlist_add_tracks(user=current_user, 
                                            playlist_id = create_test_playlist_id, 
                                            tracks = song_to_add)
            except:
                print(f"\033[1;31;40mERROR\033[1;37;40m: There was an issue adding \033[1;35;40m{spotify_song_name}\033[1;37;40mby \033[1;36;40m{spotify_song_artist}\033[1;37;40m. Please try again.")
            else:
                print(f"Added: \033[1;35;40m{spotify_song_name}\033[1;37;40m by \033[1;36;40m{spotify_song_artist}\033[1;37;40m")
    
    # --- Print out a friendly message with the URL for the playlist:
    print(f"\nYour playlist, \033[1;32;40m{playlist_name}, \033[1;37;40mis available to listen to at:\n\033[1;34;40m{create_test_playlist_url}\033[1;37;40m.")