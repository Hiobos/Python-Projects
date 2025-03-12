from turtle import Turtle, Screen

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title("Snake Game")

snake_body = []

starting_position_x = [0, -20, -40]
for index in range(0, 2):
    snake_chunk = Turtle()
    snake_chunk.shape('square')
    snake_chunk.color('green')
    snake_chunk.position()



screen.exitonclick()