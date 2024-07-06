from menu import *

money = 0
machine = True


def coffee_make():
    global machine
    global money
    product = input("What type of coffee do u want? (espresso/latte/cappuccino): ").lower()
    if product == 'report':
        print(resources)
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif product == 'off':
        machine = False
    elif product in MENU:
        if resources['water'] > MENU[product]['ingredients']['water']:
            if resources['coffee'] > MENU[product]['ingredients']['coffee']:
                if resources['milk'] in MENU[product]['ingredients'] and resources['milk'] > MENU[product]['ingredients']['milk'] or resources['milk'] not in MENU[product]['ingredients']:
                    if money >= MENU[product]['cost']:
                        print(f"Enjoy your {product}!")
                        money = money - MENU[product]['cost']
                        print(MENU[product]['cost'])
                        print(f"You have ${money} left.")
                    else:
                        print("Not enough money.")
                else:
                    print("Not enough milk")
            else:
                print('Not enough coffee')
        else:
            print('Not enough water')

def paying():
    global money
    quarters = int(input("How many quarters?: ")) #0.25
    dimes = int(input("How many dimes?: ")) #0.10
    nickles = int(input("How many nickles?: ")) #0.05
    pennies = int(input("How many pennies?: ")) #0.01
    sum = float(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies)
    money = sum

paying()
while machine:
    coffee_make()
