from turtle import Turtle, Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
score = Score()
paddle = Paddle()
ball = Ball()

#screen settings
screen.title("Pong")
screen.bgcolor("black")
screen.setup(1200, 600)
screen.tracer(0)

#setting up game
score.dotted_line()
paddle.add_paddles()

#controls
screen.listen()

# Paddle 1 KEYS: W and S
screen.onkeypress(fun=paddle.paddle_1_go_up, key="w")
screen.onkeypress(fun=paddle.paddle_1_go_down, key="s")
screen.onkeyrelease(fun=paddle.paddle_1_stop_up, key="w")
screen.onkeyrelease(fun=paddle.paddle_1_stop_down, key="s")

# Paddle 2 KEYS: UPARROW, DOWNARROW
screen.onkeypress(fun=paddle.paddle_2_go_up, key="Up")
screen.onkeypress(fun=paddle.paddle_2_go_down, key="Down")
screen.onkeyrelease(fun=paddle.paddle_2_stop_up, key="Up")
screen.onkeyrelease(fun=paddle.paddle_2_stop_down, key="Down")

#main loop
game = True

while game:
    screen.update()
    score.score_one_update()
    score.score_two_update()
    time.sleep(0.0003)
    paddle.paddle_movement()
    ball.ball_move(paddle.paddles)

    ball.ball_reset(score)



screen.exitonclick()