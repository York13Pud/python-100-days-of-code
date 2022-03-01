# Selenium is used to to simulate web page interactions
# chromedriver is used to pass instructions from selenium to chrome

# --- Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# --- Define a variable with the path for the chromedriver:
chrome_driver_path = "/Applications/Development/chromedriver98"

# --- Initialise a new driver that uses the chromedriver.
driver = webdriver.Chrome(chrome_driver_path)

# --- Open a website:
driver.get("https://www.python.org/")

# Get the placeholder name for the search bar:
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

# Get and display the size of the logo on the page.
# This will be in the form of a dictionary with the height and width values:
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

# Get the documentation link:
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

# Get the link for the bug text using xpath:
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_attribute('href'))

# --- Close the active tab that you just opened. If there is only one tab, it will quit out of Chrome:
#driver.close()

# --- Close down chrome completely:
driver.quit()