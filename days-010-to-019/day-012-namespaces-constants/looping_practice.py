import random

# A simple print out of a list
def process_list(my_list_item):
    for item in my_list_item:
        print(item)

my_list = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]

process_list(my_list_item = my_list)

# Use if statements inside a while loop to print out the numbers between the start
# and end parameters.
def looping(start_number,end_number):
    
    looping_true = True

    while looping_true is True:
        if start_number <= end_number:
            print(start_number)
            start_number += 1
        else:
            looping_true = False

looping(start_number = 0,end_number = 21)

# Use a for loop inside a while loop to print out the numbers between the start_again
# and end_again parameters.
def looping_again(start_again,end_again):

    looping_again_true = True

    while looping_again_true is True:
        for number in range(start_again,end_again):
            print(number)
            start_again += 1
            # When the loop gets to the value of end_again, it will not print (42).
            # The following if statement will print the last value of end_again (42).
            if start_again == end_again:
                print(end_again)
        else:
            looping_again_true = False

looping_again(start_again = 22,end_again = 42)