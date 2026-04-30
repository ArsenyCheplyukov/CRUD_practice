# FastAPI + PostgreSQL Learning Project

## Goal

This project is a fast hands-on practice to rebuild backend skills using:

- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker

Main goal:

- refresh core backend concepts
- understand architecture (API → Service → Repository → DB)
- build a reusable reference project

---

## Tech Stack

- FastAPI
- SQLAlchemy 2.0 (async)
- PostgreSQL
- Docker / Docker Compose
- Pydantic

---

## Project Structure

app/

- api/ → HTTP layer (routes)
- core/ → config and database setup
- models/ → ORM models (tables)
- schemas/ → Pydantic schemas (DTO)
- repositories/ → DB queries
- services/ → business logic
- main.py → entry point

---

## What is implemented

### 1. Basic FastAPI setup

- application initialized
- health check endpoint added

### 2. Docker environment

- PostgreSQL container
- volume for data persistence
- environment variables via .env

### 3. Database connection

- async SQLAlchemy engine
- session factory
- dependency injection for DB session

---

## Key Concepts Learned

### SQLAlchemy Layers

- ORM → used for most operations
- Raw SQL → used for complex queries
- Core → optional query builder

Decision:
Use ORM as main approach + raw SQL when needed

---

### Engine vs Session

- Engine = connection pool
- Session = unit of work per request

Important:

- one session per request
- no global sessions

---

### Dependency Injection (FastAPI)

- DB session created per request
- automatically closed after request
- prevents connection leaks

---

## Problems Faced

- confusion with Python module paths inside Docker
- PostgreSQL volume path differences
- initial uncertainty with async SQLAlchemy setup

---

## Notes

This project is intentionally simple.

Focus:

- understanding fundamentals
- clean architecture
- reproducibility

---

## Next Steps

- create ORM models
- implement repositories
- add service layer
- build CRUD endpoints
- handle relations and N+1 problem
