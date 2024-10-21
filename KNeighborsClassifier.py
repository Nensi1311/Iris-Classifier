from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(x_train, y_train)
print("K-nearest neighbors Accuracy is :", model.score(x_test, y_test)*100)

model.fit(x_train.values, y_train.values)
