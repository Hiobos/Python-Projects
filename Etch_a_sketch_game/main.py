from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

turt.setheading(90)

def move_forward():
    turt.forward(10)

def move_right():
    new_heading = turt.heading() - 10
    turt.setheading(new_heading)

def move_left():
    new_heading = turt.heading() + 10
    turt.setheading(new_heading)

def move_backwards():
    turt.backward(10)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.setheading(90)
    turt.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='c', fun=clear)
screen.exitonclick()