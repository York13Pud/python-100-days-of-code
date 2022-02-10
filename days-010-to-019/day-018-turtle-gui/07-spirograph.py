from turtle import Turtle, Screen, colormode
import random

leo = Turtle()
leo.pensize(1)
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

for _ in range(72):
    line_color()
    leo.left(5.0)
    leo.circle(200)
    
screen.exitonclick()