from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = df.drop(columns=["species"])
Y = df["species"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.30)

model = LogisticRegression()
model.fit(x_train, y_train)
print("Logistic Regression Accuracy is : ", model.score(x_test, y_test)*100)

model1.fit(x_train.values, y_train.values)
