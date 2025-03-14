from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def dotted_line(self):
        self.penup()
        self.color('white')
        self.width(4)
        self.goto(0, -280)
        self.setheading(90)
        while self.ycor() <= 280:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)