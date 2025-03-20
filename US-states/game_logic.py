from turtle import Turtle
import pandas as pd


class GameLogic(Turtle):
    def __init__(self):
        super().__init__()
        self.states = pd.read_csv("50_states.csv")
        self.states_right = []
        self.state_name = ''
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()

    def states_right(self):
        print(self.states.state)

    def check(self, next_state):
        for state in self.states.state:
            if next_state.title() == state:
                self.state_name = next_state
                self.states_right.append(next_state)

                x = int(self.states[self.states.state == self.state_name].x)
                y = int(self.states[self.states.state == self.state_name].y)
                self.turtle.goto(x, y)
                self.turtle.write(next_state)
                self.turtle.goto(0, 0)