from time import sleep

# A decorator function wraps another function within a function.
# It allows for the main function to control the wrapper function
# and provide additional functionality.
#
# The wrapper_function below is local rather than global so it's
# results / execution is only addressable from the parent function:

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function

# A better example:

def sleep_for_two_secs(function_called_from):
    # Initially, this is loaded but not executed, like a typical function:
    def sleep_function():
        # Print out the function name that called this function:
        print(f"Called from: {function_called_from.__name__}")
        # Print a warning:
        print("Pausing for two seconds...")
        # Sleep for two seconds:
        sleep(2)
        # Call back the function name that was passed to the parent function:
        function_called_from()

    # Call the sleep_function as the return:
    return sleep_function

# The @sleep_for_two_secs line will call the sleep_for_two_secs function
# before running the hello function when the hello function is called.
@sleep_for_two_secs
def hello():
    print("Hello World!\n")

# @sleep_for_two_secs can be used by multiple functions:
@sleep_for_two_secs
def goodbye():
    print("Godbye!\n")

# The below function will act as a normal function when called:
def greeting():
    print("How are you?\n")

# Start the script if __name__ matches __main__:
if __name__ == "__main__":
    # Call the hello and goodbye functions:    
    hello()
    goodbye()

    # Call the message function:
    greeting()