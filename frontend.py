import streamlit as st
import requests

# Set up page configuration for a sleek look
st.set_page_config(
    page_title="Customer Segmentation Tool",
    layout="centered",
    initial_sidebar_state="auto",
)

# Apply background color (black) and text styles
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stButton button {
        background-color: #0073e6;
        color: white;
    }
    .stTextInput > div > div > input {
        color: white;
    }
    .stNumberInput > div > div > input {
        color: white;
    }
    .stSelectbox > div > div > div {
        color: white;
    }
    .stFileUploader {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app with custom styling
st.markdown("<h1 style='text-align: center; color: #0073e6;'>Customer Segmentation Tool</h1>", unsafe_allow_html=True)

# Comprehensive section explaining what each cluster represents
st.markdown(""" 
## What Do Clusters Represent?
- **Cluster 1**: High Spenders – Customers who frequently buy high-value products.
- **Cluster 2**: Moderate Spenders – Customers with balanced spending habits.
- **Cluster 3**: Low Spenders – Customers who spend minimally on products.
- **Cluster 4**: Brand Loyalists – Customers who repeatedly buy from specific brands.
- **Cluster 5**: Occasional Buyers – Customers who purchase sporadically.

Use this tool to segment customers and tailor marketing strategies based on their spending patterns.
""")

# Sidebar with an image and GitHub link
st.sidebar.image("https://media.licdn.com/dms/image/C4D12AQEQSgGXtud3dA/article-cover_image-shrink_600_2000/0/1588440796258?e=2147483647&v=beta&t=0SORV_gIMlAEmaTdqPJG_UgY3PyN0TTMBOXnfmTKgJI", width=500)  
st.sidebar.markdown(
    """
    ### Wanna know how it works?
    [Go to the link provided](https://github.com/lakshay-chaudhary/my_fast_api)  
    You can view the code, explore the models used, and moreover you can contribute to fine-tuning parameters :)
    """,
    unsafe_allow_html=True
)

# Create input fields for the user to enter details
st.header("Enter Customer Details")

# Option 1: Single customer input
st.subheader("Single Customer Input")
customer_id = st.text_input("Customer ID")
customer_name = st.text_input("Customer Name")
age = st.slider("Age", 18, 100, 25)  # Optional input
gender = st.selectbox("Gender", ("Male", "Female", "Other"))  # Optional input

# Annual Income and Spending Score (will be used in the backend)
annual_income = st.number_input("Annual Income", min_value=0.0, step=1000.0)
spending_score = st.number_input("Spending Score (1-100)", min_value=0.0, max_value=100.0)

# Model selection
clustering_model_type = st.selectbox("Select Clustering Algorithm", ["KMeans", "DBSCAN", "GMM"])

# Submit button
if st.button("Segment Customer"):
    # Create a dictionary of the input data
    customer_data = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "age": age,
        "gender": gender,
        "annual_income": annual_income,
        "spending_score": spending_score,
        "clustering_model_type": clustering_model_type.lower()
    }
    
    # Make a POST request to the FastAPI backend
    try:
        response = requests.post("https://my-fast-api-2.onrender.com/predict/", json=customer_data)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Display the predicted cluster
        result = response.json()
        st.success(f"Customer {customer_name} (ID: {customer_id}) is in Cluster {result['cluster']}")
    
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except Exception as err:
        st.error(f"An error occurred: {err}")  # Handle other errors

# Option 2: CSV Upload (for show)
st.subheader("Upload Customer Data via CSV (For Show)")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, show an error message (since we are not handling CSV processing yet)
if uploaded_file is not None:
    st.error("Error occurred while uploading the file. Please refer to single customer detail input only.")
