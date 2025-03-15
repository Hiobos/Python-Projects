from turtle import Turtle

POSITIONS = [(-560, 0), (560, 0)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.paddle_1_up = False
        self.paddle_1_down = False
        self.paddle_2_up = False
        self.paddle_2_down = False

    def add_paddles(self):
        for index in POSITIONS:
            paddle = Turtle()
            paddle.setheading(90)
            paddle.penup()
            paddle.color('white')
            paddle.hideturtle()
            paddle.goto(index)
            paddle.shape('square')
            paddle.shapesize(stretch_wid=1, stretch_len=5)
            paddle.showturtle()
            self.paddles.append(paddle)

    def paddle_1_go_up(self):
        self.paddle_1_up = True

    def paddle_1_go_down(self):
        self.paddle_1_down = True

    def paddle_1_stop_up(self):
        self.paddle_1_up = False

    def paddle_1_stop_down(self):
        self.paddle_1_down = False

    def paddle_2_go_up(self):
        self.paddle_2_up = True

    def paddle_2_go_down(self):
        self.paddle_2_down = True

    def paddle_2_stop_up(self):
        self.paddle_2_up = False

    def paddle_2_stop_down(self):
        self.paddle_2_down = False

    def paddle_movement(self):
        # movement paddle 1
        if self.paddle_1_up and self.paddles[0].ycor() < 260:
            self.paddles[0].sety(self.paddles[0].ycor() + 5)
        if self.paddle_1_down and self.paddles[0].ycor() > -260:
            self.paddles[0].sety(self.paddles[0].ycor() - 5)

        # movement paddle 2
        if self.paddle_2_up and self.paddles[1].ycor() < 260:
            self.paddles[1].sety(self.paddles[1].ycor() + 5)
        if self.paddle_2_down and self.paddles[1].ycor() > -260:
            self.paddles[1].sety(self.paddles[1].ycor() - 5)