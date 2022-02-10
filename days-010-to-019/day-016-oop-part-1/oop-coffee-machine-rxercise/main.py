# --- Import the required modules:
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# --- Create new objects using the imported classes:
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# --- Set power status to True to start with:
power_on = True

while power_on:
    # --- Get the list of drink options from the get_items method:
    options = menu.get_items()
    # --- Ask the customer what they want:
    customers_choice = input(f"What would you like? ({options}): ")
    # --- Turn off the machine if "off" is chosen
    if customers_choice == "off":
        power_on = False
        print("Powering Off...")
    # --- Print a report if "report" is chosen:
    elif customers_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
    # --- Otherwise, process the drink:
        drink = menu.find_drink(customers_choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)