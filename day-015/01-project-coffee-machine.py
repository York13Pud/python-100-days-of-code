# --- Import required modules:
from main import MENU, resources, COIN_MENU, COIN_VALUES
from clear import clear_screen
import time

# --- Define the required variables for the program:
available_water = (resources["water"])
available_milk = (resources["milk"])
available_coffee = (resources["coffee"])
available_funds = float(0.00)


# --- Main Menu:
def main_menu():
    """This is the main menu of the coffee machine."""
    drink_choice = input(f"""
 --------------------------------------------------
|                     Main Menu                    |
|--------------------------------------------------|
|  Option  |         Description         |  Price  |
|--------------------------------------------------|
|     1    |  espresso                   |  £{MENU["espresso"]["cost"]:.2f}  |
|--------------------------------------------------|
|     2    |  latte                      |  £{MENU["latte"]["cost"]:.2f}  |
|--------------------------------------------------|
|     3    |  cappuccino                 |  £{MENU["cappuccino"]["cost"]:.2f}  |
|--------------------------------------------------|
|                                                  |
|--------------------------------------------------|
|     4    |  Add funds   |   Available: |  £{available_funds:.2f}  |
|--------------------------------------------------|
|                                                  |
|--------------------------------------------------|
|     5    |  Exit                                 |
 --------------------------------------------------
                         
Please enter the drink number you would like, add additional funds or exit: """)
    if drink_choice == "1":
        return check_resources("espresso")
    elif drink_choice == "2":
        return check_resources("latte")
    elif drink_choice == "3":
        return check_resources("cappuccino")
    elif drink_choice == "4":
        return add_funds()
    elif drink_choice == "5":
        print(f"\nThank you for using this machine. You have been refunded £{available_funds:.2f}.")
    # --- Display a report of what is left in the coffee machine:
    elif drink_choice == "report":
        status_report()
    # --- Turn off the Coffee Machine:
    elif drink_choice == "off" or drink_choice == "Off" or drink_choice == "OFF":
        print("Powering Off. You must be a tea drinker!!")
    else:
        print("Please enter a valid choice!")
        time.sleep(2)
        clear_screen()
        main_menu()

    
# --- Check resources sufficient:
def check_resources(drink):
    """This function will check that there is sufficient water, coffee, milk and funds available to process the requested drink. 
    If not, it will return to the main menu"""
    global available_water
    global available_milk
    global available_coffee
    global available_funds
    print(f"\nYou have selected a {drink}. Checking to see if there is sufficient water, milk and coffee available.")
    if available_coffee < (MENU[drink]["ingredients"]["coffee"]):
        print("\nThere is not enough coffee in the machine. Please request a refill.")
        input("\nPress any key to return to the main menu.")
        clear_screen()
        main_menu()
    elif available_milk < (MENU[drink]["ingredients"]["milk"]):
        print("\nThere is not enough milk in the machine. Please request a refill.")
        input("\nPress any key to return to the main menu.")
        clear_screen()
        main_menu()
    elif available_water < (MENU[drink]["ingredients"]["water"]):
        print("\nThere is not enough water in the machine. Please request a refill.")
        input("\nPress any key to return to the main menu.")
        clear_screen()
        main_menu()
    elif available_funds < (MENU[drink]["cost"]):
        print("\nThere are not enough funds in the machine. Please add additional funds.")
        print("\nReturning to the main menu. Please use option 4 to add funds.")
        input("\nPress any key to return to the main menu.")
        clear_screen()
        main_menu()
    else:
        available_water -= (MENU[drink]["ingredients"]["water"])
        available_milk -= (MENU[drink]["ingredients"]["milk"])
        available_coffee -= (MENU[drink]["ingredients"]["coffee"])
        available_funds -= (MENU[drink]["cost"])
        print("\nProcessing your drink. Please wait...")
        time.sleep(2)
        return make_coffee(drink,available_funds)


# --- Make Coffee:
def make_coffee(your_drink,remaining_funds):
    """This will complete the transaction, pour the drink and ask if the customer would like to buy another or finish."""
    print(f"\nPouring your {your_drink}, please wait...")
    time.sleep(5)
    print(f"\nYour {your_drink} is ready. Please take your {your_drink} from the machine.")
    buy_another = input("\nWould you like to buy another drink? Y/N: ")
    if buy_another == "Yes" or buy_another == "yes" or buy_another == "YES" or buy_another == "yes" or buy_another == "y" or buy_another == "Y":
        clear_screen()
        main_menu()
    else:
        print(f"\nThank you for your custom. You have been refunded £{remaining_funds:.2f}.")


# --- A function to Print a report:
def status_report():
    """This will produce a report of how much water, milk, coffee and funds are available in the machine."""
    clear_screen()
    print("Currently, this vending machine has:\n")
    print(f"Water: {available_water}ml")
    print(f"Milk: {available_milk}ml")
    print(f"Coffee: {available_coffee}g\n")
    print(f"Money: £{available_funds:.2f}\n")
    input("Press any key to return to the main menu.")
    clear_screen()
    main_menu()


# --- Process coins:
def add_funds():
    """This will present the customer with a menu to add additional funds to the machine and then return to the main menu when they are done."""
    global available_funds
    clear_screen()
    insert_coins = True
    while insert_coins is True:
        print(f"Available funds: £{available_funds:.2f}")
        coin_to_insert = input(COIN_MENU)
        if coin_to_insert == "M" or coin_to_insert == "m":
            insert_coins = False
            print("\nReturning to the main menu.")
            time.sleep(2)
            clear_screen()
            main_menu()
        elif int(coin_to_insert) in range(1,9):
            available_funds += float(COIN_VALUES["coins"][f"{coin_to_insert}"])
            clear_screen()
        else:
            input("Pease select a valid option from the above menu. Press any key to try again.")
            clear_screen()


# --- Start the program:
clear_screen()
main_menu()