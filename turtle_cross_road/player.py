from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
FINISH_LINE = 280
MOVE_BY = 20


class Player:
    def __init__(self):
        self.player = Turtle(shape='turtle')
        self.player.setheading(90)
        self.player.penup()
        self.player.goto(STARTING_POSITION)

    def player_move_forward(self):
        self.player.forward(MOVE_BY)

    def player_move_backwards(self):
        if self.player.position()[1] > -280:
            self.player.backward(MOVE_BY)

    def player_check_score(self, cars):
        if self.player.position()[1] >= FINISH_LINE:
            self.player.goto(STARTING_POSITION)
            return True

    def player_check_collision(self, cars):
        for car in cars:
            if self.player.distance(car) < 5:
                return True