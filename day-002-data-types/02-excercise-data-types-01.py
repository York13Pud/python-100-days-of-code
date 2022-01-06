# Exercise: Take the value from two_digit_number and add the two digits together.

# Request the user input a two digit number
two_digit_number = input("Type a two digit number: ")

# What is the data type?
print(type(two_digit_number))

# Get the first and second number and assign each to a variable.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two numbers together as a variable.
result_number = first_digit + second_digit

# Print the value of result_number. This will be an integer.
print(result_number)

# And just for a laugh, let's convert the result back to a string so we can output it as part of a block of text.
print("The answer is: " + str(result_number))

# Check the data type for result number. It will remain as an integer.
print(type(result_number))
