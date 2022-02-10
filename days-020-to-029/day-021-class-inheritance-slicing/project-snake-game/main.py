# --- Import the required modules:
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# --- Setup the basic screen / window:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

# --- Create a new object from the Snake class:
snake = Snake()
food = Food()
score = Score()
score.score_heading()

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
    
    # Detect when the snake hits the food and then generate a new food object:
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.refresh()
        
    # Detect collision with the wall:
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_on = False
        score.game_over()
    
    # Detect tail collision:
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            score.game_over()
            
# --- Exit the game when you click in the window.
screen.exitonclick()