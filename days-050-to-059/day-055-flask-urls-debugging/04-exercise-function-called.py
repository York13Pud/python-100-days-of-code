# Create the logging_decorator() function
def logging_decorator(function_called_from):
    def wrapper(*args):
        print(f"The function named {function_called_from.__name__}{args} called")
        result = function_called_from(args[0], args[1], args[2])
        print(f"The total added together is: {result}")
    return wrapper

# Use the decorator
@logging_decorator
def calling_logging_decorator(a, b, c):
    return a * b * c

calling_logging_decorator(1,2,3)