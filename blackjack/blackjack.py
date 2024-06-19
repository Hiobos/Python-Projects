import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sumowanie_pkt():
    global player_score, pc_score
    player_score = sum(player)
    pc_score = sum(pc)


def wypisz_pkt():
    print(f"Twoje karty to: {player}")
    print(f"Komputer {pc[:-1]} + x")


def wypisz_sume_pkt():
    print(f"Miałeś: {player_score} punktów.")
    print(f"Komputer miał {pc_score} punktów.")


def win_blackjack():
    global game
    if player_score == 21 and pc_score == 21:
        print('Remis')
        wypisz_sume_pkt()
        game = False
    elif player_score == 21:
        print('Wygrałeś, Blackjack!')
        wypisz_sume_pkt()
        game = False
    elif pc_score == 21:
        print('Komputer wygrał, Blackjack!')
        wypisz_sume_pkt()
        game = False


def over_blackjack():
    global game
    if player_score > 21:
        if 11 in player:
            as_index = 11 in player
            player[as_index] = 1
            sumowanie_pkt()
            over_blackjack()
        else:
            print('Przegrałeś!')
            wypisz_sume_pkt()
            game = False


def pc_add_card():
    while pc_score < 17:
        pc.append(random.choice(cards))
        sumowanie_pkt()


def add_card():
    global game
    while game:
        answer = input("Czy chcesz dobrać kolejną kartę? y/n: ").lower()
        if answer == 'n':
            break
        elif answer == 'y':
            player.append(random.choice(cards))
            sumowanie_pkt()
            if player_score > 21:
                over_blackjack()
                game = False
                break
        else:
            print("Zła odpowiedź")
            add_card()


def compare_score():
    global game
    if player_score <= 21 and pc_score <= 21:
        if player_score > pc_score:
            print("Wyrgywasz!")
        elif pc_score > player_score:
            print("Przegrałeś")
        elif pc_score == player_score:
            print("Remis")
    wypisz_sume_pkt()
    game = False


def start_game():
    global game, pc, player
    game = True
    pc = []
    player = []

    pc.append(random.choice(cards))
    pc.append(random.choice(cards))
    player.append(random.choice(cards))
    player.append(random.choice(cards))

    sumowanie_pkt()
    wypisz_pkt()
    win_blackjack()

    if game:
        add_card()
    if game:
        pc_add_card()
        sumowanie_pkt()
        compare_score()

while True:
    start_game()
    play_again = input("Czy chcesz zagrać znowu? y/n: ").lower()
    if play_again != 'y':
        break

print("Koniec")