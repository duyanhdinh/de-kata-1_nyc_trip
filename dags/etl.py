from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from libs.etl_yellow_trip.clean import yellow_trip_clean
from libs.etl_yellow_trip.load import yellow_trip_load
from libs.etl_yellow_trip.create_table import yellow_trip_create_table
from libs.etl_yellow_trip.transform import yellow_trip_transform
from libs.etl_yellow_trip.ingest import yellow_trip_ingest

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

    ingest = PythonOperator(
        task_id='extract',
        python_callable=yellow_trip_ingest
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=yellow_trip_transform
    )

    create_table = PythonOperator(
        task_id='create_table',
        python_callable=yellow_trip_create_table
    )

    load = PythonOperator(
        task_id='load',
        python_callable=yellow_trip_load
    )

    clean = PythonOperator(
        task_id='clean',
        python_callable=yellow_trip_clean
    )

    ingest >> transform >> create_table >> load >> clean
