# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:09:10 2024

@author: lakshay
"""

import requests

# Replace this URL with your actual endpoint
url = 'http://127.0.0.1:8000/predict'  # Change '/predict' to your actual endpoint

# Example input data
data = {
    "spending_score": 1,  # Example spending score
    "annual_income": 620,  # Example annual income
    "model_type": "kmeans"  # Change this to the model you want to use
}

# Send a POST request to the API
response = requests.post(url, json=data)

# Print the response
print('Status Code:', response.status_code)
print('Response JSON:', response.json())