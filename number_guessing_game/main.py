#simple number guessing game 1-100, 3 difficulty levels easy-10 tries, hard-5, very hard-3
import random

attempts = {
    'easy': 10,
    'hard': 5,
    'very hard': 3
}


def game_start():
    print("I'm guessing random number in range 1-100")
    TO_GUESS = random.randint(1, 100)

    difficulty = input("Select difficulty, type easy, hard or 'very hard': ").lower()
    if difficulty not in attempts:
        return
    life = attempts[difficulty]
    game = True
    while game:
        if life == 0:
            print(f"You lose, the number was: {TO_GUESS}")
            game = False
        else:
            number = int(input("Enter number: "))
            life -= 1
            if number > TO_GUESS:
                print("Too high")
            elif number < TO_GUESS:
                print("Too low")
            else:
                print("You won!")
                game = False
game_start()
play_again = True
while play_again:
    answer = input("Do you want to play again? y/n: ").lower()
    if answer == 'y':
        game_start()
    else:
        break
print("Thanks for playing.")
