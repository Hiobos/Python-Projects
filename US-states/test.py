import pandas as pd

data = pd.read_csv('50_states.csv')

#print(data.state)

#print(len(data.state))

state_check = 'Alabama'

for state in data.state:
    if state_check == state:
        print("jest")

print(int(data[data.state == "Alabama"].x))