# FastAPI + PostgreSQL Learning Project

## Overview

This project is a backend learning implementation designed to rebuild and solidify core backend engineering skills using a modern Python stack.

The focus is not just on building CRUD functionality, but on understanding how a real backend system is structured and evolves over time.

### Core stack

- FastAPI (API layer)
- SQLAlchemy 2.0 (async ORM)
- PostgreSQL (database)
- Pydantic v2 (data validation)
- Docker / Docker Compose (environment)

---

## Project Goals

- Rebuild backend fundamentals from scratch
- Understand layered architecture:
  - API → Service → Repository → Database
- Learn async database interaction patterns
- Understand ORM behavior and transaction lifecycle
- Build a reusable backend template for future projects

---

## Architecture Overview

The system follows a strict layered architecture:

Client → FastAPI (API Layer) → Service Layer → Repository Layer → SQLAlchemy ORM → PostgreSQL

### Layer responsibilities

- **API layer**: request handling, response formatting, dependency injection
- **Service layer**: business logic and transaction control
- **Repository layer**: database queries and persistence logic
- **ORM layer**: object-relational mapping to PostgreSQL

---

## Project Structure

app/
├── api/ # HTTP routes (FastAPI layer)
├── core/ # configuration, DB, dependencies
├── models/ # SQLAlchemy ORM models
├── schemas/ # Pydantic DTOs (request/response models)
├── repositories/ # database access layer
├── services/ # business logic layer
└── main.py # application entry point

---

## Key Concepts Implemented

### 1. FastAPI Fundamentals

- Route handling using APIRouter
- Health check endpoint
- Dependency injection system (Depends)

---

### 2. Async Database Layer

- SQLAlchemy 2.0 async engine
- AsyncSession lifecycle management
- PostgreSQL integration via asyncpg

Important rules:

- one session per request
- no global session usage
- sessions managed via FastAPI dependencies

---

### 3. Dependency Injection (DI)

FastAPI DI is used for:

- database session (`get_db`)
- service layer injection (`get_user_service`)

This ensures:

- no global state
- controlled lifecycle of resources
- better testability

---

## ORM Layer (SQLAlchemy)

### Model design

Entities:

- User
- Post
- Comment

### Relationships

- User → Posts (1:N)
- User → Comments (1:N)
- Post → Comments (1:N)

Relationships are defined using:

- `ForeignKey`
- `relationship`
- `back_populates`

---

### Important ORM behavior

- Objects are tracked by session
- `add()` does not execute SQL immediately
- SQL is executed on `commit()`
- `refresh()` reloads DB state into object

This follows Unit of Work pattern.

---

## Schema Layer (Pydantic v2)

Pydantic is used as a DTO layer between API and ORM.

### Schema types

- `UserCreate` → request input
- `UserRead` → response output

### Key principle

ORM models are NEVER exposed directly to API.

Instead:

- ORM → internal representation
- Pydantic → external contract

### ORM compatibility

- `from_attributes = True` enables ORM → Pydantic conversion

---

## Service Layer

The service layer contains business logic and transaction control.

### Responsibilities

- validation of business rules
- orchestration of repository calls
- transaction management (`commit`, `refresh`)
- error handling

### Example behavior

- check if user exists
- create user if not exists
- handle race conditions via DB constraints

---

## Repository Layer

Repository isolates all database operations.

### Responsibilities

- execute SQLAlchemy queries
- return ORM objects
- no business logic
- no transaction control

### Example operations

- get user by id
- get user by name
- create user
- list users

---

## Transaction Flow

Typical request lifecycle:

Request → API → Service → Repository → ORM → Database → Response

---

## Database Initialization

- Tables created on application startup
- Uses FastAPI lifespan event
- Async-safe initialization via `run_sync`

---

## Docker Environment

Project runs in Docker with:

- PostgreSQL container
- Application container
- Shared network communication
- Environment variables via `.env`

---

## Code Quality Tools

The project uses:

- black → formatting
- isort → import sorting
- ruff → linting

Purpose:

- enforce consistent code style
- reduce manual formatting errors
- improve readability and maintainability

---

## Key Problems Solved

- async SQLAlchemy setup issues
- Docker module path resolution
- incorrect ORM usage patterns
- circular import handling in models
- misunderstanding of session lifecycle
- improper separation of layers (initial stage)

---

## Important Design Decisions

### Why Repository + Service split exists

- repository → data access only
- service → business logic and orchestration

This improves:

- testability
- scalability
- separation of concerns

---

### Why schemas are separate from ORM

- prevents leaking database structure into API
- enables independent API evolution
- improves validation control

---

### Why async SQLAlchemy is used

- non-blocking I/O
- better scalability under concurrent requests
- aligns with FastAPI async model

---

## Current Status

The project is in a stable architectural state:

- layered backend structure implemented
- async database fully integrated
- DI system in place
- schema separation enforced
- codebase formatted and linted

---

## Next Steps

Planned improvements:

- introduce Alembic migrations (schema versioning)
- replace create_all with migration system
- add seed/test data
- expand API with additional entities (Post, Comment)
- investigate ORM loading strategies (N+1, lazy/eager loading)

---

Introduce Alembic migrations (schema versioning)

- replace create_all with migration system
- add seed/test data
- expand API with additional entities (Post, Comment)
- investigate ORM loading strategies (N+1, lazy/eager loading)

---
