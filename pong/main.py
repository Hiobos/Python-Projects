from turtle import Turtle, Screen
from score import Score
from paddle import Paddle

screen = Screen()
score = Score()
paddle = Paddle()

#screen settings
screen.bgcolor("black")
screen.setup(1200, 600)
#screen.tracer(0)

#setting up game
score.dotted_line()
paddle.add_paddles()

#controls
screen.listen()
# Paddle 1: W, S
screen.onkeypress(fun=paddle.paddle_1_go_up, key="w")
screen.onkeypress(fun=paddle.paddle_1_go_down, key="s")
screen.onkeyrelease(fun=paddle.paddle_1_stop_up, key="w")
screen.onkeyrelease(fun=paddle.paddle_1_stop_down, key="s")

# Paddle 2: Up, Down
screen.onkeypress(fun=paddle.paddle_2_go_up, key="Up")
screen.onkeypress(fun=paddle.paddle_2_go_down, key="Down")
screen.onkeyrelease(fun=paddle.paddle_2_stop_up, key="Up")
screen.onkeyrelease(fun=paddle.paddle_2_stop_down, key="Down")


game = True

while game:
    screen.update()
    paddle.paddle_movement()





screen.exitonclick()