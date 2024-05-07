import pandas as pd
df = pd.read_csv("iris.csv")
print(df)
print(df.describe())
species_count = df["species"].value_counts()
print(species_count)
descriptives = df.describe()

print(descriptives)
with open ("iris_summary.txt", "a") as f:
           f.write(descriptives.to_string())
           f.write("\n")
           f.write(species_count.to_string())