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
