from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        ball = Turtle(shape='circle')
        ball.color('red')
        ball.penup()
        rand_x = random.randint(-2, 2)
        rand_y = random.randint(-2, 2)
        ball.goto(rand_x, rand_y)
        self.ball = ball
        self.ball.dx = 1
        self.ball.dy = 1

    def ball_move(self, paddle):
        ball = self.ball
        ball.setx(ball.xcor() + self.ball.dx)
        ball.sety(ball.ycor() + self.ball.dy)

        #bouncing from walls
        if ball.ycor() > 290:
            ball.sety(290)
            self.ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            self.ball.dy *= -1

        #bouncing from paddles
        if ball.xcor() > 550 and ball.xcor() < 560 and ball.ycor() < paddle[1].ycor() + 40 and ball.ycor() > paddle[1].ycor() -40:
            self.ball.dx *= -1

        if ball.xcor() < -550 and ball.xcor() > -560 and ball.ycor() < paddle[0].ycor() + 40 and ball.ycor() > paddle[0].ycor() -40:
            self.ball.dx *= -1

    def ball_reset(self, score):
        ball = self.ball
        if ball.xcor() > 600:
            score.raise_player_one()
            ball.goto(0, 0)
        if ball.xcor() < -600:
            score.raise_player_two()
            ball.goto(0, 0)


