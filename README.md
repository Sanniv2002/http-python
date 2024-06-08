## Set Up this project locally

First, install all dependencies, make sure you have pip and python3 installed:

Create an virtual environment.

Mac/WSL/Ubuntu
```bash
python3 -m venv myenv
source myenv/bin/activate
```

If you're on windows.
```bash
pythone -m venv myenv
env\Scripts\activate
```

## Install Dependencies
```bash
pip install alembic psycopg2 sqlalchemy libpq-dev fastapi
```

## Create Migration Environment

```bash
alembic unit
'''

Find and open alembic.ini in your directory and change the 'sqlalchemy.url' to your database URI.

Also change the URL in database.py file to your db URI.

## Create and apply Migrate db

```bash
alembic revision --autogenerate -m "unit"
alembic upgrade head
```

## You're all set.

Run this command to start your server listening on a PORT:
```bash
uvicorn main:app --reload
```
*Never use the '--reload' flag in production.