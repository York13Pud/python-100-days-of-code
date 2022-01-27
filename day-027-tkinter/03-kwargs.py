# **kwargs allow for an unlimited number of key-word arguments to be passed to a function.
# **kwargs are stored as a dictionary for the function to use.
# The kwargs word can be anything but you must have the ** before it.
# You can also define named parameters in a function to use as well.
# Example:

# Create function with one named parameter and then any amount of kwargs:
def calculate(number, **kwargs):
    # Loop through the key/value pairs in the kwargs dictionary:
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    # Another option is to reference the key name directly:
    return (number + kwargs["b"])

# Call the function and pass an argument for number and then two unnamed parameters / arguments for kwargs:
print(calculate(10, a=1, b=2))

# **kwargs can also be used in classes. For example:

class CarOne:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_new_car = CarOne(make = "Ford", model="Fiesta")
print(my_new_car.make, my_new_car.model)

# If you don't pass one of the arguments through that is used in the init function (for example)
# it will fail with a key error. Instead, you can use the get method. What this wil do is in the event that
# you don't pass an argument, it will set the missing argument to "None". These are classed as optional arguments.
# Best to use get in classes as best possible when using **kwargs.
# For example:

class CarTwo:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_new_car = CarTwo(make = "Ford")
# This will return Ford None
print(my_new_car.make, my_new_car.model)