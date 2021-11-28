# import math module to use for rounding up.
import math

# Create a function to do the matchs of working out the number of paint cans needed for a wall.


def paint_calc(height, width, cover):
    total_cans_needed = math.ceil((height*width) / cover)
    print(f"The total cans of paint needed are: {total_cans_needed}")

# Request the size of the wall:


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# The volume of paint per can:
coverage = 5

# Call the function:
paint_calc(height=test_h, width=test_w, cover=coverage)
