from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Constant var
REPORT = 'report'

machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    usr_order = input(f"What do you want({menu.get_items()})?")
    if usr_order == REPORT:
        coffee_maker.report()
        money_machine.report()
    else:
        drink_details = menu.find_drink(usr_order)
        if drink_details is not None:
            if coffee_maker.is_resource_sufficient(drink_details):
                if money_machine.make_payment(drink_details.cost):
                    coffee_maker.make_coffee(drink_details)


