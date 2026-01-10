🚀 Taskitech API

Taskitech is a robust backend service built with FastAPI and SQLAlchemy, designed for task management.
It follows a clean, modular architecture that separates concerns between data models, database logic, business rules, and API routing.
🏗️ Architecture & Design

The project follows a Layered Architecture pattern, which ensures scalability, maintainability, and easier testing.

🔹 API Layer (main.py)

Defines RESTful endpoints

Handles HTTP requests and responses

Manages dependency injection for the database

🔹 Controller Layer (controller.py)

Orchestrates business logic

Acts as a bridge between API routes and the data repository

🔹 Repository Layer (repository.py)

Manages database connections

Handles SQLAlchemy session lifecycle

Provides the database engine

🔹 Data Layer (models.py & schemas.py)

models.py: Defines database tables using SQLAlchemy ORM

schemas.py: Defines data validation and serialization using Pydantic

📁 Project Structure
Project Alpha/
├── backend/
│   ├── __init__.py          # Marks directory as a Python package
│   ├── main.py              # Entry point: FastAPI app and routes
│   ├── models.py            # SQLAlchemy database models
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── controller.py        # Business logic and CRUD orchestration
│   └── repository.py        # DB connection and session configuration
├── venv/                    # Virtual environment
└── README.md                # Project documentation

🛠️ Tech Stack

- Framework: FastAPI
- ORM: SQLAlchemy
- Validation: Pydantic
- Database: SQLite (default for development)
- Server: Uvicorn (ASGI server)

🚀 Getting Started
✅ Prerequisites

Python 3.10+ 
pip installed

📦 Installation

Clone the project:

- git clone <repository-url>
- cd Project-Alpha


Create a virtual environment:
- python -m venv venv


Activate the virtual environment:
Windows
- venv\Scripts\activate

Mac / Linux
- source venv/bin/activate


Install dependencies:
- pip install fastapi uvicorn sqlalchemy pydantic[email]

▶️ Running the App

From the project root directory:
- uvicorn backend.main:app --reload

📋 API Endpoints

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| POST   | `/users`           | Create a new user account     |
| POST   | `/tasks`           | Create a new task for a user  |
| GET    | `/tasks/{user_id}` | Retrieve all tasks for a user |
| PATCH  | `/tasks/{task_id}` | Update an existing task       |
| DELETE | `/tasks/{task_id}` | Delete a specific task        |

👥 Authors
In developemnt ~(\\-o-\\)`
