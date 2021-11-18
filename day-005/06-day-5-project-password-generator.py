# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Request the users input:
print("Welcome to the PyPassword Generator!\n")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
# for loop to select random letters:
for nr_letter in range(1, nr_letters + 1):
    password += (random.choice(letters))

# for loop to select random numbers:
for nr_number in range(1, nr_numbers + 1):
    password += (random.choice(numbers))

# for loop to select random symbols:
for nr_symbol in range(1, nr_symbols + 1):
    password += (random.choice(symbols))

# Print the password as is:
print(f"The password in order is: {password}\n")

# Randomise the password and print it:
random_password = ''.join(random.sample(password, len(password)))
print(f"The randomised password is: {random_password}\n")
