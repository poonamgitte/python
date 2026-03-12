from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def task_a():
    print("Task A completed")

def task_b():
    print("Task B running")

def task_c():
    print("Task C running")

with DAG(
    dag_id="python_task_chain",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="task_a",
        python_callable=task_a,
    )

    t2 = PythonOperator(
        task_id="task_b",
        python_callable=task_b,
    )

    t3 = PythonOperator(
        task_id="task_c",
        python_callable=task_c,
    )

    # Task A triggers B and C
    t1 >> [t2, t3]