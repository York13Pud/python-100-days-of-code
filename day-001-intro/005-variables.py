# When it comes to naming variables, use names that make sense.
# You can use the _ to separate words in a variable. E.G. username would be user_name.
# You cannot start the name of a variable with a number.
# You can use numbers in the name, such as test_1.
# Don't use function names as a name for a variable.

# Define two variables called a and b and assign them a value of 1 and 2 respectively.
a = 1
b = 2

# Now add the values of a and b together:
a+b

# Assign the input that asks for your name to a variable called name.
name = input("What is your name? ")

# Print the value of the variable called name.
print("Your name is", name)

# Print out the number of charecters in your name.
print("The length of your name is:", len(name))

# Another method would be to have the length also be defined as a variable and use the value of name to determine its length.
name = input("What is your name? ")
length = len(name)
print("Your name is", name)
print("The length of your name is:", length)


# You can overwrite a variable by defining it again:
# Define a variable called myname with the value of John
myname = "John"
print(myname)

# Change the value of myname to Jane.
myname = "Jane"
print(myname)
