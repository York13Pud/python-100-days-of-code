# Use a for loop to perform an action against items in a list.

# For example, take a list called fruits and then print out each item in the list.
fruits = ["Apple", "Grape", "Pear"]

# To make it easy to read, use a singular version of the list name (fruits to fruit)
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
# The below line is outside the for loop so it will print out the entire list:
print(fruits)

# The range function is used to perform an action on a number between two ranges.
# The below example will print out the numbers 1 to 9. It will not print 10.
for number in range(1, 10):
    print(number)

# To print out 10, you set the range to 11.
for number in range(1, 11):
    print(number)

# You can specify a step number to increment by when performing an action.
# For example, setting the step to 3 will print the numbers 1, 4, 7 and 10:
for number in range(1, 11, 3):
    print(number)

# Add up all the numbers between 1 and 100.
total = 0
for number in range(1, 101):
    total += number
print(total)

# You can use variables for the range numbers:
starting_number = 1
last_number = 101

total_number = 0

for single_number in range(starting_number, last_number):
    total_number += single_number
print(total_number)
