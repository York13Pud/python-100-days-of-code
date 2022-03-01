# --- Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# --- Define a variable with the path for the chromedriver:
chrome_driver_path = "/Applications/Development/chromedriver98"

# --- Initialise a new driver that uses the chromedriver.
driver = webdriver.Chrome(chrome_driver_path)

# --- Open a website:
driver.get("https://www.python.org/")

# --- Get the link for the bug text using xpath:
all_dates = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/time')
all_dates_text = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/a')

# --- Define two empty lists; one for the dates and another for the text:
event_dates_list = []
event_text_list = []

# --- Add the dates to the dates list:
for entry in all_dates:
    event_dates_list.append(entry.text) 

# --- Add the text to the text list:
for entry in all_dates_text:
    event_text_list.append(entry.text)

# --- Define a blank dictionary for the final data format:
upcoming_events = {}

# --- Create dictionary items for each event:
for index_number in range(len(event_dates_list)):
    upcoming_events[index_number] = {
        "time": event_dates_list[index_number],
        "name": event_text_list[index_number]
    }
    
# --- Print the contents of the dictionary:
print(upcoming_events)

# --- Close down Chrome completely:
driver.quit()