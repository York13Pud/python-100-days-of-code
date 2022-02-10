# Load / import the random module.
import random
# Load / import my custom module.
# Note: Module names must use _ for spaces and cannot start with a number for the filename.
import example_custom_module

# Generate a random integer between 1 and 10 and then print it out.
random_integer = random.randint(1, 10)
print(random_integer)

# This will print out the text variable defined in the custom module and the random number generated in this script.
print(f"{example_custom_module.text} {random_integer}")

# Generate a random float between 0 and 5 and then print it out.
# Note: using random.random() will only allow a random number to be generated between 0 and 1.
random_float = random.uniform(0.0, 5.0)
print(random_float)

# round the number to two decimal places:
random_float_rounded = round(random_float, 2)
print(random_float_rounded)

# This will print out the text variable defined in the custom module and the random number generated in this script.
print(f"{example_custom_module.text} {random_float_rounded}")
