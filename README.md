# Customer Segmentation ML Project

## Overview

This project uses machine learning to predict e-commerce customer segments based on customer behavior.

The five segments are:

- Iron
- Copper
- Silver
- Gold
- Platinum

## Dataset

The dataset contains 10,000 customer records and 14 columns.

The target variable is `Segment_Label`.

Customer_ID was not used for model training.

## Machine Learning

I trained two classification models:

| Model | Accuracy |
|---|---:|
| Random Forest | 1.0000 |
| Logistic Regression | 0.9995 |

Random Forest was selected as the final model.

The trained model is saved in:

`models/customer_segment_model.pkl`

## Airflow

Apache Airflow was used to create a pipeline for the project.

The pipeline contains:

Load Data → Validate Data → Load Model

DAG name:

`customer_segmentation_pipeline`

## Streamlit

A Streamlit application was created to allow users to enter customer information and get a predicted customer segment.

The application uses the saved Random Forest model.

## Project Structure

customer_segmentation/

├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── ecommerce_user_segmentation.csv
├── models/
│   └── customer_segment_model.pkl
├── notebooks/
│   └── Untitled.ipynb
└── dags/
    └── customer_segmentation_dag.py

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

python -m streamlit run app.py
