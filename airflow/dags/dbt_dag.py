from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import mlflow


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),}

def log_dbt_to_mlflow(**context):
    mlflow.set_tracking_uri("http://mlflow:5000")
    
    with mlflow.start_run(run_name="dbt_run_tracking"):
        mlflow.set_tag("project", "dbt_project")
        mlflow.set_tag("dag_id", context['dag'].dag_id)
        mlflow.set_tag("task_id", context['task'].task_id)
        mlflow.log_param("run_type", "dbt_run")
        mlflow.log_metric("status_code", 0)
        mlflow.log_artifacts("/opt/airflow/dbt/target", artifact_path="dbt_output")
        

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

    log_dbt_to_mlflow = PythonOperator(
        task_id='log_dbt_to_mlflow',
        python_callable=log_dbt_to_mlflow,
    )

    dbt_run >> log_dbt_to_mlflow >> dbt_test