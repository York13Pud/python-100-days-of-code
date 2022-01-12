import turtle
from turtle import Turtle, Screen

# --- Use the Turtle class as a variable.
leo_the_turtle = Turtle()

# --- Render the screen and set the background to black:
screen = Screen()
screen.bgcolor("black")

# --- Change the arrow to a turtle:
leo_the_turtle.shape("turtle")

# --- Change the turtle icon colour to purple:
leo_the_turtle.color("DarkOrchid")
leo_the_turtle.forward(100)
leo_the_turtle.left(90)
leo_the_turtle.color("green1")
leo_the_turtle.forward(100)
leo_the_turtle.left(90)
leo_the_turtle.color("blue1")
leo_the_turtle.forward(100)
leo_the_turtle.left(90)
leo_the_turtle.color("red1")
leo_the_turtle.forward(100)
leo_the_turtle.color("DarkOrchid")

# --- Wait for the user to click on it to exit:
screen.exitonclick()