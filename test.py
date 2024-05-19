#Import pandas for data manipulation using dataframes
import pandas as pd

#Import matplotlib.pyplot to generate plots
import matplotlib.pyplot as plt

#Import numpy to create arrays from pandas dataframe
import numpy as np

#Read in dataset
df = pd.read_csv("iris.csv")

df_setosa = df.query("species == 'setosa'")["petal_length"]
df_versicolor = df.query("species == 'versicolor'")["petal_length"]
df_verginica = df.query("species == 'versicolor'")["petal_length"]
print(df_setosa)

import scipy.stats as stats

#Testing assumption of normal distribution-  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
#print(stats.shapiro(df["petal_length"]))

df_setosa = df.query("species == 'setosa'")["petal_length"]
df_versicolor = df.query("species == 'versicolor'")["petal_length"]
df_verginica = df.query("species == 'versicolor'")["petal_length"]

#Levene's test
print(stats.levene(df_setosa, df_versicolor, df_verginica))

print(np.var(df_setosa), np.var(df_versicolor), np.var(df_verginica))

#Kruskal-Wallis test- https://www.statology.org/kruskal-wallis-test-python/
kruskal_petal_length = stats.kruskal(df['petal_length'][df['species'] == 'setosa'],
               df['petal_length'][df['species'] == 'versicolor'],
               df['petal_length'][df['species'] == 'virginica'])
print (kruskal_petal_length)