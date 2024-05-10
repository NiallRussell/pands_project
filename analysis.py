#Import pandas for data manipulation using dataframes
import pandas as pd

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