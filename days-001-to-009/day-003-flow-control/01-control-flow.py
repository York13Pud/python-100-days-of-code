# Starting with if statements:

# if condition:
#   do this
# else:
#   do this instead

# # Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("You can't ride the rollercoaster!")

# # Comparison operators:
# #
# # > Greater than
# # >= Greater than or equal to
# # < Less than
# # <= Less than or equal to
# # == Equal to
# # != Not equal to
# # % Modulo (use to determine how many digits are left over when deviding a number by say two to determine if it is odd (remainder) or even (no remainder))

# # Nested if statements
# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))
# age = int(input("What is your age? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 15:
#         print("Please pay $7")
#     elif age <= 17:
#         print("Please pay $9")
#     else:
#         print("Please pay $11")
# else:
#     print("You can't ride the rollercoaster!")

# elif is used where once it hits a match, it will stop. If multiple steps are needed, use multiple if statements instead.

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
ticket_price = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Child tickets are $5.")
        ticket_price = 5
    elif age <= 15:
        print("Youth tickets are $7")
        ticket_price = 7
    elif age >= 45 and age <= 55:
        print("Ticket price is $0")
        ticket_price = 0
    else:
        print("Adult tickets are $12")
        ticket_price = 12

    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        ticket_price += 3

    print(f"The total bill is: ${ticket_price}")

else:
    print("You can't ride the rollercoaster!")
