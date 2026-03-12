from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from sqlalchemy import create_engine, text

# Same PostgreSQL database used by Alembic
#DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/airflow_demo_db"
DATABASE_URL = "postgresql+psycopg2://airflow:airflow@postgres:5432/employee_db"


def fetch_employees():
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM employees"))

        for row in result:
            print(row)

with DAG(
    dag_id="read_employees_from_postgres",
    start_date=datetime(2026, 3, 4),
    schedule="@daily"
) as dag:

    task = PythonOperator(
        task_id="read_table_data",
        python_callable=fetch_employees,
    )

    task