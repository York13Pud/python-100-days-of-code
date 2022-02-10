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

# Print out a bit of ASCII art:
print(logo)

# Ask for the users first number:
num1 = int(input("What is the first number?: "))

# Print out the operations in the dictionary (+ - / *)
def print_operations():
    for operation in operations:
        print(f'{operation}')

# Print the operations that a user can choose from:
print_operations()

# Ask the user what math function they wish to use:
symbol_to_use = input("Please select a symbol from the above list of choices: ")

# Ask for the users second number:
num2 = int(input("What is the second number?: "))

# Perform the calculation and print out the answer:
calculation_function = operations[symbol_to_use]

first_answer = calculation_function(num1,num2)

print(f"{num1} {symbol_to_use} {num2} = {first_answer}")

# Print the operations that a user can choose from:
print_operations()

# Ask the user what math function they wish to use:
symbol_to_use = input("Please select a symbol from the above list of choices: ")

# Ask for the users third number:
num3 = int(input("What is the third number?: "))

# Perform the calculation and print out the answer:
calculation_function = operations[symbol_to_use]

second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {symbol_to_use} {num3} = {second_answer}")