import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd
import statistics as st

data = pd.read_csv("Titanic Dataset.csv")
print(data.head())
print(data.info())
print(data.dtypes)
mean_age = np.mean(data['Age'])
print(f"Mean age of passenger is {mean_age}")
mean_faire = np.mean(data['Fare'])
print(f"Mean of fare is {mean_faire}")

median_age = np.median(data['Age'])
print(f"Median age of passenger is {median_age}")
median_faire = np.median(data['Fare'])
print(f"Median of fare is {median_faire}")

mode_age = st.mode(data['Age'])
print(f"Mode of Age is {mode_age}")
mode_Pclass = st.mode(data['Pclass'])
print(f"Mode of pClass is {mode_Pclass}")
mode_gender = data["Gender"].value_counts().index[0]
print(f"Mode of gender is {mode_gender}")