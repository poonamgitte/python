from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Default arguments including retries
default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

# Task 1 - Generate a number
def generate_number(ti):
    number = 10
    print("Generated number:", number)

    # Push value to XCom
    # or we can skip to push value to XCom it will automatically pushed to xCom when we return value 
    ti.xcom_push(key="num", value=number)
    

# Task 2 - Multiply number
def multiply_number(ti):
    # Pull value from XCom
    number = ti.xcom_pull(task_ids="generate_number", key="num")

    result = number * 5
    print("After multiplication:", result)

    ti.xcom_push(key="result", value=result)

# Task 3 - Print result
def print_result(ti):
    result = ti.xcom_pull(task_ids="multiply_number", key="result")
    print("Final result:", result)

# DAG definition
with DAG(
    dag_id="schedule_retry_xcom_demo",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",   # DAG runs every day
    catchup=False,
    default_args=default_args
) as dag:

    task1 = PythonOperator(
        task_id="generate_number",
        python_callable=generate_number
    )

    task2 = PythonOperator(
        task_id="multiply_number",
        python_callable=multiply_number
    )

    task3 = PythonOperator(
        task_id="print_result",
        python_callable=print_result
    )

    task1 >> task2 >> task3