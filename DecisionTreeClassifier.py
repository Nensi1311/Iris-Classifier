from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print("Decision Tree Accuracy is :", model.score(x_test, y_test)*100)

model.fit(x_train.values, y_train.values)
