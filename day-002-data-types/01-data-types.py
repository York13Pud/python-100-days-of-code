# Display the first charecter in a string. This is called subscripting.
print("hello"[0])

# Display the last charecter in a string.
print("hello"[4] + "hello"[0])

# Display a charecter from multiple strings on the same line.
print("hello"[4] + "hello"[0])

# You can also use maths to print only a single charecter. For example, print o in the below but you must start at 0.
# Method 1, addition.
print("hello"[0+4])

# Method 2, subtraction
print("hello"[0-1])

# Integers are defined by writing the whole number(s) out without any "", which would make them a string.
print(10+10)

# Tip: with long numbers, you can use an _ to separate it out, similar to how you use a , normally.
# For example: 100,000 would be 100_000
print(100_000+100_000)

# Floats work the same way as integers in terms of defining them.
print(10.5+10.5)

# Booleans are either True or False (make sure to capitalise the first letter)

# To check what the data type is for a variable (for example), use the type function.
# The result should be a class of int, meaning an integer.
name = len("John")
print(type(name))

# The below will produce an error as concatinating does not support non-string data.
print("Your namne is " + name + " charecters long!")

# To get around this, you can convert the data type for name from an integer to a string using the str function into a new variable.
# There are also int(), float() and bool() functions available to convert to those formats as well.
name_string = str(name)
print("Your namne is " + name_string + " charecters long!")

# As a good practice, set the data type for each variable to enforce its data type and make it easier to understand.
