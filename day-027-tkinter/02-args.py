# A function can require arguments to be passed and if none are received it will error.
# You can, instead, set default values for a parameter in a function so that if an argument isn't passed
# it will work correctly. for example:

def my_function(a, b = 1, c = 2):
    print(a)
    print(b)
    print(c)

# Calling the function without passing a value for a will result in a TypeError (missing arg). This is due to a 
# not having a default value assigned to it when the function is defined.
# my_function()

# To remedy this, you have to pass an argument for a:
my_function(a = 1)

# You can override the defaults by simply passing a new argument for that parameter:
my_function(1, 10, 20)
# Or
# my_function(a = 1, b = 10, c = 20)

# *args
#
# If you need to pass an unlimited amount of arguments to a function, you can use *args to do this.
# It allows you to loop through the arguments sent to the function. These are effectively stored in a tuple.
# These are also called unlimited positional arguments.
# For example:

def example(*args):
    for number in args:
        print(number)

example(1, 2, 3, 4, 5, 6)

# The key to this is the * before args. The word args is used as reference for the function to use. You can use
# any word you like but args is a standard practice.

# Exercise 1: Add all the values together that passed to the add function and print the final number.
def add(*args):
    return(sum(args))
        
print(add(1, 2, 3, 4, 5, 6, 7))