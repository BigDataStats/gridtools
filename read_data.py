import pandas as pd

rides = pd.read_csv("C:/Users/mbg877/Datasets/Rides_C.csv", na_values = "NA")

rides.drop(["Unnamed: 0"], axis = 1)

rides.describe()


rides.iloc[:, :10].head()