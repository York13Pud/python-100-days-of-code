# List comprehension allows you to iterate over a list in a way that is quicker and easier
# than using a for loop. 
 
# new_list = [new_item for item in list]

# For example:
# Start with a simple list of numbers:
numbers = [1, 2, 3]

# Now we want to create a new list where we add 1 to each item in the list:
# First, name the list (new_list).
# Second, what action do we want to do for each item in the source list (numbers). In this case, add 1)
# Third, iterate over each item in the list:
new_list = [n + 1 for n in numbers]

# Print out the values of new_list (2, 3, 4):
print(new_list)

# You can also work with non-list sources like a variable with a string:
name = "Jason"
new_name_list = [letter for letter in name]
# The output will be a list containing the individual charecters of the string.
print(new_name_list)

# Exercise: take a range of numbers (1-4) and double eachone into a new list.

range_list = [range_number * 2 for range_number in range(1, 5)]
print(range_list)

# You can add conditions to a list comprehension
# new_list = [new_item for item in list if test_criteria]
# For example, make a new list which contains the names that have less than 5 charecters:
full_names = ["Bob", "Jason", "Sam", "Alexis"]
short_names = [name for name in full_names if len(name) < 5]
print(short_names)
#Result is: ['Bob', 'Sam']

# Exercise: use the list of names above but convert the case for the result to upper for each name:
full_names = ["Bob", "Jason", "Sam", "Alexis"]
short_names = [name.upper() for name in full_names if len(name) < 5]
print(short_names)
#Result is: ['BOB', 'SAM']

# Exercise: square each number in a list:
to_be_squared = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in to_be_squared]
print(squared_numbers)

# Exercise: Add numbers to a new list if they are even:
even_numbers = [number for number in to_be_squared if number % 2 == 0]
print(even_numbers)