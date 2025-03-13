from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

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
            self.snake_body[0].color('white')

    def move(self):
        for chunk in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[chunk - 1].xcor()
            new_y = self.snake_body[chunk - 1].ycor()
            self.snake_body[chunk].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_right(self):
        if self.snake_body[0].heading() != 180.0:
            self.snake_body[0].setheading(0)

    def move_left(self):
        if self.snake_body[0].heading() != 0.0:
            self.snake_body[0].setheading(180)

    def move_up(self):
        if self.snake_body[0].heading() != 270.0:
            self.snake_body[0].setheading(90)

    def move_down(self):
        if self.snake_body[0].heading() != 90.0:
            self.snake_body[0].setheading(270)

