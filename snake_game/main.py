from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title("Snake Game")
#turns off animations
screen.tracer(0)

snake = Snake()
#screen listening for key presses
screen.listen()
screen.onkeypress(key='Left', fun=snake.move_left)
screen.onkeypress(key='Right', fun=snake.move_right)
screen.onkeypress(key='Up', fun=snake.move_up)
screen.onkeypress(key='Down', fun=snake.move_down)

score = Score()
food = Food()

#main loop
game = True
while game:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #detects collision with food
    if snake.head.distance(food) < 15:
        #passed_score += 1
        snake.add_chunk()
        food.new_food()
        score.update_score()

    #detects collision with walls
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490:
        score.game_over()
        game = False


    #detects collision of snake head with its body
    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 10:
            score.game_over()
            game = False




screen.exitonclick()