from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

game = True
while game:
    screen.update()
    time.sleep(0.05)
    snake.move()

    screen.onkeypress(key='Left', fun=snake.move_left)
    screen.onkeypress(key='Right', fun=snake.move_right)
    screen.onkeypress(key='Up', fun=snake.move_up)
    screen.onkeypress(key='Down', fun=snake.move_down)


screen.exitonclick()