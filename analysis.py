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

#Capitalizing index and removing abbreviation for display purposes- https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html
descriptives.index = descriptives.index.str.capitalize()
descriptives.index = descriptives.index.str.replace("Std", "Standard Deviation")

#Rounding to 3 decimal places for readability- https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
descriptives = round(descriptives, 3)

#Write contents of descriptives and species count dataframes to txt file- https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file
with open ("iris_summary.txt", "w") as f:
           f.write(descriptives.to_string())
           f.write("\n\n")
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

fig = px.scatter_matrix(df_upper, 
                        dimensions=["Sepal Width", "Sepal Length", "Petal Width", "Petal Length"], 
                        color="Species")
fig.show()

#One-way ANOVA to determine significant difference in petal length across species- https://www.pythonfordatascience.org/anova-python/
import scipy.stats as stats

#Testing assumption of normal distribution-  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
print(stats.shapiro(df["petal_length"]))

#Testing assumption of homogeneity of variances-
#pl_setosa = np.array(df[df["petal_length"])
#pl_versicolor =
#pl_verginica = 

one_way = stats.f_oneway(df['petal_length'][df['species'] == 'setosa'],
               df['petal_length'][df['species'] == 'versicolor'],
               df['petal_length'][df['species'] == 'virginica'])

print(one_way)