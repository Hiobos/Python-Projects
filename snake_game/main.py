from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkeypress(key='Left', fun=snake.move_left)
screen.onkeypress(key='Right', fun=snake.move_right)
screen.onkeypress(key='Up', fun=snake.move_up)
screen.onkeypress(key='Down', fun=snake.move_down)

food = Food()

game = True
while game:
    screen.update()
    time.sleep(0.05)
    #food
    snake.move()

    if snake.head.distance(food) < 15:
        screen.bgcolor('purple')
        snake.add_chunk()
        food.new_food()
    snake.snake_body[-1].color('green')





screen.exitonclick()