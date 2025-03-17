#turtle cross road game
from turtle import Screen, Turtle
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
import time

#screen settings
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

#initializing
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#controls
screen.listen()
screen.onkeypress(key='Up', fun=player.player_move_forward)
screen.onkeypress(key='Down', fun=player.player_move_backwards)

screen.onkeypress(key='r', fun=scoreboard.update_score)
screen.onkeypress(key='c', fun=car_manager.clean_cars)

#main loop
game = True
while game:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()

    if player.player_check_collision(car_manager.cars):
        game = False

    if player.player_check_score(car_manager.cars):
        scoreboard.update_score()
        #car_manager.up_speed()
        car_manager.clean_cars()
    else:
        pass