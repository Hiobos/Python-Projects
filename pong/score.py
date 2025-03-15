from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_player_one = 0
        self.score_player_two = 0

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

    def score_one_turtle(self):
        score1_turtle = Turtle()
        score1_turtle.clear()
        score1_turtle.color('white')
        score1_turtle.hideturtle()
        score1_turtle.penup()
        score1_turtle.goto(-50, 250)
        score1_turtle.clear()
        score1_turtle.write(self.score_player_one, move=False, align="center", font=("Verdana", 30, "normal"))

    def score_two_turtle(self):
        score2_turtle = Turtle()
        score2_turtle.color('white')
        score2_turtle.hideturtle()
        score2_turtle.penup()
        score2_turtle.goto(50, 250)
        score2_turtle.clear()
        score2_turtle.write(self.score_player_two, move=False, align="center", font=("Verdana", 30, "normal"))

    def raise_player_one(self):
        self.score_player_one += 1

    def raise_player_two(self):
        self.score_player_two += 1