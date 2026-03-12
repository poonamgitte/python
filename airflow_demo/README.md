# Apache Airflow Demo Project

This repository contains sample **Apache Airflow DAGs** demonstrating
core workflow orchestration concepts such as task scheduling,
dependencies, retries, XCom communication, and database integration.

The goal of this project is to understand how **Airflow
pipelines are created and executed**.

------------------------------------------------------------------------

# What is Apache Airflow?

**Apache Airflow** is an open‑source platform used to **programmatically
author, schedule, and monitor workflows**.

Workflows are defined using **Python code** and organized as **DAGs
(Directed Acyclic Graphs)**. Each workflow consists of multiple tasks
that run based on defined dependencies.

------------------------------------------------------------------------

# Key Concepts

## DAG (Directed Acyclic Graph)

A **DAG** represents a workflow and defines: - Tasks - Dependencies
between tasks - Execution schedule

Example:

Task A → Task B → Task C

------------------------------------------------------------------------

## Task

A **task** is a single unit of work in a DAG.

Examples: - Running a bash command - Executing a Python function -
Querying a database - Calling an API

------------------------------------------------------------------------

## Operators

Operators define **what type of task should run**.

Common operators used in this project:

-   **BashOperator** -- Runs bash commands
-   **PythonOperator** -- Executes Python functions

------------------------------------------------------------------------

## Scheduler

The **Airflow Scheduler** triggers DAG runs based on the defined
schedule.

Examples:

@daily\
@hourly\
@weekly

------------------------------------------------------------------------

## XCom (Cross Communication)

**XCom** allows tasks to share small amounts of data between each other.

Example: - Task 1 generates a value - Task 2 reads that value

------------------------------------------------------------------------

# Example DAGs in this Repository

  -----------------------------------------------------------------------
  DAG Name                            Description
  ----------------------------------- -----------------------------------
  simple_bash_dag                     Prints "Hello World" using
                                      BashOperator

  bash_task_chain                     Demonstrates task dependencies with
                                      bash tasks

  python_task_chain                   Demonstrates task dependencies
                                      using PythonOperator

  read_employees_from_postgres        Reads employee data from PostgreSQL

  schedule_retry_xcom_demo            Demonstrates scheduling, retries,
                                      and XCom communication
  -----------------------------------------------------------------------

# Alembic Migration 

This project uses Alembic to manage database schema changes. Alembic works with SQLAlchemy and allows version-controlled database migrations.

Migration scripts are stored in the alembic/versions directory and can be used to upgrade or downgrade the database schema.

1) Run migration

  alembic upgrade head

2) Create new migration

  alembic revision --autogenerate -m "migration message"

------------------------------------------------------------------------

# Method 1: Install Airflow Using Python Virtual Environment

## Step 1 -- Create Virtual Environment

``` bash
python3 -m venv airflow_env
```

Activate environment

Linux / Mac

``` bash
source airflow_env/bin/activate
```

Windows

``` bash
airflow_env\Scripts\activate
```

------------------------------------------------------------------------

## Step 2 -- Install Apache Airflow

pip install "apache-airflow==3.1.7" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.7/constraints-3.12.txt"

The **constraints file ensures compatible dependency versions**.

------------------------------------------------------------------------

## Step 3 -- Set Airflow Home

``` bash
export AIRFLOW_HOME=$HOME/airflow
```

------------------------------------------------------------------------

## Step 4 -- Initialize Database

``` bash
airflow db migrate
```

------------------------------------------------------------------------

## Step 5 -- Start Airflow

``` bash
airflow standalone
```

This command will automatically:

-   Initialize the database
-   Create admin user
-   Start scheduler
-   Start webserver

------------------------------------------------------------------------

## Step 6 -- Access Airflow UI

Open browser:

http://localhost:8080

Login credentials will appear in the terminal.

------------------------------------------------------------------------

## Step 7 -- Add DAG Files

Place your DAG files inside:

\~/airflow/dags

Airflow automatically loads DAGs from this folder.

------------------------------------------------------------------------

# Method 2: Run Airflow Using Docker

Docker is the **recommended method** for running Airflow in development
and production.

------------------------------------------------------------------------

## Step 1 -- Install Docker

Download Docker Desktop:

https://www.docker.com/products/docker-desktop

Verify installation:

``` bash
docker --version
```

------------------------------------------------------------------------

## Step 2 -- Download Official Docker Compose File

``` bash
curl -LfO https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
```

------------------------------------------------------------------------

## Step 3 -- Create Required Directories

``` bash
mkdir -p ./dags ./logs ./plugins
```

------------------------------------------------------------------------

## Step 4 -- Create Environment File

``` bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

------------------------------------------------------------------------

## Step 5 -- Initialize Airflow

``` bash
docker compose up airflow-init
```

------------------------------------------------------------------------

## Step 6 -- Start Airflow

``` bash
docker compose up
```

This starts:

-   Airflow Webserver
-   Airflow Scheduler
-   PostgreSQL
-   Redis

------------------------------------------------------------------------

## Step 7 -- Open Airflow UI

http://localhost:8080

Default credentials:

username: airflow
password: airflow

------------------------------------------------------------------------

## Step 8 -- Add DAGs

Place DAG files inside:

./dags

Docker automatically detects them.

------------------------------------------------------------------------

# Technologies Used

-   Apache Airflow
-   Python
-   PostgreSQL
-   SQLAlchemy
-   Docker

------------------------------------------------------------------------

# Purpose of This Project

This project demonstrates:

-   Creating DAGs
-   Task dependencies
-   Scheduling workflows
-   Retry mechanisms
-   XCom communication
-   Database integration with PostgreSQL

