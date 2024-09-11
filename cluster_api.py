# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Create FastAPI instance
app = FastAPI()

# Load the dictionary of pre-trained models
models = pickle.load(open("models_dict.sav", "rb"))

# Define a Pydantic model for input validation
class CustomerData(BaseModel):
    annual_income: float
    spending_score: float
    model_type: str  # kmeans, dbscan, gmm

# API route to handle prediction
@app.post("/predict/")
def predict_cluster(data: CustomerData):
    # Extract data from request
    annual_income = data.annual_income
    spending_score = data.spending_score
    model_of_Choice = data.model_type.lower()  # To handle case sensitivity

    # Combine the features into a single array
    input_data = [[annual_income, spending_score]]

    # Select model based on user input
    if model_of_Choice == "dbscan":
        model = models["dbscan"]
        prediction = model.fit_predict(input_data)  # DBSCAN uses fit_predict
    elif model_of_Choice == "gmm":
        model = models["gmm"]
        prediction = model.predict(input_data)  # GMM uses predict
    elif model_of_Choice == "kmeans":
        model = models["kmeans"]
        prediction = model.predict(input_data)  # K-Means uses predict
    else:
        return {"error": "Invalid model type. Choose 'kmeans', 'dbscan', or 'gmm'."}

    # Return the predicted cluster
    return {"cluster": int(prediction[0])}
