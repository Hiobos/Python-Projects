from turtle import Turtle
from score import Score
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        ball = Turtle(shape='circle')
        ball.color('red')
        ball.penup()
        ball.goto(0, 0)
        self.ball = ball

    def ball_move(self, paddle):
        ball = self.ball
        ball.forward(1)

        #print(ball.xcor())
        if ball.xcor() > 550 and ball.xcor() < 560 and ball.ycor() < paddle.ycor() + 40 and ball.ycor() > paddle.ycor() -40:
            pass

    def ball_reset(self, score):
        ball = self.ball
        if ball.xcor() > 600:
            score.raise_player_one()
            ball.goto(0, 0)
        if ball.xcor() < -600:
            score.raise_player_two()
            ball.goto(0, 0)


