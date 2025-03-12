from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()


    def create_snake(self):
        for index in STARTING_POSITIONS:
            snake_chunk = Turtle(shape='square')
            snake_chunk.color('green')
            snake_chunk.penup()
            snake_chunk.goto(index)
            self.snake_body.append(snake_chunk)

    def move(self):
        for chunk in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[chunk - 1].xcor()
            new_y = self.snake_body[chunk - 1].ycor()
            self.snake_body[chunk].goto(new_x, new_y)
            self.snake_body[0].forward(10)