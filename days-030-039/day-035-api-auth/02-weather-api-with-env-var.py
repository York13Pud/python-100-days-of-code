from itertools import islice
import os
import requests
import smtplib

# --- Define the required contants and variables
API_KEY = os.environ.get("weather_api_key")
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 0
MY_LONG = 0
will_it_rain = False

# --- Setup required email settings:
my_email = ""
to_email = ""
smtp_server = ""
sender_username = ""
sender_password = ""

# --- Define the required parameters for the API call:
API_PARAMS = {
    #"q": CITY_NAME,
    "lon": MY_LONG,
    "lat": MY_LAT,
    "appid": API_KEY,
    "country": "gb",
    "units": "metric",
    "exclude": "current,minutely,daily"
}

# --- Execute the API call:
response = requests.get(url=API_ENDPOINT, params=API_PARAMS)

# --- Display the HTTP response code:
print(f"\nHTTP Response Code: {response.status_code}\n")

# --- If an error occurs, this will print out the response and its meaning:
response.raise_for_status()

# --- This will print out the details as JSON:
data = response.json()

# --- Check the hourly data for the next 12 hours and if it will, change will_it_rain to true:
for hour in islice(data["hourly"],12):
    weather_code = hour["weather"][0]["id"]
    if int(weather_code) <= 700:
        will_it_rain = True

# --- Display a message to indicate if it will rain or not:
if will_it_rain is True:
    message_body = "Bring a brolly with you!!"
else:
    message_body = "Safe to put the washing out!!"
    
# --- Send an email to say if it will rain or not:
with smtplib.SMTP(smtp_server, port=25) as connection:
    # --- Make the connection secure:
    connection.starttls()
    # --- Login to the SMTP Server:
    connection.login(user=sender_username,password=sender_password)
    # --- Send a message.
    # --- Note: \n\n after the subject is required to separate the subject and message body:
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg=f"Subject:Weather for the next 12 hours \n\n{message_body}")