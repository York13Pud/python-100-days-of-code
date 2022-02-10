# This will import the turtle module which has a pre-defined class called Turtle in it.
from turtle import Turtle, Screen
import prettytable

# timmy is the object.
# Turtle() is a class from the turtle module to use.
timmy = Turtle()

print(timmy)
# The output would be similar to <turtle.Turtle object at 0x101a7faf0>. This just shows that an object is there.

# To access / set an attribute for an object from the class, you use Class_name.attribute_name. For example:
my_screen = Screen()
print(my_screen.canvheight)

# Accessing a method (function) in a class is done the same way but allows you to pass optional arguments through. For example:
timmy.shape("turtle")
timmy.color("DarkOrchid2")
timmy.forward(100)

# This will keep the turtle screen visible until it is clicked on:
my_screen.exitonclick()