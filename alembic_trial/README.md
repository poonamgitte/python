# Alembic Migration Demo

This folder contains practice exercises for **Alembic migrations** in Python using **SQLAlchemy**.  
It demonstrates how to manage database schema changes, create migrations, and apply them.

---

## Setup Instructions

1. **Clone the repository** (if not already done):

git clone https://github.com/poonamgitte/python.git
cd python/alembic_migration

2. create a virtual environment 

python -m venv venv
# Activate the environment
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows

3. Install dependencies:
pip install sqlalchemy alembic psycopg2-binary


Alembic Migration Commands

1. Initialize Alembic(if not done already):
alembic init alembic

2. Create a new migration:
alembic revision --autogenerate -m "migration message"

3. Apply the latest migration:
alembic upgrade head

4. Rollback migration (optional):
alembic downgrade -1