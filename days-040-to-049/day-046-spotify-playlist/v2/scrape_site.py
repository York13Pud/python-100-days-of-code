# --- Import the required libraries / modules:
from bs4 import BeautifulSoup
import requests

# --- Define the required constants:

# --- The base URL to scrape from:
BASE_URL_TO_SCRAPE = "https://www.billboard.com/charts/hot-100"

def scrape_site(date_to_use: str):   
    """This function will perform the scraping of the hot-100 for a given date and produce a list of
    songs that can be used to add to a playlist.
    
    The date_to_use parameter must be a string in the format YYYY-MM-DD."""
    
    # --- Define a variable to join the base_url to scrape and the date_to_use to give the complete URL:
    full_url_to_scrape = f"{BASE_URL_TO_SCRAPE}/{date_to_use}"
    
    # --- Define an empty list to use for the list of songs to add:
    songs = []
        
    # --- Perform the scraping and at the end, return the list of songs:
    try:
        # --- A little message to show the full URL:
        print(f"\nScraping Top 100 songs from: \033[1;34;40m{full_url_to_scrape}\n\033[1;37;40m")
    
        # --- Open the site and assign it to a variable:
        site_response = requests.get(full_url_to_scrape)
    
    # --- If any errors occur, print a message:
    except:
        print("\033[1;31;40mERROR\033[1;37;40m: Please check the date you entered is correct.")
    
    # --- If all is ok, proceed to process the scraped results:
    else:
        # --- Parse the page using BeautifulSoupL:
        soup = BeautifulSoup(site_response.text, "html.parser")

        # --- Find all h3 tags with a class of lrv-u-font-size-16. They will be added to a list:
        top_100_songs = soup.select(selector="h3" ".lrv-u-font-size-16")
        
        # --- get the song names only and strip out the \n's:
        for song in top_100_songs:
            songs.append(song.getText("h3").strip("\n"))
        
        # --- Return the list of songs to the main program's songs variable:
        return songs
    


