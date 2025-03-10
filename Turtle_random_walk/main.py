import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
turt = Turtle()
turt.speed(500)
turt.pensize(15)
rotates = [0, 90, 180, -90]


def rand_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color


for _ in range(500):
    rotate = random.choice(rotates)
    turt.color(rand_color())
    turt.forward(30)
    turt.right(rotate)





screen = Screen()
screen.exitonclick()