# --- Import required modules:
from selenium.webdriver.common.by import By
from time import sleep
from itertools import cycle

# --- Define a function that gets the number of cookies collected:
def get_cookies_collected(driver: str):
    """This function will get the current number of cookies collected as a point in time 
    for you to spend on upgrades and products."""
    sleep(5)
    cookie_count_text = driver.find_element(By.CSS_SELECTOR, "#cookies").text
    
    cookie_count_text = driver.find_element(By.CSS_SELECTOR, "#cookies").text
    cookie_count_text_remove_after = "\n"
    cookie_count_number_text = cookie_count_text[:cookie_count_text.index(cookie_count_text_remove_after)]
    cookie_count_number = int(cookie_count_number_text.replace(",", ""))
    
    buy_available_upgrades(driver = driver, cookie_count = cookie_count_number)


def buy_available_upgrades(driver: str, cookie_count: int):
    upgrades_price = driver.find_elements(By.XPATH, '//*[@class="product unlocked enabled"]/div[3]/span[2]')
    upgrades_description = driver.find_elements(By.XPATH, '//*[@class="product unlocked enabled"]/div[3]/div[2]')
    upgrades_id = driver.find_elements(By.XPATH, '//*[@class="product unlocked enabled"]')

    upgrades_price_list = []
    for upgrade_price in upgrades_price:
        price_number = int(upgrade_price.text.replace(",", ""))
        upgrades_price_list.append(price_number)

    upgrades_description_list = []
    for upgrade_description in upgrades_description:
        upgrades_description_list.append(upgrade_description.text)

    upgrades_id_list = []
    for upgrade_id in upgrades_id:
        upgrades_id_list.append(upgrade_id.get_attribute("id"))

    # --- Next, add each of the above to a list of dictionaries.
    available_upgrades = []

    for available_upgrade_number in range(0, len(upgrades_price_list)):
        available_upgrades.append({"Product_ID": upgrades_id_list[available_upgrade_number],
                                "Product_Description": upgrades_description_list[available_upgrade_number],
                                "Product_Price":upgrades_price_list[available_upgrade_number]
                                })
    
    # --- Reverse the list so that the most expensive upgrade is first:
    available_upgrades.reverse()
    print("*** \033[1;32;40mChecking for purchasable upgrades\033[1;37;40m ***\n")
    for available_upgrade in cycle(range(0, len(available_upgrades))):
            if available_upgrades[available_upgrade]["Product_Price"] <= cookie_count:
                try:
                    buy_upgrade = driver.find_element(By.CSS_SELECTOR, f'#{available_upgrades[available_upgrade]["Product_ID"]}')
                except:
                    print("\033[1;31;40mNo upgrades available to buy!\033[1;37;40m\n")
                else:
                    buy_upgrade.click()
                    cookie_count -= available_upgrades[available_upgrade]["Product_Price"]
                    print(f"\033[1;32;40m[Bought:]\033[1;37;40m {available_upgrades[available_upgrade]['Product_Description']}")
                    sleep(2)
            else:
                export_save_state(driver = driver)

                              
def buy_last_option(driver: str):
    available_options = driver.find_elements(By.XPATH, '//*[@class="crate upgrade enabled"]')

    available_options_list = []
    for option_id in available_options:
        available_options_list.append(option_id.get_attribute("id"))
    
    available_options_list.reverse()
    print("*** \033[1;32;40mChecking for purchasable options\033[1;37;40m ***\n")
    try:
        buy_last_option = driver.find_element(By.CSS_SELECTOR, f'#{available_options_list[0]}')
    except IndexError:
        print("\033[1;31;40mNo options available to buy!\033[1;37;40\n")
        get_cookies_collected(driver = driver)
    else:    
        buy_last_option.click()

        print(f"\033[1;32;40m[Bought:]\033[1;37;40m {available_options_list[0]}\n")
        
        cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
        cookie.click()
        
        get_cookies_collected(driver = driver)


def export_save_state(driver: str):
    """This function will export the saved game state to a file from the game so 
    it can be restored at a later date."""
    
    # --- Perform the interactions with the site:
    options_button = driver.find_element(By.CSS_SELECTOR, "#prefsButton")
    options_button.click()
    
    export_save_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[1]")
    export_save_button.click()
    
    export_text_area = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[11]/div/div[1]/div[2]/textarea")
    copy_save_data = export_text_area.text
    
    close_export_prompt = driver.find_element(By.XPATH, "//*[@id='promptOption0']")
    close_export_prompt.click()
    
    options_button.click()
    print("*** \033[1;33;40mSaving Game State\033[1;37;40m ***\n")
    # --- Save the game state to a text file:    
    with open(f"./cookie-clicker-save.txt", mode="w") as file_to_use:
        file_to_use.write(copy_save_data)
    
    # --- Start clicking the cookie again:
    click_cookie(driver = driver)
    
    
# --- Define a function that will click the cookie:
def click_cookie(driver: str):
    counter = float(100)
    print("*** \033[1;35;40mClicking for More Cookies!\033[1;37;40m ***\n")
    # --- Define a variable that points to the big cookie to click on:
    cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
    while counter > 0:
        cookie.click()
        counter -= 1
    else:
        buy_last_option(driver = driver)