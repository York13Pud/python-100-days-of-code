# --- Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- Define a variable with the path for the chromedriver:
chrome_driver_path = "/Applications/Development/chromedriver98"

# --- Initialise a new driver that uses the chromedriver.
driver = webdriver.Chrome(chrome_driver_path)

# --- Open a website:
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

# --- Get the link for the bug text using xpath:
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# --- Simulate the clicking of the link:
#article_count.click()

# --- Another way to find and interact with a link is:
# --- Note: It is still case specific!
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
all_portals.click()

# --
search_bar = driver.find_element(By.XPATH, "//*[@id='searchInput']")
search_bar.send_keys("Python")
# --- This allows you to send a number of keystrokes, mostly used for special keys:
search_bar.send_keys(Keys.ENTER)

# Or you can use submit():
# search_bar.submit()

# --- Close down Chrome completely:
#driver.quit()