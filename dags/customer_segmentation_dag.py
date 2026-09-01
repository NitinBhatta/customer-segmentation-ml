from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import pickle


DATA_PATH = "/home/nbhatta/customer_segmentation/data/ecommerce_user_segmentation.csv"
MODEL_PATH = "/home/nbhatta/customer_segmentation/models/customer_segment_model.pkl"


def load_data():
    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)
    print("Dataset loaded successfully!")


def validate_data():
    df = pd.read_csv(DATA_PATH)

    print("Missing values:", df.isnull().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())

    print("Data validation completed!")


def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    print("Model loaded successfully!")
    print("Model type:", type(model).__name__)


with DAG(
    dag_id="customer_segmentation_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task_load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    task_validate_data = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    task_load_model = PythonOperator(
        task_id="load_model",
        python_callable=load_model,
    )

    task_load_data >> task_validate_data >> task_load_model

