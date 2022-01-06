# Import the random module:
import random

# Setup a variable for the randomised number:
coin_toss = random.randint(0, 1)
# print(coin_toss)

# Display the result. 1 = Heads:
if coin_toss == 1:
    print("Heads")
else:
    print("Tails")
