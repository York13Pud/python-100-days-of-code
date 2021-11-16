# A list is a variable with a number of items in them.
# You can mix data types (added 1 to show this).

example_list = ["first_name", "lastname", "age", "town", "city", 1]

# To output an entry in the list, use the variable name and then the item index in [].
# For example (prints the first entry):
print(example_list[0])

# You can also use negative index references 9the below example would print city):
print(example_list[-2])

# To print the entire list, just use a normal print with the variable name:
print(example_list)

# To print out the fourth letter of the first list item, put another [] and enter the number of the letter you want.
print(example_list[0][3])

# To print out multiple values from the list, you need to call the variable again:
print(example_list[0] + " " + example_list[3])

# To change an item in the list, you can call the variable name, along with the index in [] and change it:
# Before:
print(example_list)

# this changes age to dob
example_list[2] = "dob"

# After
print(example_list)

# To add an object to the list (at the end), use the append function on the variable.
# For example:

example_list.append("post_code")
print(example_list)

# To add multiple objects to a list, use the extend function:
example_list.extend(["age", 2, "country"])
print(example_list)

# To remove an object from a list, use the remove function and the name / number of the object.
# For example, let's remove 1 (an integer) and city (a string) from the list.
example_list.remove(1)
example_list.remove("city")
print(example_list)

# IndexError: list index out of range.
# This can be fixed by using len(variable_name - 1). It removes one from the length of the list
# to reflect the way python handles list indexes (always starting at 0).
print(len(example_list))
list_length = len(example_list)
print(list_length-1)

# You can use nested lists in Python by creating two individual lists and then referencing them in another list.
# For example:

list_one = ["one", "two", "three"]
list_two = ["four", "five", "six"]
full_list = [list_one, list_two]
print(full_list)

# Note: To return just one item (two in this case), we need to reference the list index (there are two in the above full_list(0 and 1)) and also reference the object index within that list.
# For example (print two):
print(full_list[0][1])
# print six:
print(full_list[1][2])
