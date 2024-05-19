# Analysis of Fisher's Iris Dataset
This dataset contains data on 150 individual flowers. 
Three species are included, each containing 50 flowers. 
Petal length, petal width, sepal length, and sepal width are recorded for each flower

## About this Project
This repository includes the dataset in csv format and a program called analysis.py which:
1. Outputs a summary of each variable to a single text file, 
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables. 
4. Performs any other analysis you think is appropriate. (INCLUDE ANALYSIS HERE)

## Use of this Project
This project can be used to obtain an overview of the variables in the Fisher's Iris dataset. 

A histogram of each variable is saved to png files, which can be viewed to assess the distribution of each variable

Scatter plots help to visualise the association between variable pairs, and a scatter plot is generated for each variable pair

OTHER ANALYSIS

Assumptions- https://statistics.laerd.com/spss-tutorials/one-way-anova-using-spss-statistics.php

As the p-value of the Shapiro-Wilk test is below .05, the assumption of normal distribution is violated 

As the p-value of Levene's test is below .05 the assumption of homogeneity of variances is violated
The variances of each of the three petal length samples were examined and as the largest variances is more than 4 times the smallest variance, a Kruskal-Wallis test was performed instead of a one way ANOVA- https://www.statology.org/brown-forsythe-test-in-python/

As the p-value of the Kruskal-Wallis statistic is less than .05, the null hypothesis that median petal length is the same for all three species- https://www.statology.org/kruskal-wallis-test-python/

Dunn's test was performed for post-hoc comparisons- https://www.statology.org/dunns-test-python/
As the p-value for each pair of comparisons was below .05, there is a significant difference in petal length across the three species 

## Getting Started

## Getting Help
Please contact the author at g00439452@atu.ie

## Contribute
## Author
Niall Russell
