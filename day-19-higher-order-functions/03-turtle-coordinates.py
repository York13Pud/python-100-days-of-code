from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
screen.title("Turtle Racing")

players = []
player_count = 6

def create_players():
    colours = ["red", "green", "blue", "purple", "orange", "yellow"]
    colour_number = 0
    y_spacing = 360 / player_count
    y_location = -150
    print(f"\ny_spacing: {y_spacing}\n")
    for _ in range(0, 6):
        player = (colours[colour_number])
        player = Turtle(shape="turtle")
        player.color(colours[colour_number])
        player.penup()
        player.goto(-230,y_location)
        players.append(player)
        
        print(f"{colours[colour_number]} y_location: {y_location}")
        
        colour_number +=1
        y_location += y_spacing
    start_game()
    
def start_game():
    is_race_on = False
    
    user_bet = screen.textinput("Make your bet", "Which turtle colour will win?:")
    print(f"\nYour bet is: {user_bet}\n")

    if user_bet:
        is_race_on = True

    while is_race_on is True:
        for turtle in players:
            if turtle.xcor() > 210:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")

            #Make each turtle move a random amount.
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)      

create_players()

screen.exitonclick()