from turtle import Turtle
import random

COLORS = ['orange', 'red', 'blue', 'purple', 'green', 'yellow']

cars = []

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []


    def generate_cars(self):
        if len(self.cars) < 20:
            y_axis = random.randrange(-260, 280, 20)
            x_axis = random.randrange(-300, 300)
            car = Turtle(shape='square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(x_axis, y_axis)
            self.cars.append(car)
        for car in self.cars:
            car.forward(10)
            if car.position()[0] < -300:
                y_axis = random.randrange(-260, 280, 20)
                car.goto(300, y_axis)

    def clean_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()