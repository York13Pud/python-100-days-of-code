# Use try to open a file and print out a key from a dictionary:
try:
    file = open("myfile.txt")
    dict_example = {"key":"value"}
    print(dict_example["key"])

# You need to create an except for each possible error type that could occur in your try.
# Note: As per the norm, when an error is encountered, the code will error and stop running.
# In this case, file not found, we can create the file instead:
except FileNotFoundError:
    file = open("myfile.txt", "w")
    file.write("A text file")
# For the key error, we will print a statement that it cannot be found.
# error_message will be the key name that we tried to pass:
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

# If there are no exceptions, perform the steps in the else section:    
else:
    content = file.read()
    print(content)
    
# The finally section is used to run some code no matter what the outcome (error or no error):
finally:
    file.close()
    print("file was closed!")
    # You can also force an error to appear if you so wish:
    raise TypeError("This is a false error")