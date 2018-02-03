import pandas as pd
import numpy as np

# Read data set
datetime_cols = ["started_on", "updated_date", "completed_on", "esimtated_time_arrive"]
rides = pd.read_csv("C:/Users/mbg877/Datasets/Rides_C.csv", na_values = ["NA", "NaN"], parse_dates = datetime_cols)
rides.drop("Unnamed: 0", axis = 1, inplace = True)
rides = rides[rides["total_fare"] < 100]

# Sample rows 
#N = 10000
#rides = rides.sample(N)

# Choose columns
cols = ["rider_id", "started_on", "completed_on", "start_location_long", "start_location_lat", 
        "end_location_long", "end_location_lat", "total_fare", ]
rides = rides[cols]

# Create variable for weekday and variable
weekday = 1 # let's start with mondays
rides["weekday"] = [x.weekday() for x in rides["completed_on"]]
rides["hour"] = [x.hour for x in rides["completed_on"]]
rides = rides[rides["weekday"] == 0]

# Create variable for spatial location
# Create Linspace
resol = 25
min_lat = min(rides["start_location_lat"].min(), rides["end_location_lat"].min())
min_lon = min(rides["start_location_long"].min(), rides["end_location_long"].min())
max_lat = max(rides["start_location_lat"].max(), rides["end_location_lat"].max())
max_lon = max(rides["start_location_long"].max(), rides["end_location_long"].max())
lat_cut = np.linspace(min_lat, max_lat, resol)
lon_cut = np.linspace(min_lon, max_lon, resol)

# Cuts
rides["end_lat_cut"] = pd.cut(rides["end_location_lat"], lat_cut)
rides["end_lon_cut"] = pd.cut(rides["end_location_long"], lon_cut)

# Cut the outut variable
min_out = rides["total_fare"].min()
max_out = rides["total_fare"].max()
range_out = max_out - min_out

nlevels = 5
for i in range(nlevels + 1):
    cut = np.linspace(min_out, max_out, 2 ** i + 2)
    label = "total_fare_cut" + str(i + 1)
    rides[label] = pd.cut(rides["total_fare"], cut)


# Store data fur cut lebel