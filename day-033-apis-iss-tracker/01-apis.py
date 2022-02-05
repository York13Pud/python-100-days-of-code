# API endpoint is the URL of the API.
# API request is an action to perform against the API endpoint.

from curses import keyname
import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")

# If an error occurs, this will print out the response and its meaning:
response.raise_for_status()

# This will print out the details as JSON:
data = response.json()
print(data)
# Call a specific part of the JSON response:
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
# Response codes:
# 100 Hold on.
# 200 Ok here.
# 300 Go away.
# 400 You made a mistake.
# 500 We screwed up our side.