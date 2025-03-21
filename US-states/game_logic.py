from turtle import Turtle
import pandas as pd
from _collections import deque
from pandas.core.interchange.dataframe_protocol import DataFrame


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

    def generate_csv(self):
        all_states = deque(self.states.state.to_list())
        all_states.appendleft("States you've missed:")
        right_states = self.states_right
        states_wrong = [x for x in all_states if x not in right_states]
        df = pd.DataFrame(states_wrong)
        df.to_csv("States_wrong.csv")