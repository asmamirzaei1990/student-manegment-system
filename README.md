# Student Management System

A Python CLI project demonstrating clean separation of models, data/seed definitions, repositories, services, validation, exceptions, menus, logging, SQLite persistence, and tests.

## Architecture

```text
Menu/UI -> Service -> Repository -> SQLite
              |          |
          Validation   Database
          Exceptions
```

## Features
- Student, Professor, Course, Enrollment, Grade management
- CRUD and search operations
- SQLite persistence
- Course capacity checks
- Duplicate enrollment prevention
- Grade validation (0..20) and enrollment requirement
- Email / numeric validation
- Custom exceptions
- Logging
- Pytest tests
- Seed data on first run

## Run

```bash
python main.py
```

The database `student_management.db` is created automatically in the project root.

## Tests

```bash
pytest -q
```

## Reset database

```python
from database import Database
Database().reset()
```

Then run `python main.py` again.
