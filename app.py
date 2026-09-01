import streamlit as st
import pandas as pd
import pickle

# Load trained model
MODEL_PATH = "models/customer_segment_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Page title
st.title("Customer Segmentation Prediction")
st.write("Enter customer information to predict the customer segment.")

# Input fields
recency = st.number_input("Recency", min_value=0.0, value=30.0)
frequency = st.number_input("Frequency", min_value=0.0, value=10.0)
monetary = st.number_input("Monetary", min_value=0.0, value=500.0)
avg_order_value = st.number_input(
    "Average Order Value", min_value=0.0, value=50.0
)

session_count = st.number_input("Session Count", min_value=0.0, value=10.0)
avg_session_duration = st.number_input(
    "Average Session Duration", min_value=0.0, value=10.0
)
pages_viewed = st.number_input("Pages Viewed", min_value=0.0, value=20.0)
clicks = st.number_input("Clicks", min_value=0.0, value=500.0)

campaign_response = st.number_input(
    "Campaign Response", min_value=0.0, max_value=1.0, value=0.5
)

wishlist_adds = st.number_input("Wishlist Adds", min_value=0.0, value=10.0)

cart_abandon_rate = st.number_input(
    "Cart Abandon Rate", min_value=0.0, max_value=100.0, value=20.0
)

returns = st.number_input("Returns", min_value=0.0, value=5.0)

# Prediction
if st.button("Predict Customer Segment"):

    input_data = pd.DataFrame([[
        recency,
        frequency,
        monetary,
        avg_order_value,
        session_count,
        avg_session_duration,
        pages_viewed,
        clicks,
        campaign_response,
        wishlist_adds,
        cart_abandon_rate,
        returns
    ]], columns=[
        "Recency",
        "Frequency",
        "Monetary",
        "Avg_Order_Value",
        "Session_Count",
        "Avg_Session_Duration",
        "Pages_Viewed",
        "Clicks",
        "Campaign_Response",
        "Wishlist_Adds",
        "Cart_Abandon_Rate",
        "Returns"
    ])

    prediction = model.predict(input_data)

    st.success(f"Predicted Customer Segment: {prediction[0]}")
