# Customer Segmentation ML Project

## Project Overview

This project develops an end-to-end machine learning solution for customer segmentation using e-commerce customer behavior data.

The project includes exploratory data analysis, machine learning model development, Airflow pipeline orchestration, and Streamlit deployment.

## Dataset

The dataset contains 10,000 customer records and 14 columns.

The target variable is:

`Segment_Label`

The customer segments are:

* Iron
* Copper
* Silver
* Gold
* Platinum

## Features Used for Machine Learning

The following 12 features were used:

* Recency
* Frequency
* Monetary
* Avg_Order_Value
* Session_Count
* Avg_Session_Duration
* Pages_Viewed
* Clicks
* Campaign_Response
* Wishlist_Adds
* Cart_Abandon_Rate
* Returns

`Customer_ID` was excluded from the model.

## Exploratory Data Analysis

EDA was performed to understand customer behavior and differences between customer segments.

The analysis examined:

* Segment distribution
* Customer purchasing behavior
* Customer engagement
* Session activity
* Pages viewed
* Clicks
* Campaign response
* Wishlist activity
* Cart abandonment
* Returns

The analysis showed clear differences between customer segments. Platinum customers generally demonstrated higher purchasing and engagement activity, while Iron customers showed lower engagement.

## Machine Learning

Two classification models were trained and evaluated:

| Model               | Accuracy |
| ------------------- | -------: |
| Random Forest       |   1.0000 |
| Logistic Regression |   0.9995 |

Random Forest was selected as the final model because it achieved the highest accuracy.

The trained model is saved as:

`models/customer_segment_model.pkl`

## Airflow Pipeline

Apache Airflow is used to orchestrate the project workflow.

The Airflow DAG is:

`customer_segmentation_pipeline`

The pipeline performs the following tasks:

```text
Load Data
    ↓
Validate Data
    ↓
Load Trained Model
```

The DAG was successfully tested using Apache Airflow.

## Streamlit Application

A Streamlit web application was developed to allow users to enter customer information and receive a predicted customer segment.

The application loads the trained Random Forest model and predicts one of the following segments:

* Iron
* Copper
* Silver
* Gold
* Platinum

## Project Structure

```text
customer_segmentation/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── ecommerce_user_segmentation.csv
│
├── models/
│   └── customer_segment_model.pkl
│
├── notebooks/
│   └── Untitled.ipynb
│
└── dags/
    └── customer_segmentation_dag.py
```

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run Streamlit

From the project directory:

```bash
python -m streamlit run app.py
```

Then open the local URL displayed by Streamlit.

## Airflow

The Airflow DAG is located in:

```text
dags/customer_segmentation_dag.py
```

The DAG can be triggered using the Airflow interface.

## Conclusion

This project demonstrates an end-to-end machine learning workflow, starting with customer data analysis and model development and continuing through Airflow orchestration and Streamlit deployment.
