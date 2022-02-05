import requests
from datetime import datetime

MY_LAT = 53.432602
MY_LONG = -1.363501

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunrise = sunrise.split("T")
sunrise = sunrise[1].split(":")

sunset = data["results"]["sunset"]
sunset = sunset.split("T")
sunset = sunset[1].split(":")

print(f"Sunrises at: {sunrise[0]}:{sunrise[1]}\nSunsets at: {sunset[0]}:{sunset[1]}")

time_now = datetime.now()
print(time_now.time())