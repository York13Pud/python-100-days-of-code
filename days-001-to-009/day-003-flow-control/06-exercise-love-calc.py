print("Welcome to the Love Calculator!")

# Define the required variables:
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Convert name1 and name2 to lowercase
name1 = (name1.lower())
name2 = (name2.lower())

# Combine the two names
both_names = name1 + name2

# Add up all the instances of the letters "true love" that appear in both_name.
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

true = t+r+u+e

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

love = l+o+v+e

# Put the two numbers together. This is done by converting each name score to a string, concatnate the two together
# and then convert that to an integer.
total_score = int(str(true) + str(love))

# Display the result with an appropriate message based on the score.
if (total_score <= 10) or (total_score >= 90):
    print(f"Your score is {total_score}, you go together like glue")
elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}")
