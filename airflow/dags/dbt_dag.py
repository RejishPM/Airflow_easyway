from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),}

with DAG(
       dag_id='dbt_dag',
       default_args=default_args,
       schedule_interval='@daily',
         start_date=datetime(2023, 1, 1),
         catchup=False,
         tags=['dbt'],
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt && dbt run',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt/ && dbt test',
    )

    dbt_run >> dbt_test