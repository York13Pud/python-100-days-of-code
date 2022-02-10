from turtle import Turtle

class Player(Turtle):
    def __init__(self, position, colour):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(colour)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position, 0)
    # def create_player(self, position):
    #     self.paddle.goto(position,0)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)