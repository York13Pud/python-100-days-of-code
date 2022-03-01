# --- Import required modules:
from selenium import webdriver
from time import sleep
from options_menu import set_short_number_to_off, restore_saved_state, mute_audio
from game_play import click_cookie


# --- Define a variable with the path for the chromedriver:
chrome_driver_path = "/Applications/Development/chromedriver98"

# --- Initialise a new driver that uses the chromedriver.
driver = webdriver.Chrome(chrome_driver_path)

# --- Open a website:
driver.get("https://orteil.dashnet.org/cookieclicker/")


# --- Pause for a few seconds to let the page fully load.
# --- Experience with the site shows that not all elements load quickly:
sleep(5)


# --- Start the program:

# --- Set the numbers that displayed from short (xx Million) to full (x,xxx,xxx,xxx):
set_short_number_to_off(driver=driver)
sleep(1)

# --- Load the last saved state from a file:
restore_saved_state(driver=driver)
sleep(1)

# --- Mute the bloody audio:
mute_audio(driver = driver)
sleep(1)

# --- Begin clicking the giant cookie:
click_cookie(driver=driver)


# --- Close down Chrome completely:
driver.quit()