def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()


# Create a while loop to get over the hurdles by using the jump function.
# If the flag is at your position, stop:
while not at_goal():
    if wall_in_front() == True:
        jump()
    else:
        move()
