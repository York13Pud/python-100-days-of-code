def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Create a variable for the total number of hurdles:
hurdle_count = 6

# Create a while loop to get over the hurdles by using the jump function.
# If the flag is at your position, stop:
while not at_goal():
    jump()


# Another method:
# while hurdle_count > 0:
#     if at_goal():
#         done()
#     else:
#         jump()
#         hurdle_count -= 1
