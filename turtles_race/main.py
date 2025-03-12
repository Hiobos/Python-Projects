from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

race_on = False

bet = screen.textinput("Make a BET", "Which turtle will win?: ")

colors = ["red", "orange", "green", "yellow", "blue", "black"]
positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, positions[turtle_index])
    turtles.append(new_turtle)


if bet:
    race_on = True


while race_on:
    for turtle in turtles:
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
        if turtle.pos()[0] >= 230:
            print(f"Turtle {turtle.color()[0]} won")
            if turtle.color()[0] == bet:
                print("You won the bet!")
            else:
                print("Better luck next time!")
            race_on = False
    

screen.exitonclick()