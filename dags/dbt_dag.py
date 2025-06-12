from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='dbt_workflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['dbt']
) as dag:

    dbt_debug = BashOperator(
        task_id='dbt_debug',
        bash_command='cd /usr/app && dbt debug',
    )

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd /usr/app && dbt deps && dbt seed',
        dag=dag,
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /usr/app && dbt run',
    )

    dbt_docs = BashOperator(
        task_id='dbt_docs_generate',
        bash_command='cd /usr/app && dbt docs generate',
    )

    dbt_debug >> dbt_seed >> dbt_run >> dbt_docs