from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 470)
        self.write(f"Current Score: 0", move=False, align="center", font=('Arial', 20))
        self.hideturtle()

    def update_score(self, passed_score):
        self.clear()
        self.write(f"Current Score: {passed_score}", move=False, align="center", font=('Arial', 20))