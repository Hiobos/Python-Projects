import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# values = data["Primary Fur Color"].value_counts()
#
# new_file = pd.DataFrame(values)
#
# new_file.to_csv("squirrels.csv")

data = pd.read_csv("squirrels.csv")
print(data)