# --- Import the required modules:
from turtle import Screen
from snake import Snake
import time

# --- Setup the basic screen / window:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# --- Create a new object from the Snake class:
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True

while game_on is True:
    screen.update()
    time.sleep(0.1)

    snake.move()

# --- Exit the game when you click in the window.
screen.exitonclick()