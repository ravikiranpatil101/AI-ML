import streamlit as st
from model import predict_flower

st.title("Iris Flower Predictor")

st.write("Enter flower measurements below:")

sepal_length = st.number_input("Sepal Length", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width", 0.0, 10.0, 0.2)

if st.button("Predict"):

    result = predict_flower(
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    )

    st.success(f"Predicted Flower: {result}")