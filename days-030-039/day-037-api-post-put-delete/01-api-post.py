# Get = requests.get() = Get data from an API.
# Post = requests.post() = Send a new piece of data via an API.
# Put = requests.put() = Update an existing bit of data via an API.
# Delete = requests.delete() = Delete some data via an API.

from datetime import datetime
import requests

# --- Define the required constants / variables:
USERNAME = "Change_Me"
API_TOKEN = "Change_Me"
API_ENDPOINT = "https://pixe.la/v1/users"

# --- use strftime to format the date how you would like it to be (easily):
today = datetime.now()
todays_date = today.strftime("%Y%m%d")

# --- Create an account:
new_user_perams = {
    "token": API_TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}


# --- Create an account by calling the api:
new_user_requests = requests.post(url=API_ENDPOINT, json=new_user_perams)
print(new_user_requests.text)


# --- Use API headers for authentication as the API_TOKEN / token will not show up in logs.
token_headers = {
    "X-USER-TOKEN": API_TOKEN
}

# --- Create a graph definition:
new_graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

new_graph_request = requests.post(url=f"{API_ENDPOINT}/{USERNAME}/graphs", headers=token_headers, json=new_graph_params)
print(new_graph_request.text)


# --- Create a new graph entry:
new_graph_entry_params = {
    "date": todays_date,
    "quantity": "8"
}

new_graph_entry_request = requests.post(url=f"{API_ENDPOINT}/{USERNAME}/graphs/{new_graph_params['id']}", headers=token_headers, json=new_graph_entry_params)
print(new_graph_entry_request.text)


# --- Update a pixel record:
update_graph_entry_params = {
    "quantity": "10"
}

# --- Use the put method to update an existing record:
update_graph_entry_request = requests.put(url=f"{API_ENDPOINT}/{USERNAME}/graphs/{new_graph_params['id']}/{todays_date}", headers=token_headers, json=update_graph_entry_params)
print(update_graph_entry_request.text)


# --- Delete a pixel record:
update_graph_entry_params = {
    "quantity": "10"
}

# --- Use the delete method to delete an existing record:
delete_graph_entry_request = requests.delete(url=f"{API_ENDPOINT}/{USERNAME}/graphs/{new_graph_params['id']}/{todays_date}", headers=token_headers)
print(delete_graph_entry_request.text)


# --- Delete the user account:
# delete_user_account_request = requests.delete(url=f"{API_ENDPOINT}/{USERNAME}", headers=token_headers)
# print(delete_user_account_request.text)