# Customer Clustering API

This project is a FastAPI application that provides an API for customer clustering using different machine learning algorithms, including K-Means, DBSCAN, and Gaussian Mixture Models (GMM). The API allows users to submit customer data and receive clustering results based on the selected model.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Contributing](#contributing)

## Features

- Clustering of customer data using K-Means, DBSCAN, and GMM.
- RESTful API built with FastAPI.
- User-friendly input format for customer data.
- Dynamic model selection based on user input.
- Easy deployment and scalability.

## Technologies Used

- **FastAPI**: The web framework used to create the API.
- **Scikit-learn**: Library for machine learning algorithms.
- **Pickle**: For model serialization and deserialization.
- **Pydantic**: For data validation and settings management.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **Python 3.8+**: Programming language used for development.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Fast_api_clustering_customers.git
   cd Fast_api_clustering_customers/data
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Ensure you have the model files (models_dict.sav) in the correct directory.

## Usage

To run the API, navigate to the directory containing your FastAPI application and run:
  ```bash
  uvicorn cluster_api:app --reload
```
The API will be available at http://127.0.0.1:8000.


## API Endpoints

  POST /cluster
  Description: Clusters customer data based on the selected model.
  Request Body:
  
  ```bash
{
  "model_of_choice": "KMeans",  // Options: "KMeans", "DBSCAN", "GMM"
  "data": [
    {
      "customer_id": 1,
      "age": 25,
      "gender": "Male",
      "annual_income": 50000,
      "spending_score": 70
    },
    ...
  ]
}
```
response 
```bash
{
  "clusters": [
    {
      "customer_id": 1,
      "cluster_label": 0
    },
    ...
  ]
}
```

## Models

The following clustering models are implemented in this project:

K-Means: Partitions customers into K distinct clusters based on their features.
DBSCAN: Groups together points that are closely packed together while marking as outliers points that lie alone in low-density regions.
Gaussian Mixture Models (GMM): A probabilistic model that assumes all data points are generated from a mixture of several Gaussian distributions.

Known Issues
The clustering models (GMM and DBSCAN) require fine-tuning as there are accuracy issues.
Users may encounter version warnings related to the pickled model files if using different versions of scikit-learn.

**Each cluster has meaning to it and it follows as 
Cluster 1 (High Spenders): This group includes customers who have a high annual income and spending score. They are likely to be frequent purchasers and respond well to premium products or services.

Cluster 2 (Moderate Spenders): Customers in this cluster have a moderate spending score and income. They may be occasional buyers and are potential targets for promotions and loyalty programs to increase their spending.

Cluster 3 (Low Spenders): This group consists of customers with low spending scores and possibly lower incomes. They might be more price-sensitive and could benefit from discount offers or budget-friendly product suggestions.

Cluster 4 (Brand Loyalists): Customers in this cluster may have lower spending scores but exhibit strong brand loyalty, consistently purchasing certain brands. Engaging this group with personalized marketing strategies can enhance retention.

Cluster 5 (Occasional Buyers): This group may show sporadic purchasing behavior with varied spending scores. Targeting them with targeted marketing campaigns could help convert them into more frequent buyers.

## Contributing

Contributions from the community is welcomed, If you'd like to contribute, please check out that files are available in 2 different branches : main branch contains main ML model files(google colab) where as branch named API contains sav file , api file and testing file with requirments.txt for downloading required libraries .  

