from info import MENU
from colorama import Fore
from art import logo

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many ₹10 rupee coins?: ")) * 10
    total += int(input("how many ₹5 rupee coins?: ")) * 5
    total += int(input("how many ₹2 rupee coins?: ")) * 2
    total += int(input("how many ₹1 rupee coins?: ")) * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(Fore.RED + "Sorry that's not enough money. Money refunded." + Fore.RESET)
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    print(Fore.BLUE + logo + Fore.RESET)
    print(Fore.CYAN + "***************************************************************************" + Fore.RESET)
    print(Fore.MAGENTA + "The cost of Espresso Coffee is ₹15." + Fore.RESET)
    print(Fore.WHITE + "The cost of Latte Coffee is ₹20." + Fore.RESET)
    print(Fore.GREEN + "The cost of Cappuccino Coffee is ₹25." + Fore.RESET)
    print(Fore.CYAN + "***************************************************************************" + Fore.RESET)
    choice = input(Fore.YELLOW + "​What would you like? (espresso/latte/cappuccino): ".lower() + Fore.RESET)
    if choice == "off".lower():
        is_on = False
    elif choice == "report".lower():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
