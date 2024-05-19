#Import pandas for data manipulation using dataframes
import pandas as pd

#Import matplotlib.pyplot to generate plots
import matplotlib.pyplot as plt

#Import numpy to create arrays from pandas dataframe
import numpy as np

#Read in dataset
df = pd.read_csv("iris.csv")

df.pivot(columns='species', values='petal_length').plot.hist()
plt.show()