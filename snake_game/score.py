from turtle import Turtle
import os

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("high_score.txt", "r") as high_score:
            self.high_score = high_score.read()

        self.color('white')
        self.penup()
        self.goto(0, 470)
        self.write(f"Current Score: {self.score} High Score {self.high_score}", move=False, align="center", font=('verdana', 20, 'normal'))
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"Current Score: {self.score} High Score {self.high_score}", move=False, align="center", font=('verdana', 20, 'normal'))

    def update_and_add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current Score: {self.score} High Score {self.high_score}", move=False, align="center", font=('verdana', 20, 'normal'))

    def reset(self):
        if self.score > int(self.high_score):
            print(f"{self.score} jest wyższe od {self.high_score}")

            with open("high_score.txt", "w") as score1:
                score1.write(str(self.score))

            self.high_score = self.score

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", move=False, align="center", font=('verdana', 20, 'normal'))