# First-class objects can be passed around as arguments for a function. For example:

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def calculate(calc_function, n1, n2):
    return calc_function(n1,n2)

# Change add to sub. These are the first-class functions
result = calculate(add,1,2)
print(result)


# Nested function example:
def outer_function():
    print("Outer")
    
    # Note: the nested function can only be called from within the parent function.
    def nested_function():
        print("nested")
    
    return nested_function

# This will only print outer as nested_function is return to the variable.
inner_function = outer_function()

# Calling the variable will print outer and nested.
inner_function()