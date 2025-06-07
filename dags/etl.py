from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from libs.etl.transform.yellow_trip import transform_yellow_trip
from libs.ingest.yellow_trip import ingest_yellow_trip

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='extract',
        python_callable=ingest_yellow_trip
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_yellow_trip
    )

    t1 >> t2   # Define task dependency
