from turtle import Turtle
from snake import Snake
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 480)
        self.goto(random_x, random_y)

    def new_food(self):
        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 480)
        self.goto(random_x, random_y)
