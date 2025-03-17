from turtle import Turtle

FONT = ("Courier", 12, "normal")
POSITION = (-260, 280)

class Scoreboard:
    def __init__(self):
        turtle = Turtle()
        turtle.color('black')
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(POSITION)
        self.score = 0
        self.turtle = turtle
        turtle.write("Score: 0", font=FONT)

    def update_score(self):
        self.score += 1
        self.turtle.clear()
        self.turtle.write(f"Score: {self.score}", font=FONT)