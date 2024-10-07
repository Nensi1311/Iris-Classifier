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
