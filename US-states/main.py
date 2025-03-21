import turtle
from game_logic import GameLogic
import string

#screen setup with image of the states
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S states game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#main game loop
game = True

gl = GameLogic()

while game:
    next_state = turtle.textinput(title=f"{len(gl.states_right)}/50 State name", prompt="What's the next state?:  ")
    gl.check(string.capwords(next_state))
    if len(gl.states_right) == 50:
        game = False
        print("U won!")
    elif next_state.lower() == "exit":
        game = False
        gl.generate_csv()