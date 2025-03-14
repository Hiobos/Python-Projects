from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 470)
        self.write(f"Current Score: 0", move=False, align="center", font=('verdana', 20, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current Score: {self.score}", move=False, align="center", font=('verdana', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align="center", font=('verdana', 20, 'normal'))