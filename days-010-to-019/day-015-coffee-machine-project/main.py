MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_MENU = """
Please insert your coins.
==========================
Press 1 for a 1p coin.
Press 2 for a 2p coin.
Press 3 for a 5p coin.
Press 4 for a 10p coin.
Press 5 for a 20p coin.
Press 6 for a 50p coin.
Press 7 for a £1 coin.
Press 8 for a £2 coin.
Press M to return to the main menu.
"""

COIN_VALUES = {
    "coins": {
        "1": 0.01,
        "2": 0.02,
        "3": 0.05,
        "4": 0.10,
        "5": 0.20,
        "6": 0.50,
        "7": 1.00,
        "8": 2.00,
    }
}