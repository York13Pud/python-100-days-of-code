from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points_count = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(0, 265)
        self.score_heading()
        
    def score_heading(self):
        self.write(f"Score: {self.points_count}", align=ALIGN, font=FONT)
        
    def refresh(self):
        self.points_count += 1
        self.clear()
        self.score_heading()
        
    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"Game Over!\nYour Score was: {self.points_count}", align=ALIGN, font=FONT)