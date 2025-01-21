import art
print(art.logo)

# Constant variables
REPORT = 'report'
ESPRESSO = 'espresso'
LATTE = 'latte'
CAPPUCCINO = 'cappuccino'
INGREDIENTS = 'ingredients'
COST = 'cost'
WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

# Functions
def set_water(w):
    global water
    water = w
def set_milk(m):
    global milk
    milk = m
def set_coffee(c):
    global coffee
    coffee = c

def report():
    print(f"Water: {water}ml\n"
          f"Milk: {milk}ml\n"
          f"Coffee: {coffee}g\n"
          f"Money: ${money}\n")

def user_input_payment():
    pay_quarters = int(input("How many quarters? "))
    pay_dimes = int(input("How many dimes? "))
    pay_nickles = int(input("How many nickles? "))
    pay_pennies = int(input("How many pennies? "))
    return calculate(pay_quarters, pay_dimes, pay_nickles, pay_pennies)
def calculate(quarters, dimes, nickles, pennies) -> int:
    sum_usr_payment = 0
    for key in COIN_VALUES:
        if key == 'quarter':
            sum_usr_payment += quarters * COIN_VALUES[key]
        elif key == 'dime':
            sum_usr_payment += dimes * COIN_VALUES[key]
        elif key == 'nickel':
            sum_usr_payment += nickles * COIN_VALUES[key]
        elif key == 'penny':
            sum_usr_payment += pennies * COIN_VALUES[key]
    return sum_usr_payment

def process_transaction(drink, usr_pay):
    global money, give_change, water, coffee, milk
    for typ in MENU:
        if typ == drink:
            if usr_pay >= MENU[typ][COST]:
                if has_inventory(typ):
                    money += MENU[typ][COST]
                    water -= MENU[typ][INGREDIENTS][WATER]
                    coffee -= MENU[typ][INGREDIENTS][COFFEE]
                    if typ != ESPRESSO:
                        milk -= MENU[typ][INGREDIENTS][MILK]
                    give_change = usr_pay - MENU[typ][COST]
                    print(f"Here is ${round(give_change,2)} in change.")
                    return True
                elif not has_inventory(typ):
                    print("Sorry there is not enough inventory.")
            else:
                print("Sorry that's not enough money. Money refunded.")
                return False

def has_inventory(drink_typ) -> bool:
    if MENU[drink_typ][INGREDIENTS][WATER] <= water and MENU[drink_typ][INGREDIENTS][COFFEE] <= coffee:
        if drink_typ != ESPRESSO:
            if MENU[drink_typ][INGREDIENTS][MILK] <= milk:
                return True
        else:
            return True
    else:
        return False

def order(drink_type):
    print("Please insert coins.")
    sum_usr_payment = user_input_payment()
    if process_transaction(drink_type, sum_usr_payment):
        print(f"Here is your {drink_type} ☕️ Enjoy!")

# Variables
water = 0
milk = 0
coffee = 0
money = 0
machine_on = True
receive_payment = 0
give_change = 0

# Main body
set_water(300)
set_milk(200)
set_coffee(100)
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == REPORT:
        report()
    else:
        order(user_choice)




















