# Create a sample list of dictionaries:
sample_list = [
                {"test": "one", "value": "potato"}, 
                {"test": "two", "value": "apple"}
              ]

# Print out the entire list:
print(sample_list[0])

# Print the value of index 0 in the list and return the contents of "value" in the dictionary:
print(f"The value of test {sample_list[0]['test']} is {sample_list[0]['value']}\n")

# iterate over the list

for sample in sample_list:
    # now i is a dict, now we see the keys of the dictionary:
    for key, val in sample.items():
    # print every key and value of each dictionary:
        print('{}: {}'.format(key, val))

    print("=====================")
