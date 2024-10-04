# -*- coding: utf-8 -*-
"""
Spyder Editor

@codeby- Lakshay Chaudhary (github-> https://github.com/lakshay-chaudhary)
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
    clustering_model_type: str  # kmeans, dbscan, gmm

# API route to handle prediction
@app.post("/predict/")
async def predict_cluster(data: CustomerData):
    # Extract data from request
    annual_income = data.annual_income
    spending_score = data.spending_score
    model_of_choice = data.clustering_model_type.lower()  # To handle case sensitivity

    # Combine the features into a single array
    input_data = [[annual_income, spending_score]]

    # Select model based on user input
    if model_of_choice == "dbscan":
        model = models["dbscan"]
        prediction = model.fit_predict(input_data)  # DBSCAN uses fit_predict
        cluster = prediction[0] if len(prediction) > 0 else -1  # Handle case when no cluster is found
    elif model_of_choice == "gmm":
        model = models["gmm"]
        prediction = model.predict(input_data)  # GMM uses predict
        cluster = int(prediction[0])
    elif model_of_choice == "kmeans":
        model = models["kmeans"]
        prediction = model.predict(input_data)  # K-Means uses predict
        cluster = int(prediction[0])
    else:
        return {"error": "Invalid model type. Choose 'kmeans', 'dbscan', or 'gmm'."}

    # Return the predicted cluster
    return {"cluster": int(cluster)}

# Add root endpoint for testing (optional)
@app.get("/")
async def root():
    return {"message": "Welcome to the Customer Segmentation API. Use the /predict/ endpoint to get cluster predictions."}
