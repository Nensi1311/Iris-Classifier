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

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

X = df.drop(columns=["species"])
Y = df["species"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.30)

model = LogisticRegression()
model.fit(x_train, y_train)
print("Logistic Regression Accuracy is : ", model.score(x_test, y_test)*100)
model1.fit(x_train.values, y_train.values)

model = KNeighborsClassifier()
model.fit(x_train, y_train)
print("K-nearest neighbors Accuracy is :", model.score(x_test, y_test)*100)
model.fit(x_train.values, y_train.values)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print("Decision Tree Accuracy is :", model.score(x_test, y_test)*100)
model.fit(x_train.values, y_train.values)

import pickle
filename = "iris"
pickle.dump(model, open(filename, "wb"))
filename = "iris"
try:
    with open(filename, "wb") as file:
        pickle.dump(model, file)
    print("Model Saved Successfully!")
except Exception as e:
    print(f"Can't Save the model : {e}")

load_model = pickle.load(open(filename, "rb"))
SL = float(input("Enter Sepal Length :"))
SL
SW = float(input("Enter Sepal Width :"))
SW
PL = float(input("Enter Petal Length :"))
PL
PW = float(input("Enter Petal Width :"))
PW
print("Iris flower Species is : ",load_model.predict([[SL, SW, PL, PW]]))
