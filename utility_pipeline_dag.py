from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def validate_raw_data():
    print("Validating raw input files")


def load_bronze_layer():
    print("Loading Bronze layer")


def transform_silver_layer():
    print("Transforming Silver layer")


def publish_gold_layer():
    print("Publishing Gold layer")


def generate_kpis():
    print("Generating KPI outputs")


with DAG(
    dag_id="utility_data_pipeline_orchestration",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "owner": "ashok",
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    },
    description="Enterprise utility pipeline orchestration DAG"
) as dag:

    validate_task = PythonOperator(
        task_id="validate_raw_data",
        python_callable=validate_raw_data
    )

    bronze_task = PythonOperator(
        task_id="load_bronze_layer",
        python_callable=load_bronze_layer
    )

    silver_task = PythonOperator(
        task_id="transform_silver_layer",
        python_callable=transform_silver_layer
    )

    gold_task = PythonOperator(
        task_id="publish_gold_layer",
        python_callable=publish_gold_layer
    )

    kpi_task = PythonOperator(
        task_id="generate_kpis",
        python_callable=generate_kpis
    )

    validate_task >> bronze_task >> silver_task >> gold_task >> kpi_task
