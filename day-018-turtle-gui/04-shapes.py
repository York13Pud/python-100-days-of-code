from turtle import Turtle, Screen, colormode
import random

leo = Turtle()
leo.pensize(2)

screen = Screen()
screen.bgcolor("black")

def line_color():
    colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return leo.color(red, green, blue)

sides = 3

while sides != 11:
    line_color()
    angle = 360 / sides
    for _ in range(sides):
        leo.forward(100)
        leo.right(angle)
    sides += 1

screen.exitonclick()