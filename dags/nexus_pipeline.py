from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG and its core properties
with DAG(
    dag_id='nexus_pipeline_v1',
    start_date=datetime(2023, 1, 1),
   schedule_interval=None,  # Triggered manually
    catchup=False            # Do not run missed past tasks
) as dag:

     # Task 1: Simulate data processing using Spark
    # We use BashOperator to execute system commands directly inside the container
    process_data = BashOperator(
        task_id='spark_process_task',
        bash_command='echo "Starting Spark Job..." && sleep 5 && echo "Data Transformation Completed Successfully!"'

    )
