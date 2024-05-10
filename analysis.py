#Import pandas for data manipulation using dataframes
import pandas as pd

#Import matplotlib.pyplot to generate plots
import matplotlib.pyplot as plt

#Import numpy to create arrays from pandas dataframe
import numpy as np

#Read in dataset
df = pd.read_csv("iris.csv")

#Frequencies for categorical variables
species_count = df["species"].value_counts()

#Descriptives for scale variables 
descriptives = df.describe()

#Write contents of descriptives and species count dataframes to txt file- https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file
with open ("iris_summary.txt", "a") as f:
           f.write(descriptives.to_string())
           f.write("\n")
           f.write(species_count.to_string())


sepal_length = df["sepal_length"].to_numpy()
sepal_width = df["sepal_width"].to_numpy()
petal_length = df["petal_length"].to_numpy()
petal_width = df["petal_width"].to_numpy()

plt.hist(sepal_length)
plt.savefig('sepal_length.png')
plt.close()
plt.hist(sepal_width)
plt.savefig('sepal_width.png')
plt.close()
plt.hist(petal_length)
plt.savefig('petal_length.png')
plt.close()
plt.hist(petal_width)
plt.savefig('petal_width.png')
plt.close()
#https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
