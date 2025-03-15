from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_player_one = 0
        self.score_player_two = 0
        #Turtle for first player score
        self.score1_turtle = Turtle()
        self.score1_turtle.clear()
        self.score1_turtle.color('white')
        self.score1_turtle.hideturtle()
        self.score1_turtle.penup()
        self.score1_turtle.goto(-50, 250)
        #Turtle for second player score
        self.score2_turtle = Turtle()
        self.score2_turtle.color('white')
        self.score2_turtle.hideturtle()
        self.score2_turtle.penup()
        self.score2_turtle.goto(50, 250)

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

    def score_one_update(self):
        self.score1_turtle.clear()
        self.score1_turtle.write(self.score_player_one, move=False, align="center", font=("Verdana", 30, "normal"))

    def score_two_update(self):
        self.score2_turtle.clear()
        self.score2_turtle.write(self.score_player_two, move=False, align="center", font=("Verdana", 30, "normal"))

    def raise_player_one(self):
        self.score_player_one += 1

    def raise_player_two(self):
        self.score_player_two += 1