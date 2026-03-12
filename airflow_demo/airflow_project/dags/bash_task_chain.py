from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="bash_task_chain",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task_a = BashOperator(
        task_id="task_a",
        bash_command="echo 'Task A completed'",
    )

    task_b = BashOperator(
        task_id="task_b",
        bash_command="echo 'Task B running'",
    )

    task_c = BashOperator(
        task_id="task_c",
        bash_command="echo 'Task C running'",
    )

    # Task A triggers B and C
    task_a >> [task_b, task_c]