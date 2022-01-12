from turtle import Turtle, Screen, colormode
import random

leo = Turtle()
leo.pensize(15)
leo.speed("fastest")
leo.shape("turtle")

screen = Screen()
screen.bgcolor("black")

def line_color():
    colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return leo.color(red, green, blue)

directions = [45, 90, 180, 270]

for _ in range(500):
    line_color()
    leo.setheading(random.choice(directions))
    leo.forward(20)
 
screen.exitonclick()