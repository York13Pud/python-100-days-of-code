# Require art, clear and random modules
from art import logo
from clear import clear_screen
import random

# Generate a random number
def set_random_number():
    new_random_number = random.randint(1,100)
    return new_random_number

# Ask the player to determine the difficulty level they would like to set:
def set_difficulty():
    difficulty_choice = True
    while difficulty_choice == True:
        difficulty = input("Which difficulty level would you like to set?\n\nPlease enter either E for easy or H for hard: ")
        if difficulty == "E":
            print("\nYou selected easy. You will get a maximum of 10 guesses.")
            input("Press any key to begin..")
            clear_screen()
            difficulty_choice == False
            return 10
        elif difficulty == "H":
            print("\nYou selected hard. You will get a maximum of 5 guesses.")
            input("\nPress any key to begin..")
            clear_screen()
            difficulty_choice == False
            return 5

# Ask the player for a number and determine if it is higher, lower or the correct number.
# If the number of tries exceeds the maximum number of tries, it's game over!!
def guess_the_number():
    tries = 1
    try_again = True
    while try_again == True:
        guess = int(input(f"\033[1;36;40m\nGuess {tries}. \033[1;37;40mPlease enter a number between 1 and 100: "))
        if guess == RANDOM_NUMBER:
            try_again = False
            print(f"\033[1;32;40m\nThe number I thought of was {RANDOM_NUMBER}.")
            print("\n*** You have chosen, wisely. You Win! ***")
        elif tries == maximum_tries:
            try_again = False
            print(f"\033[1;31;40m\nThe number I thought of was {RANDOM_NUMBER}.")
            print("\n*** You have run out of tries. Game Over! ***")
        elif guess == 101:
            print(f"\033[1;33;40m\n*** You cheating son of a *!^$£. The number I thought of is {RANDOM_NUMBER} ***")
            print(f"You have {maximum_tries - tries} trie(s) remaining\033[1;37;40m")
            tries += 1            
        elif guess > RANDOM_NUMBER:
            print("\nThe number is higher than what I was thinking.")
            print(f"You have {maximum_tries - tries} trie(s) remaining")
            tries += 1
        elif guess < RANDOM_NUMBER:
            print("\nThe number is lower than what I was thinking.")
            print(f"You have {maximum_tries - tries} trie(s) remaining")
            tries += 1
            
# Set random_number to the number returned from set_random_number:
RANDOM_NUMBER = set_random_number()

# Clear the screen so the logo loads at the top of the terminal:
clear_screen()

# Print the fancy logo:
print(logo)

# Ask the player to press any key for no reason other than to see the logo first.
input("Press a key to begin...")

clear_screen()

# Set the maximum tries by calling the set_difficulty function:
maximum_tries = set_difficulty()

# Begin the guessing game by calling the guess_the_number function:
guess_the_number()