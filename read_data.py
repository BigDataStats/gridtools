import pandas as pd
import numpy as np
import datetime as dt

datetime_cols = ["started_on", "updated_date", "completed_on", "esimtated_time_arrive"]
rides = pd.read_csv("C:/Users/mbg877/Datasets/Rides_C.csv", na_values = ["NA", "NaN"], parse_dates = datetime_cols)
rides.drop("Unnamed: 0", axis = 1, inplace = True)
rides.head()

time_ls = np.arange(23) # hour of the day
long_ls = np.linspace(rides["end_location_long"].min(), rides["end_location_long"].max(), 10)
lat_cut = np.linspace(rides["end_location_lat"].min(), rides["end_location_lat"].max(), 10)
out_ls = np.array([0, 50, 100])

z = rides["total_fare"]

pd2 = pd.DataFrame()
pd2["end_location_lat"] = rides["end_location_lat"]
pd2["latcut"] = pd.cut(pd2["end_location_lat"], lat_cut)

lat_counts = pd2["latcut"].value_counts()

# First let's count space only

#for i, x in enumerate(long_ls):
#    for j, y in enumerate(lat_ls):
#        