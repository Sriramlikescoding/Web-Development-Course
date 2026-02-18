import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np
data = pd.read_csv("gapminder(2007).csv")
print(data.info())
print(data.head())
continent_count = data.groupby("continent").size()
p.figure(figsize=(7,7))
p.pie(continent_count, labels = continent_count.index, autopct='%.2f%%', labeldistance = 1.15, wedgeprops = {"linewidth":2, "edgecolor":"white"})
p.title("Distribution of countries by continent")
p.show()