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
  
