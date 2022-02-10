# --- Import the turtle module
from turtle import Turtle

# --- Create a contant for the position of the initial three squares
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# --- Create another constant for the move distance
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# --- Define the Snake class:
class Snake():
    def __init__(self):
        self.segments = []
        # --- call the create_snake method to create the initial three squares:
        self.create_snake()
        self.snake_head = self.segments[0]
        
    # --- Define the create_snake method to create the initial three squares:   
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        if position == (0, 0):
            snake.color("black")
        else:
            snake.color("black")
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        # self.snake_head.left(90)
        if self.snake_head.heading() !=UP:
             self.snake_head.setheading(DOWN)
        
    def left(self):
        if self.snake_head.heading() !=RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() !=LEFT:
            self.snake_head.setheading(RIGHT)