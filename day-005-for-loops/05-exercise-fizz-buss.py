# Set two variables, one for the starting number and another for the last number.
starting_number = 1
last_number = 101

# Process the numbers in the range and match the number to the required output.
# The number will be caught by the first matching rule in the if statement and the matching output displayed.
# This is why the 3 and 5 if statement is first as 15 for example would be caught by 3 and 5 but if 3 and 5 were below 3
# then it would match to 3.

for number in range(starting_number, last_number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
