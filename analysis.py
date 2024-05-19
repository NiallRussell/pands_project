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

#Capitalizing index and removing abbreviation for display purposes- https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html
descriptives.index = descriptives.index.str.capitalize()
descriptives.index = descriptives.index.str.replace("Std", "Standard Deviation")

descriptives_by_species.index = descriptives_by_species.index.str.capitalize()

#As species becomes the index when grouping by species, standard deviation is a column name 
#and can't be renamed with string replace: https://stackoverflow.com/questions/19758364/rename-specific-columns-in-pandas
descriptives_by_species = descriptives_by_species.rename(columns = {"std":"Standard Deviation"})

#Rounding to 3 decimal places for readability- https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
descriptives = round(descriptives, 3)

#Write contents of descriptives and species count dataframes to txt file- https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file
with open ("iris_summary.txt", "w") as f:
           f.write("Summary of Descriptives") 
           f.write("\n\n")
           f.write(descriptives.to_string())
           f.write("\n\n")
           f.write ("Species Count")
           f.write("\n\n")
           f.write(species_count.to_string())
           f.write("\n\n")
           f.write("Descriptives by Species")
           f.write("\n\n")
           f.write(descriptives_by_species.to_string())
           

#Converting dataframe columns to numpy arrays for histograms
sepal_length = df["sepal_length"].to_numpy()
sepal_width = df["sepal_width"].to_numpy()
petal_length = df["petal_length"].to_numpy()
petal_width = df["petal_width"].to_numpy()

#Saving histograms to PNG files- https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
#Grouping by species- https://www.geeksforgeeks.org/how-to-fill-color-by-groups-in-histogram-using-matplotlib/
df_upper.pivot(columns='Species', values='Sepal Length').plot.hist(alpha = .5, color = ["lawngreen", "cyan", "lightcoral"], edgecolor = "white")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.savefig('sepal_length.png')
plt.close()

df_upper.pivot(columns='Species', values='Sepal Width').plot.hist(alpha = .5, color = ["lawngreen", "cyan", "lightcoral"], edgecolor = "white")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig('sepal_width.png')
plt.close()

df_upper.pivot(columns='Species', values='Petal Length').plot.hist(alpha = .5, color = ["lawngreen", "cyan", "lightcoral"], edgecolor = "white")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.savefig('petal_length.png')
plt.close()

df_upper.pivot(columns='Species', values='Petal Width').plot.hist(alpha = .5, color = ["lawngreen", "cyan", "lightcoral"], edgecolor = "white")
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

#Correlation matrix- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
corr = df_upper.corr(numeric_only=True)
print(corr)

#One-way ANOVA to determine significant difference in petal length across species- https://www.pythonfordatascience.org/anova-python/
import scipy.stats as stats

#Testing assumption of normal distribution-  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
print(stats.shapiro(df["petal_length"]))

#Testing assumption of homogeneity of variances- https://statistics.laerd.com/spss-tutorials/one-way-anova-using-spss-statistics.php
                                                #https://www.statology.org/levenes-test-python/


#Extracting petal length values of each species- https://sparkbyexamples.com/pandas/pandas-extract-column-value-based-on-another-column
pl_setosa = df.query("species == 'setosa'")["petal_length"]
pl_versicolor = df.query("species == 'versicolor'")["petal_length"]
pl_virginica = df.query("species == 'virginica'")["petal_length"]

#Levene's test
print(stats.levene(pl_setosa, pl_versicolor, pl_virginica))

#Examining variances of each group
print(np.var(pl_setosa), np.var(pl_versicolor), np.var(pl_virginica))

#Kruskal-Wallis test- https://www.statology.org/kruskal-wallis-test-python/
kruskal_petal_length = stats.kruskal(df['petal_length'][df['species'] == 'setosa'],
               df['petal_length'][df['species'] == 'versicolor'],
               df['petal_length'][df['species'] == 'virginica'])

print(kruskal_petal_length)

#Dunn's test for posthoc comparisons - https://www.statology.org/dunns-test-python/
import scikit_posthocs as sp

pl_by_species = [pl_setosa, pl_versicolor, pl_virginica]

print(sp.posthoc_dunn(pl_by_species, p_adjust = 'bonferroni'))