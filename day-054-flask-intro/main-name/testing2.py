from testing import testing

# __name__ is a special, read-only attribute that is built into Python.
# __name__ references back to __main__ when the program 
# is run as a script (gets the name as part of the input) or from an
# interactive prompt where user input is passed to the __name__ class.
# 
# If the file is imported as a module and executed, __name__ will change
# when executing code in the imported module to the name of the file.
#
# The purpose for this is to check that the file is being run correctly.
# If it is a module that is imported, it should not have a name the ==
# __main__. Instead, it should have the name of the file instead of __main__.

print(__name__)
if __name__ == "__main__":
    testing()