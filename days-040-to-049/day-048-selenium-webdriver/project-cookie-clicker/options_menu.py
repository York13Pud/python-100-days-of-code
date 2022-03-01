# --- Import required modules:
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from game_play import click_cookie

# --- Define a function that sets the cookies collected number to full, rather than short:
def set_short_number_to_off(driver: str):
    """This function will check to see if the Short numbers option is set to OFF.
    If it isn't, it will set it from ON to OFF."""
    
    print("\n*** \033[1;36;40mSetting Short Numbers to OFF\033[1;37;40m ***\n")
    # --- Perform the interactions with the site:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton")
    options_button.click()
    short_numbers_button = driver.find_element(By.CSS_SELECTOR, "#formatButton")
    if short_numbers_button.text == "Short numbers ON":
        short_numbers_button.click()
    options_button.click()

# --- Define a function to restore the games saved data:
def restore_saved_state(driver: str):
    """This function will import the saved game state from a file into the game so 
    it can carry on from the last save."""
    
    # --- Open a file with the games saved data:
    with open(f"./cookie-clicker-save.txt") as file_to_use:
        game_saved_data = file_to_use.read()
    
    print("*** \033[1;36;40mRestoring Save State\033[1;37;40m ***\n")
    # --- Perform the interactions with the site:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton")
    options_button.click()
    import_save_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[2]")
    import_save_button.click()
    save_data_text_area = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[11]/div/div[1]/div[2]/textarea[1]")
    save_data_text_area.click()
    save_data_text_area.send_keys(game_saved_data)
    save_data_load = driver.find_element(By.XPATH, "//*[@id='promptOption0']")
    save_data_load.click()
    options_button.click()

def mute_audio(driver: str):
    """this function will mute the audio in the game. When clicking the cookie, there is a 
    lag after it stops and it's very annoying so it's best to mute the audio."""
    
    print("*** \033[1;36;40mMuting the Damn Audio\033[1;37;40m ***\n")
    # --- Perform the interactions with the site:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton")
    options_button.click()
    audio_slider = driver.find_element(By.CSS_SELECTOR, "#volumeSlider")
    move = ActionChains(driver)
    move.click_and_hold(audio_slider).move_by_offset(-100,0).release().perform()
    options_button.click()