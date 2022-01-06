 # A dictionary is like a table when compared to a list.
 # It is based on a key / value pair.
example_table = {
      "Potato": "A potato is a veg",
      "Carrot": "A carrot is a veg",
      1:"One",
}

# Print out all elements in the dictionary.
print(example_table)

# Print out the value of Potato. 
# Note: It it case sensitive.
print(example_table["Potato"])

# Data types do exist in dictionaries as well. In the example table, there are two strings and one number.
# To retrieve the number, you use the same method as above but only type the number 1 in on its own:
print(example_table[1])

# To add an element to the dictionary:
example_table["Apple"] = "An apple is a fruit"
print(example_table)
print(example_table["Apple"])

# To edit an existing element:
example_table["Apple"] = "An apple is not a veg"
print(example_table["Apple"])
print(example_table)

# To loop through a dictionary:
for key in example_table:
    print(f"{key}: {example_table[key]}")

# To remove an element from a dictionary:
del example_table["Apple"]
print(example_table)

# To create an empty dictionary:
empty_dictionary = {}

# To clear an existing dictionary:
example_table = {}

# To delete an existing dictionary:
del empty_dictionary
# This will cause a NameError as the dictionary no longer exists:
print(empty_dictionary)