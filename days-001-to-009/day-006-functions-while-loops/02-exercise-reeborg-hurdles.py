# Used on the site https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Define a function called jump to get over one hurdle:
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

# Create a for loop to get over the hurdles by using the jump function:
for hurdle in range(hurdle_count):
    jump()
