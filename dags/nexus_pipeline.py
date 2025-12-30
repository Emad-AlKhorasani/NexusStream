from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='nexus_pipeline_v1',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    process_data = BashOperator(
        task_id='spark_process_task',
        bash_command='echo "Running Spark Task..." && sleep 5 && echo "Success!"'
    )