# # Namespaces, aka global and local scope.
# #
# # local scope is a variable that is contained within a function.
# # Global scopes are defined outside of functions.
# #
# # For example, if you set a variable outside (global) of a function and then try to change it
# # inside the function, it will not update but treat it as a different variable.
# #
# # For example:

# # Global scope variable
# testing = 1

# def inc_testing():
#     # Local scope variable
#     testing = 100
#     print(f"The value of testing in the function is: {testing}")

# inc_testing()
# print(f"\nThe value of testing outside the function is: {testing}")

# # Another example. You are trying to call a function that is defined inside a function:

# def example_2():
#     # Local scope variable
#     test_local_scope = 1
#     print(test_local_scope)

# # This will run the function and print out 1:
# example_2()
# # This will produce a name error as the variable is only available within the function (local scope):
# #print(test_local_scope)


# # When creating a global and local scoped variable, don't use the same name.
# # Local scopes also apply to operations other than variables as well. For example, nesting functions
# # within other functions:

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 1000
#         # This will print 10:
#         print(player_health)
#     # This will call the drink_potion function within the game function:
#     drink_potion()
#     # This would not work as potion_strength is called outside of the local scope of the drink_potion function:
#     print(potion_strength)
# # This will print 10:
# print(player_health)
# game()

# There is no concept of block scopes. What this means is that if you define a variable in an if / for or while loop
# it does not count as a local scope, until it is inside a function.

# You can modify a global variable within a function scope but it is not recommended as it can cause issues / bugs.
# To do this, you have to define the variable as "global" before you actually modify it.
# For example:

testing = 1

def inc_testing():
    # We now specify the testing variable as a global scope variable:
    global testing
    testing += 100
    # This will print 101
    print(f"The value of testing in the function is: {testing}")

inc_testing()
# This will also print 101
print(f"\nThe value of testing outside the function is: {testing}")

# Avoid modifying global scopes as best possible.

# One possible method to work around modifying a global in a function is to use a return:

testing_2 = 1

def inc_testing():
    # This will print 1
    print(f"The value of testing in the function is: {testing_2}")
    return testing_2 + 100

testing_2 = inc_testing()
# This will print 101
print(f"\nThe value of testing outside the function is: {testing_2}")