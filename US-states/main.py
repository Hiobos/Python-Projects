import turtle
from game_logic import GameLogic

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
print(len(gl.states_right))

while game:
    next_state = turtle.textinput(title=f"{50-len(gl.states_right)}/50 State name", prompt="What's the next state?:  ")
    gl.check(next_state)



turtle.mainloop()