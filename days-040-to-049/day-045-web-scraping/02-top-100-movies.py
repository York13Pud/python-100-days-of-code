from bs4 import BeautifulSoup
import requests

# --- Define a variable for the site to use:
site_to_use = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# --- Open the site and assign it to a variable:
site_response = requests.get(site_to_use)
web_page_text = site_response.text

# --- Parse the page using BeautifulSoupL:
soup = BeautifulSoup(web_page_text, "html.parser")

# --- Find all h3 tags with a class of title. They will be added to a list:
movies = soup.find_all(name="h3", class_="title")

# --- Reverse the list as 100 is first before hand:
movies.reverse()

# --- Write the list to a text file:
with open("top-100-movies.txt", mode="w") as file_to_use:
    for item in movies:
        file_to_use.write(f"{item.getText()}\n")

print("\nThe Top 100 Movies to watch are:\n==============================\n")

# --- Print the contents of the file:
with open("top-100-movies.txt", mode="r") as file_to_use:        
    contents = file_to_use.read()
    print(contents)