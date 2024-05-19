#Import pandas for data manipulation using dataframes
import pandas as pd

#Import matplotlib.pyplot to generate plots
import matplotlib.pyplot as plt

#Import numpy to create arrays from pandas dataframe
import numpy as np

#Read in dataset
df = pd.read_csv("iris.csv")

#Changing column names for readability when displaying stats- https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas 
df_upper = df.rename(columns={"sepal_length": "Sepal Length", "sepal_width": "Sepal Width", "petal_length": "Petal Length", "petal_width": "Petal Width", "species": "Species"})

# Capitalising values for Species for display purposes- https://www.geeksforgeeks.org/string-capitalize-python/
df_upper["Species"] = df_upper["Species"].str.capitalize()

#Frequencies for categorical variables
species_count = df_upper["Species"].value_counts()

#Capitalizing the index for diplay purposes- applied capitalize method similar to index manipulation here: https://stackoverflow.com/questions/30576323/pandas-convert-index-values-to-lowercase
species_count.index = species_count.index.str.capitalize()

#Descriptives for scale variables 
descriptives = df_upper.describe()
descriptives_by_species = df_upper.groupby("Species").describe()
print(descriptives_by_species)