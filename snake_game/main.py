from turtle import Turtle, Screen

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title("Snake Game")

snake_body = []

starting_position_x = [(0, 0), (-20, 0), (-40, 0)]
for index in range(0, 3):
    snake_chunk = Turtle(shape='square')
    screen.tracer(2, 0)
    snake_chunk.color('green')
    snake_chunk.penup()
    snake_chunk.goto(starting_position_x[index])
    snake_body.append(snake_chunk)

game = True

while game:
    for chunk in snake_body:
        chunk.forward(10)


screen.tracer(1, 0)
screen.exitonclick()