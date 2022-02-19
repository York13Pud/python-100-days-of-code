# --- Import the required libraries / modules:
from art import splash_screen
from clear import clear_screen
from time import sleep
from date_to_use import get_date_to_use
from scrape_site import scrape_site
from create_spotify_playlist import create_spotify_playlist

# --- show the splash screen:
clear_screen()
print(splash_screen)
sleep(3)
clear_screen()

# --- Set a variable to use for looping the question of adding a playlist:
create_playlist = True

# --- Crete a playlist until create_playlist is no longer true:
while create_playlist is True:
    # --- Call the get_date_to_use module to get a date to use from the user:
    date_to_use = str(get_date_to_use())

    # --- Call the scrape_site module to get a list of songs to add to a new playlist:
    songs = scrape_site(date_to_use = date_to_use)

    # --- Call the create_spotify_playlist module / function to create a playlist and
    # --- add the songs in the songs list:
    create_spotify_playlist(songs = songs, date_to_use = date_to_use)
    
    create_another_playlist = input("\nWould you like to create another playlist? Y / N: ").capitalize()
    clear_screen()
    
    if create_another_playlist[0] == "N":
        create_playlist = False
        print("Thank you! Goodbye!")