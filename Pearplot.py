import matplotlib.pyplot as p
import pandas as pd
import numpy as np
import seaborn as sns
dataSet = pd.read_csv("USA_Housing.csv")
dataSet.head()
print(dataSet.head())
print(dataSet.info())
print(dataSet.columns)
sns.pairplot(dataSet)
p.show()
p.figure(figsize=(10,6))
sns.heatmap(dataSet.corr(), annot = True)
p.show()