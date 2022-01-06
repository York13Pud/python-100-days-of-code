# Import the random module:
import random

# Specify some nice ASCII art.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\033[1;37;40m'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\033[1;37;40m'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\033[1;37;40m'''

error = '''
___    ___
\  \  /  /
 \  \/  /
  |    |
 /  /\  \\
/__/  \__\\
\033[1;37;40m'''

# A nice welcome screen, because why not!
print('''\033[1;33;40m
#############################################
#                                           #
#                   Let's                   #
#                                           #
#                   Play                    #
#                                           #
#             Rock, Paper, Scissors         #
#                                           #
#############################################\033[1;37;40m\n\n''')

# Put the images variable names into a list.
images = [rock, paper, scissors, error]

# Request the users choice they wish to make:

your_choice = input(
    "\033[1;37;40mPlease make your choice? Press 0 for Rock, 1 for Paper or 2 for Scissors: ")
your_choice = int(your_choice)

# Display the users choice as ASCII art.
print(f"\033[1;35;40mYou chose:")
print(images[your_choice])

# Use a random number for the computers choice.
computers_choice = random.randint(0, 2)
print(f"\033[1;36;40mThe computer chose:")
print(images[computers_choice])

# Display the result of the game. Win lose or draw:
if (your_choice == 0) and (computers_choice == 0):
    print("\033[1;34;40mIt's a draw!\n")
elif (your_choice == 0) and (computers_choice == 1):
    print("\033[1;31;40mYou lost!\n")
elif (your_choice == 0) and (computers_choice == 2):
    print("\033[1;32;40mYou win!\n")
elif (your_choice == 1) and (computers_choice == 0):
    print("\033[1;32;40mYou win!\n")
elif (your_choice == 1) and (computers_choice == 1):
    print("\033[1;34;40mIt's a draw!\n")
elif (your_choice == 1) and (computers_choice == 2):
    print("\033[1;31;40mYou Lost!\n")
elif (your_choice == 2) and (computers_choice == 0):
    print("\033[1;31;40mYou Lost!\n")
elif (your_choice == 2) and (computers_choice == 1):
    print("\033[1;32;40mYou Win!\n")
elif (your_choice == 2) and (computers_choice == 2):
    print("\033[1;34;40mIt's a draw!\n")
else:
    print("\033[1;31;40mYou entered an invalid number. You lose!\n")
