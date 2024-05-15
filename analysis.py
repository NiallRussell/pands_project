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
with open ("iris_summary.txt", "w") as f:
           f.write(descriptives.to_string())
           f.write("\n")
           f.write(species_count.to_string())

#Converting dataframe columns to numpy arrays for histograms
sepal_length = df["sepal_length"].to_numpy()
sepal_width = df["sepal_width"].to_numpy()
petal_length = df["petal_length"].to_numpy()
petal_width = df["petal_width"].to_numpy()

#Saving histograms to PNG files- https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
plt.hist(sepal_length)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.savefig('sepal_length.png')
plt.close()

plt.hist(sepal_width)
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig('sepal_width.png')
plt.close()

plt.hist(petal_length)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.savefig('petal_length.png')
plt.close()

plt.hist(petal_width)
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.savefig('petal_width.png')
plt.close()

#Import plotly.express to allow for scatterplot matrix- https://plotly.com/python/plotly-express/
import plotly.express as px

#Workaround for px plot not working with Pandas 2.0- https://community.plotly.com/t/scatter-matrix-with-plotly-express-does-not-work-with-pandas-2-0/77695
pd.DataFrame.iteritems = pd.DataFrame.items


fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
fig.show()

