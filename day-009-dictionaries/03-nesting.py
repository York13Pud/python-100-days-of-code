# You can nest a list / dictionary inside a dictionary.
# List inside a dictionary:
# cities = {
#     "France": ["Paris", "Lille", "Nice"],
#     "Germany": ["Berlin", "Hamburg"]
# }

# # A dictionary inside a dictionary:
# cities = {
#     "France": {"cities_visited": ["Paris", "Lille", "Nice"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stutguard"], "total_visits": 5}
# }
# print(cities)
# print(travel_log)

# You can also nest a list inside of a list:
#nested_list = ["A", "B", ["C", "D", "E"], "F"]

# You can nest a dictionary inside of a list.
# Define a new list with multiple dictionaries, with each dictionary also having a nested list:
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Nice"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stutguard"], 
        "total_visits": 5
    }
]

# Search for an item in the travel_log list of dictionaries and print out the results:
search_result = next(item for item in travel_log if item["country"] == "France")

print(f"\nYou have been to {search_result['country']}. You visited {search_result['total_visits']} times.")

print(f"\nWhilst in {search_result['country']} you visited \
{search_result['cities_visited'][0]}, \
{search_result['cities_visited'][1]} and \
{search_result['cities_visited'][2]}.")