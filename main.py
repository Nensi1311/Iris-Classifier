# import libraries
# pandas - working with data set, load data from a CSV file, grouping data by a specific column
import pandas as pd
# working with numeric data, provides efficient operations on arrays of homogeneous data
import numpy as np
# is a library for making statistical graphics in Python
import seaborn as sns
# displaying data and creating static, animated and interactive plots
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# load data set or read from download
df = sns.load_dataset("iris")
df

# print first five rows of the data
df.head()

# print last five of the data
df.tail()

# print true if there is null value in the data
df.isnull()

# print sum of null values
df.isnull().sum()

df.describe()

df.describe(include = "object")

df.info()

df['species'].value_counts()

# EDA
df['sepal_length'].hist()
df['sepal_width'].hist()
df['petal_length'].hist()
df['petal_width'].hist()

colors = ["red", "blue", "green"]
Species = ["setosa", "versicolor", "virginica"]
for i in range(3):
    x = df[df['species'] == Species[i]]
    plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label = Species[i])
plt.xlabel("Sepal Length")    
plt.ylabel("Sepal Width")
plt.show()

for i in range(3):
    x = df[df['species'] == Species[i]]
    plt.scatter(x['petal_length'], x['petal_width'], c = colors[i], label = Species[i])
plt.xlabel("Petal Length")    
plt.ylabel("Petal Width")
plt.show()

for i in range(3):
    x = df[df['species'] == Species[i]]
    plt.scatter(x['sepal_length'], x['petal_length'], c = colors[i], label = Species[i])
plt.xlabel("Sepal Length")    
plt.ylabel("Petal Length")
plt.show()

for i in range(3):
    x = df[df['species'] == Species[i]]
    plt.scatter(x['sepal_width'], x['petal_width'], c = colors[i], label = Species[i])
plt.xlabel("Sepal Width")    
plt.ylabel("Petal Width")
plt.show()

corr = df.corr()
corr
sns.heatmap(corr, cmap="PuRd", annot=True)
