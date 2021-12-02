from art import logo
import os
clear = lambda: os.system('clear')

# Create an empty list
bids = list()

# Create a new function to play the game.
def new_bidder():
    # Create an empty (or empty the existing) dictionary.
    new_bid = {}
    # Ask the bidder to enter their name and their bid price
    new_bid["bidder"] = input("Please enter your name: ")
    new_bid["bid_price"] = int(input("\nPlease enter your bid price: £"))
    # Add the bid to the list.
    bids.append(new_bid)
    
    # Ask the player if there is another bidder. If yes, play again. If no, determin the winner.
    play_again = input("\nWould you like to add another bidder? y/n: ")
    if play_again =="y" or play_again =="Y":
        clear()
        new_bidder()
    else:
        winning_bid = max([bid['bid_price'] for bid in bids])
        winning_bidder = next(winner for winner in bids if winner["bid_price"] == winning_bid)
        print(f"\nThe winning bidder is {winning_bidder['bidder']} with a bid of £{winning_bidder['bid_price']}")
        print("\nThank you for playing!")

# Display the logo, a greeting and call the new_bidder function.
print(logo)
print("\nWelcome to the secret bidder game!\n")
new_bidder()