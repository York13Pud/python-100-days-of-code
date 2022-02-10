# Request a number from the user:
number = int(input("Which number do you want to check? "))

# Determine it the number is even (divisible by two) or odd (any remainder from dividing by two):
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
