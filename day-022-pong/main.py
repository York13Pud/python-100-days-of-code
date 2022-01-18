# --- Import the required modules:
from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

# --- A function to draw a line down the middle of the screen:
def middle_line():
    centre_line = Turtle(shape="square")
    centre_line.width(5)
    centre_line.color("white")
    centre_line.hideturtle()
    centre_line.penup()
    centre_line.goto(0.0,-280.0)
    centre_line.setheading(90)
    for _ in range(29):
        centre_line.pendown()
        centre_line.forward(10)
        centre_line.penup()
        centre_line.forward(10)

# --- Setup the basic screen / window:
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# --- Draw the line down the middle of the screen:
middle_line()

l_player = Player(-360, "blue")
r_player = Player(350, "yellow")

scores = Scoreboard()

ball = Ball()

   
screen.listen()
screen.onkey(l_player.up, "q")
screen.onkey(l_player.down,"a")
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down,"Down")


# --- Keep playing until game over:
game_on = True

while game_on is True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detect when the ball hits the top and bottom of the screen:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect when the ball hits player 2's paddle
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        scores.l_point()
        ball.reset_position()
        
        
    if ball.xcor() < -390:
        scores.r_point()
        ball.reset_position()
        
        
# --- Exit the game when you click in the window.
screen.exitonclick()