travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# Create a function to add Russia to the travel_log as a new nested dictionary in the list:

# Method 1: Append a new dictionary to the list:
# def add_new_country(location,count,visited):
#     travel_log.append({
#         "country": location,
#         "visits": count,
#         "cities": visited,
#     })

#     print(f"You've visited {location} {count} times.")
#     print(f"You've been to {visited[0]} and {visited[1]}.\n")

# Method 2: Create a new dictionary and append it to the list:
def add_new_country(location,count,visited):
    new_country = {}
    new_country["country"] = location
    new_country["visits"] = count
    new_country["cities"] = visited
    travel_log.append(new_country)

    # Search through the list of nested dictionaries for the added location and print out the results.
    # Note: When using dictionary searches, don't forget the "" and '' rule (can't use the same thing in the f string).
    search_results = next(item for item in travel_log if item['country'] == location)
    print(f"You've visited {search_results['country']} {search_results['visits']} times.")
    print(f"You've been to {search_results['cities'][0]} and {search_results['cities'][1]}")
    

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

travel_log = []