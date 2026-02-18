import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np
data = pd.read_csv("Weather_Data.csv")
print(data.info())
print(data.head())
datagroup = data.groupby("month").mean(numeric_only = True)
#groups graph by month, then averages column, n
datagroup = datagroup.reset_index()
#groups data not by month
p.figure(figsize = (8, 5))
datagroup.plot.area(x="month", y = "Humidity", alpha = 0.6)
p.title("Average monthly humidity")
p.xlabel("Humidity")
p.ylabel("Month")
#Alpha is transparency
p.show()
p.figure(figsize = (8,5))
p.plot(data["Temperature (C)"])
p.title("Temperature over time")
p.xlabel("Reading number over time")
p.ylabel("Temperature")
p.show()