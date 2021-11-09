# Display the length of the charecters you enter for your name.
# For example, enterint the name of john would result in 4 being the output.

# My solution 👇

# Use len to count the input you provide by wrapping the input function inside the len function. Both are wrapped in the print
# function to output the number of charecters entered.

print(len(input("What is your name?: ")))

# Note: always remember to use the print function in the above scenario. If you don't and you run it normally, it will not show
# the output. However though, if you are running python3 already and just run:
# len(input("What is your name?: "))
# it will show you the value but it wont if you run python3 <path-to-file>.
