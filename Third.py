import matplotlib.pyplot as p
import pandas as pd
Countries_Data = pd.read_csv("Countries_Data.csv")
countries = Countries_Data
countries.head(3)
c_52 = countries.loc[countries["year"]==1952]
c_52.head()
c_07 = countries.loc[countries["year"]==2007]
c_07.head()
c_merge = c_52.merge(c_07, left_on="country", right_on="country")
c_merge.head()
c_merge.drop(["year_x", "year_y"], axis=1)
c_merge.head()
c_merge["population_growth"] = (c_merge["population_y"]-c_merge["population_x"])
c_merge = c_merge.sort_values("population_growth", ascending = False).head(10)
c_merge.head(10)
names = ["China", "India", "United States", "Indonesia", "Brazil", "Pakishtan", "Bangladesh", "Nigeria", "Mexico", 'Philipeanes']

population_growth = (c_merge["population_growth"]/10**6)
p.figure(figsize = (15,9))
p.bar(names, population_growth, width=0.6)
p.xlabel("country")
p.ylabel("Population Growth")
p.xticks(rotation = 45)
p.show()