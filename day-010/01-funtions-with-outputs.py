# Functions with outputs allow the function to create an output that can be
# used to relace the function call. For example:
# Define a new function to add 4 + 2 (6) and return the result
def quick_calculation():
    """ This is an example of a docstring. It is use as a helper to describe what a function does. 
    For example, when you call a function and hover over it, this text will be shown to indicate 
    what it does. Basically used for documentation.
    You can use the same format outside of a function to do multi-line comments or ASCII art.
    Note: it must be on the first line of the function you define."""
    calculation = 4 + 2
    # Note: the return function is the end of the function. Anything after it will not be processed.
    return calculation
    # The below print statement will not run as it is after the return function.
    print("Hello!!")

# Call the function as a variable. The value of this will be 6.
# Hover over quick_calculation() below to see the docstring at the bottom of the pop-up.
result = quick_calculation()
# Print out the value of result, which will be 6.
print(result)

# Nesting functions inside each other will allow for passing on the values from the original to the next in the chain:
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
    
result = outer_function(5, 10)
# The result will be 15 as a - passed to c and b is passed to d.
print(result)