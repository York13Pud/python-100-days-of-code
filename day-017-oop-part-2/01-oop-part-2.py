# To create a class, use class followed by the name:
# Class names should have the first letter of each word capitalised (this is Pascal case). E.g MyClass.

# Case reminder:
# Pascal Case: MyClass
# Camel Case: myClass
# Snake Case: my_class

# class User:
    # If you want to create an empty class or function, use the pass keyword to allow Python to know that there is nothing to do.
    #pass

class User():
    # __init__ is used to initialise the attributes that would be used when an object calls the class and then passes the
    # attribute arguments over to the class. __init__ is a special, built-in function in Python.
    # self is used to pass the name of the object that is being created / initialised.
    # To pass an attribute its value to the init method, it works like a normal function so you add parameters to the
    # method so that they can be passed from the object.
    #
    # Note: self needs to be the first parameter in the method so that the object using it can be referenced / passed.
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        # You can also set a default value that doesn't require a parameter / argument to be set / passed through.
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create a new user and pass the required arguments to the class
user_1 = User("001","Me")
user_2 = User("002","You")

# Have user_1 follow user_2:
user_1.follow(user_2)

# Print out the values of the user_1 and user_2 objects:
print(user_1.user_id, user_1.username, user_1.followers, user_1.following)
print(user_2.user_id, user_2.username, user_2.followers, user_2.following)

# Output would be this:
# 001 Me 0 1
# 002 You 1 0
 