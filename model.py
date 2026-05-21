import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Prediction function
def predict_flower(sepal_length, sepal_width, petal_length, petal_width):

    data = np.array([
        [sepal_length, sepal_width, petal_length, petal_width]
    ])

    prediction = model.predict(data)[0]

    species = ["Setosa", "Versicolor", "Virginica"]

    return species[prediction]