# Import modules and set the required variables:
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Determine the number of items in the list:
total_names = len(names)

# Use the random module to set the random number range. Remove one from the total_names to match the lists last number.
random_number = random.randint(0, total_names - 1)

# Display the result.
print(f"{names[random_number]} is going to buy the meal today!")

# Below is used for diagnostics:
# print(total_names)
# print(random_number)
# print(names[random_number])

# Another (quicker method) to all of the above is to use random.choice:
payer = random.choice(names)
print(f"{payer} is going to buy the meal today!")
