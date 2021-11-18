# Set the variables for the starting number and the last number (100 being the final):
starting_number = 1
last_number = 101

# ------------ Method 1:

# Set a variable for the total:
total_number = 0

# Perform the addition of the numbers in the range:
for single_number in range(starting_number, last_number):
    if single_number % 2 == 0:
        total_number += single_number
        # print(single_number)

# Display the total:
print(f"The total is: {total_number}")

# ------------ Method 2:

# Set a variable for the total:
total_number = 0

# Perform the addition of the numbers in the range:
for single_number in range(2, 101, 2):
    total_number += single_number

# Display the total:
print(f"The total is: {total_number}")

# Method 1 works better than method 2 at it starts at 1, rather than 2 which the exercise outlined as a requirement
# but method 2 does give the same outcome, only it starts at 2.
