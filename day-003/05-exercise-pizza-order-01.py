# Welcome prompt:
print("Welcome to Python Pizza Deliveries!")

# Set the required variables:
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total_price = 0

# Set the price of the pizza:
if size == "S":
    total_price += 15
elif size == "M":
    total_price += 20
elif size == "L":
    total_price += 25

# Add the price of pepperoni, if needed:
if add_pepperoni == "Y" and size == "S":
    total_price += 2
elif add_pepperoni == "Y" and (size == "M" or "L"):
    total_price += 3
else:
    print("No pepperoni for you!")

# Add the price of extra cheese, if needed:
if extra_cheese == "Y":
    total_price += 1
else:
    print("No extra cheese for you!")

# Output the final price:
print(f"The total cost of your pizza is: ${total_price}")
