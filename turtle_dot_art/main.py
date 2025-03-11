# import colorgram

# colors = colorgram.extract("turtle_dot_art/image.jpg", 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)
import turtle
import random
from turtle import Turtle, Screen
color_list = [(249, 249, 248), (250, 248, 250), (203, 172, 108), (220, 227, 234), (237, 245, 242), (153, 180, 195), (152, 186, 174), (193, 161, 176), (214, 203, 113), (208, 179, 195), (174, 188, 213), (161, 213, 187), (161, 203, 215), (114, 123, 186), (177, 160, 71), (213, 182, 181), (198, 207, 46), (105, 114, 142), (164, 121, 51)]

turtle.colormode(255)
turt = Turtle()
x = -300
y = 300

turt.hideturtle()
for _ in range(10):
    turt.penup()
    turt.goto(x, y)
    for i in range(10):
        turt.pendown()
        turt.dot(20, random.choice(color_list))
        turt.penup()
        turt.forward(50)

    y -= 50








screen = Screen()
screen.exitonclick()