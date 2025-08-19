# Task Management App

A simple **Task Management API** built with **FastAPI**, **SQLAlchemy (async)**, and **PostgreSQL**.

---

## Features

- Create, Read, Update, Delete (CRUD) tasks
- Async database operations with SQLAlchemy
- RESTful API endpoints
- PostgreSQL database integration

---

## Project Structure

task-management-app/
│── app/
│ │── main.py
│ │── crud.py
│ │── models.py
│ │── schemas.py
│ │── database.py
│ │── routers/
│ │── tasks.py
│── create_table.py
│── .env
│── README.md
│── .gitignore


## Installation

1. Clone the repository:

```bash
git clone https://github.com/coder-jayp/task-management-app.git
cd task-management-app

2. Create a virtual environment and activate it:

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

3. Install dependencies:

pip install fastapi sqlalchemy asyncpg uvicorn python-dotenv

4. Create a .env file in the project root with your database URL:

DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/taskmanagerdb

Replace user, password, and taskmanagerdb with your own credentials.

Usage

1. Create database tables:

```bash
python create_table.py

2. Start the FastAPI server:

uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

3. Open API docs in your browser:

http://127.0.0.1:8001/docs

## API Endpoints

- `POST /tasks/` → Create a new task  
- `GET /tasks/` → Get all tasks  
- `GET /tasks/{task_id}` → Get a single task by ID  
- `PUT /tasks/{task_id}` → Update a task  
- `DELETE /tasks/{task_id}` → Delete a task
