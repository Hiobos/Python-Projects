from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.color('black')