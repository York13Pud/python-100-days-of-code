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

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        line_color()
        leo.circle(200)
        leo.setheading(leo.heading() + size_of_gap)
        
draw_spirograph(5)

screen.exitonclick()