from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="simple_bash_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello World'",
    )