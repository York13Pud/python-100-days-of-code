# --- Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- Define a variable with the path for the chromedriver:
chrome_driver_path = "/Applications/Development/chromedriver98"

# --- Initialise a new driver that uses the chromedriver.
driver = webdriver.Chrome(chrome_driver_path)

# --- Open a website:
driver.get("http://secure-retreat-92358.herokuapp.com/")

# --- Fill out the form on the page:
first_name = driver.find_element(By.NAME, "fName").send_keys("First")
last_name = driver.find_element(By.NAME, "lName").send_keys("Last")
# You can send multiple send keys:
email = driver.find_element(By.NAME, "email").send_keys("first.last@test.test", Keys.ENTER)

# --- Close down Chrome completely:
#driver.quit()