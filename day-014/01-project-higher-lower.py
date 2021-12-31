# --- Import the data for the game, the artwork and any required modules:
from art import logo, vs, lost
from game_data import data
from clear import clear_screen
import random
import time

# --- display the logo:
print(logo)
print("The first round will start in two seconds.")
time.sleep(2)
clear_screen()

# --- Determine the length of the list that contains all the choices. Reduce by one to match it to the list indexes:
items_in_data = (len(data)-1)

# --- Define a function for the bulk of the game:
def play_game():
    # --- set game_over to False:
    game_over = False
    score = 0
    # --- Until game_over is True, the game will continue to play:
    while game_over is False:
        # --- Generate two random numbers between 0 and the maximum number in the list.
        a_choice = data[random.randint(0, items_in_data)]
        b_choice = data[random.randint(0, items_in_data)]
        # --- Display the two results.
        print(f"\033[1;36;40mChoice A: {a_choice['name']}, a {a_choice['description']} from {a_choice['country']}.")
        print(vs)
        print(f"\033[1;35;40mChoice B: {b_choice['name']}, a {b_choice['description']} from {b_choice['country']}.\n")
        # --- Ask the player for their choice:
        players_choice = input("\033[1;37;40mPlease chose which is higher, \033[1;36;40mA \033[1;37;40mor \033[1;35;40mB\033[1;37;40m: ")
        if players_choice == "A" or players_choice == "a":
            # --- If A is higher than B, you will get to play again.
            if a_choice["follower_count"] > b_choice["follower_count"]:
                print("\n\033[1;32;40mYou are correct. Another round will start in two seconds.")
                score +=1
                time.sleep(2)
                clear_screen()
            # --- If B and A are the same, start another round:
            elif a_choice["follower_count"] == b_choice["follower_count"]:
                print("\n\033[1;32;40mThey are the same. Another round will start in two seconds.")
                time.sleep(2)
                clear_screen()
            # --- If A is lower than B, set game_over to true and end the game.
            else:
                print("\n\033[1;31;40mA was lower.\n")
                print(f"Your final score was: {score}")
                time.sleep(3)
                game_over = True
                clear_screen()
                print(lost)
                time.sleep(2)
        elif players_choice == "B" or players_choice == "b":
            # --- If B is higher than A, you will get to play again.
            if b_choice["follower_count"] > a_choice["follower_count"]:
                print("\n\033[1;32;40mYou are correct. Another round will start in two seconds.")
                score +=1
                time.sleep(2)
                clear_screen()
            # --- If B and A are the same, start another round:
            elif b_choice["follower_count"] == a_choice["follower_count"]:
                print("\n\033[1;32;40mThey are the same. Another round will start in two seconds.")
                time.sleep(2)
                clear_screen()
            # --- If B is lower than A, set game_over to true and end the game.
            else:
                print("\n\033[1;31;40mB was lower.\n")
                print(f"Your final score was: {score}")
                time.sleep(3)
                game_over = True
                clear_screen()
                print(lost)
                time.sleep(2)
        else:
            # --- For any input provided other than A, a, B or b, 
            print("\nPlease enter either A or B. Another round will start in two seconds.")
            time.sleep(2)
            clear_screen()

# --- Start the game:
play_game()