from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

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

score = Score()
food = Food()

passed_score = 0
game = True
while game:
    screen.update()
    time.sleep(0.05)
    #food
    snake.move()

    if snake.head.distance(food) < 15:
        passed_score += 1
        snake.add_chunk()
        food.new_food()
        score.update_score(passed_score)





screen.exitonclick()