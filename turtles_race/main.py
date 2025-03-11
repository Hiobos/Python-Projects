from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput("Make a BET", "Which turtle will win?: ")

colors = ["red", "orange", "green", "yellow", "blue", "black"]
positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.color(colors[turtle_index])
    turt.penup()
    turt.goto(-230, positions[turtle_index])

game = True
while game:
    turt.forward(random.randint(0, 3))
    



screen.exitonclick()