#Import pandas for data manipulation using dataframes
import pandas as pd

#Import matplotlib.pyplot to generate plots
import matplotlib.pyplot as plt

#Import numpy to create arrays from pandas dataframe
import numpy as np

#Read in dataset
df = pd.read_csv("iris.csv")

df_upper = df.rename(columns={"sepal_length": "Sepal Length", "sepal_width": "Sepal Width", "petal_length": "Petal Length", "petal_width": "Petal Width", "species": "Species"})

#Frequencies for categorical variables
species_count = df_upper["Species"].value_counts()
species_count.index = species_count.index.str.capitalize()

#Descriptives for scale variables 
descriptives = df_upper.describe()
descriptives.index = descriptives.index.str.capitalize()
descriptives.index = descriptives.index.str.replace("Std", "Standard Deviation")

#Write contents of descriptives and species count dataframes to txt file- https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file
with open ("iris_summary.txt", "w") as f:
           f.write(descriptives.to_string())
           f.write("\n\n")
           f.write(species_count.to_string())
