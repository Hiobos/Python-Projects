from menu import MENU, resources
product = input("What type of coffee do u want? (espresso/latte/cappuccino)").lower()

machine = True

def coffee_make():
    global machine
    if product == 'report':
        print(resources)
    elif product == 'off':
        machine = False
    elif product in MENU:
        if resources['water'] > MENU[product]['resources']['water']:
            if resources['coffee'] > MENU[product]['resources']['coffee']:
                if resources['milk'] > MENU[product]['resources']['milk'] or ['milk'] not in MENU[product]['resources']:
                    pass #robi kawe
                else:
                    print("Not enough milk")
            else:
                print('Not enough coffee')
        else:
            print('Not enough water')


while machine:
    coffee_make()
