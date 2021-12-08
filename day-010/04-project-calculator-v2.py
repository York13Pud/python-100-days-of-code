from art import logo

# Create the functions to perform the various math functions:
# Add:
def add(n1, n2):
    return n1 + n2

# Subtract:
def subtract(n1, n2):
    return n1 - n2

# Multiply:
def multiply(n1, n2):
    return n1 * n2

# Divide:
def divide(n1, n2):
    return n1 / n2

# Create a dictionary that points to the function names based on user input later on:
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def print_operations():
    for operation in operations:
        print(f'{operation}')

# Print out a bit of ASCII art:
print(logo)

# Ask the user for their first number:

def calculator():
    num1 = float(input("What is the first number?: "))
    previous_answer = num1

    # Ah yes. Next time, don't ever use the word 'continue' for a variable name. It's a reserved name!
    # Define a variable to use to track if a new calculation should take place:
    new_calc = True

    # Use a while loop to ask for the symbol to use and the next number to work with.
    while new_calc is True:  
        # Print the list of operations the user can do:
        print_operations()

        # Ask the user what math function they wish to use:
        symbol_to_use = input("Please select a symbol from the above list of choices: ")

        # Ask for the users second number:
        next_num = float(input("What is the next number?: "))

        # Get the name of the symbol from the operations dictionary:
        calculation_function = operations[symbol_to_use]

        # Define the variable called answer that will send the previous_number and next_num to the correct function that is
        # returned from calculation_function. For example calculation_function = add so it will be add(previous_answer,next_num):
        answer = calculation_function(previous_answer,next_num)
        
        # Print out the answer:
        print(f"{answer} {symbol_to_use} {next_num} = {answer}\n")

        # Ask the user if they would like to perform another calculation, exit or start again:
        go_again = input("Would you like to perform another calculation (y), exit (n) or start again (s)?: ")
        
        # If the user does not input any variation of y or a, the program will exit:
        if go_again == "y":
            # Set  previous_answer to equal answer. This is used later if the user needs to perform another calculation:
            previous_answer = answer
        elif go_again == "s":
            # exits the while loop:
            new_calc = False
            # Recursively runs the calculator function again:
            calculator()
        else:
            # exits the while loop and prints out a final message:
            new_calc = False
            print("Thank You. Goodbye and Good Night")

# Call the calculator function:
calculator()