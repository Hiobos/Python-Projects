import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
turt = Turtle()
turt.speed('fastest')
turt.pensize(2)
rotates = [0, 90, 180, -90]


def rand_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color

for _ in range(180):
    turt.color(rand_color())
    turt.circle(200)
    current_position = turt.heading()
    turt.setheading(current_position + 5)





screen = Screen()
screen.exitonclick()