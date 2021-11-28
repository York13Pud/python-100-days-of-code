# # Create a function to print out three lines of a greeting.
# def universal_greeting():
#     print("Bah weep-Graaaaagnah")
#     print("weep")
#     print("nini bong")


# universal_greeting()

# # ----------------------------------------------------------------------------------

# # Create a function to print out a greeting but inject a variables value into it.
# # When dealing with variables defined in a function, the variable is commonly called a parameter (name in the below).


# def greeting(name):
#     print(f"Hello {name}")


# # In the (), put the text that you wish to pass to the function variable called name.
# # The value of the parameter called name will be the argument of "Neil"
# greeting("Neil")

# # ----------------------------------------------------------------------------------

# # Create a function to print out a greeting but inject an argument into the perameter from a users input.


# def greeting_with_input(name):
#     print(f"Hello {name}")


# # Insert an input to ask for your name that will then be passed to the parameter called name.
# greeting_with_input(input("What is your name?: "))

# # Create a function with more than one input.


def greet_with_location(name, location):
    print(f"Hello, {name}")
    print(f"You are from {location}")


# When you have multiple parameters, the arguments you pass are positional, meaning that where you put the argument will be relative to the parameter.
# Positional based example:
greet_with_location(input("What is your name?: "),
                    input("Where are you from?: "))

# You can get arount the positional argument by stating the parameter name to use before the argument. This is keyword-based.
# Keyword based example:
greet_with_location(name=input("What is your name?: "),
                    location=input("Where are you from?: "))
