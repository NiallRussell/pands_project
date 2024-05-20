# Analysis of Fisher's Iris Dataset
This dataset contains data on 150 individual flowers. 
Three species are included, each containing 50 flowers. 
Petal length, petal width, sepal length, and sepal width are recorded for each flower

## About this Project
This repository includes the dataset in csv format and a program called analysis.py which:
1. Outputs a summary of each variable to a single text file, 
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables. 
4. Performs a Kruskal-Wallis test to examine differences in petal length across species 

## Use of this Project
This project can be used to obtain an overview of the variables in the Fisher's Iris dataset. 

The .txt file provides a summary of descriptive statistics including mean and standard deviation. It also provides an overview of descriptive statistics across species to allow for comparisons

A histogram of each variable is saved to .png files, which can be viewed to assess the distribution of each variable

Scatter plots help to visualise the association between variable pairs, and a scatter plot is generated for each variable pair

Finally, a Kruskal-Wallis test is presented to examine the difference in petal length across species, and Dunn's test is presented to examine comparisons across each pair of species.

## Guide to Analyses
### *Histograms*
Histograms are presented for each of the four scale variables: petal length, petal width, sepal length and sepal width. The bins are grouped by species to visualise the difference in distributions across species.

Looking at the petal length and petal width histograms, we can see that the distribution of Setosa flowers do not overlap with the other two species, with the values confined to the lower end of the scale. 

The number of bins was set to 40 to allow for a clearer visual of the distribution of each species. Here, we can see that the distribution of petal width in Setosa flowers are positively skewed. Similarly, the distribution of petal length in Versicolor flowers shows a negative skew. 

On the whole, the histograms, with the exeption of sepal width, reveal that the data are not normally distributed. This is important to consider when selecting the appropriate analyses. 

### *Scatterplot*

The scatterplot matrix provides a visualisation of the relationship between each scale variable. Together with the correlation matrix, it shows that sepal width is negatively correlated with sepal length, petal length and petal width; petal length is positively correlated with sepal length and petal width; and petal width is correlated positively with sepal length.

The scatterplot matrix also highlights the values for each species. There are clear clusters visible across species, suggesting a difference in values across species. For example, petal length and sepal length are notably lower for Setosa flowers than other species. 

A positive trend can be seen when examining Versicolor and Virginica data points. Indeed, the correlation coefficient of .82 for this pairing suggests a strong, positive correlation (although the statistical significance is not known as p-values were not computed for the correlations). It is not clear from looking at the scatter plot whether this correlation would be observed in the Setosa species alone. This project provides a good starting point for researchers looking to further examine the associations between measures across species.

### *Kruskal-Wallis Test*
A one way ANOVA to examine differences in petal length across species was intended, and the assumptions of normal distribution and homogeneity of variances were tested- https://statistics.laerd.com/spss-tutorials/one-way-anova-using-spss-statistics.php

As the p-value of the Shapiro-Wilk test is below .05, the assumption of normal distribution is violated 

As the p-value of Levene's test is below .05, the assumption of homogeneity of variances is violated

The variances of each of the three petal length samples were examined and as the largest variances is more than 4 times the smallest variance, a Kruskal-Wallis test was performed instead of a one way ANOVA- https://www.statology.org/brown-forsythe-test-in-python/

As the p-value of the Kruskal-Wallis statistic is less than .05, the null hypothesis that median petal length is the same for all three species is rejected- https://www.statology.org/kruskal-wallis-test-python/

Dunn's test was performed for post-hoc comparisons- https://www.statology.org/dunns-test-python/
As the adjusted p-value for each pair of comparisons is below .05, there is a significant difference in petal length across the three species.

Examining the petal length means across species in the .txt file, we can conclude that Setosa flowers have, on average, siginficantly shorter petals than Versicolor and Virginica flowers; Versicolor flowers have significantly longer petals than Setosa plants and significantly shorter petals than Virginica flowers; and Virginica flowers have significantly longr petals than both Versicolor and Setosa flowers.

## Output
When the programme is run, the following occurs:
1. A txt file is created containing a summary of descriptive statistics
2. Histograms are created for each of the four scale variables, grouped by species, and saved to .png files
3. A scatterplot matrix of relationships between the four scale variables is presented, grouped by species
4. A corelation matrix is presented to show the strength of relationships across the four scale variables
5. The Shapiro-Wilk statistic and corresponding p-value is presented for petal length
6. The Levene test statistic and corresponding p-value is presented for petal length, grouped by species
7. For each sample of petal length values (grouped by species), the variance is presented
8. The Kruskal-Wallis statistic and corresponding p-value is presented for petal length and species
9. The results of Dunn's test is presented showing the adjusted p-values for each pair of comparisons between species on petal length

## Getting Help
Please contact the author at g00439452@atu.ie

## Contribute
To contribute to this project, please contact the author at g00439452@atu.ie

## Author
Niall Russell
