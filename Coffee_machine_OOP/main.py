from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

machine = True
options = ["espresso", "latte", "cappuccino", "off", "report"]



while machine:
    choice = input(f"What would you like? espresso/latte/cappuccino: ").lower()
    if choice in options:
        if choice == 'off':
            machine = False
        elif choice == 'report':
            coffe_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffe_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)
    else:
        print("invalid option.")