import random
from art import *
from game_data import data

#print(data[0]['country'])
def start_data():
    global game
    global score
    global rand_number1
    global rand_number2
    score = 0
    rand_number1 = random.randint(0, len(data)-1)
    rand_number2 = random.randint(0, len(data)-1)
    game = True

start_data()


def game_start():
    global game
    global score
    global rand_number1
    global rand_number2
    #checks if random number 1 is equal to random number 2, if it is then keep re-rolling
    while rand_number1 == rand_number2:
        rand_number2 = random.randint(0, len(data))
    print(logo)
    print(f"A: Name: {data[rand_number1]['name']}, {data[rand_number1]['description']}, from {data[rand_number1]['country']}")
    print(vs)
    print(f"B: Name: {data[rand_number2]['name']}, {data[rand_number2]['description']}, from {data[rand_number2]['country']}")
    pick = input("Type A or B to choose: ").lower()

    if pick == 'a':
        if data[rand_number1]['follower_count'] >= data[rand_number2]['follower_count']:
            rand_number2 = random.randint(0, len(data)-1)
            score += 1
            game_start()
        else:
            game = False
            print(f"You lose, your score was: {score}")
    elif pick == 'b':
        if data[rand_number2]['follower_count'] >= data[rand_number1]['follower_count']:
            rand_number1 = random.randint(0, len(data)-1)
            score += 1
            game_start()
        else:
            game = False
            print(f"You lose, your score was: {score}")


def gameplay():
    global game
    while game:
        game_start()
    play_again = input("Do you want to play again? y/n: ").lower()
    if play_again == 'y':
        game = True
        start_data()
        gameplay()
    else:
        print("Thanks for playing.")


gameplay()