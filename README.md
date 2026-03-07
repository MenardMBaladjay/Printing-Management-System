# Printing Management System Backend

This is a FastAPI backend for a printing management system. It
implements basic CRUD operations for print orders and calculates the cost
based on simple pricing rules.

## Setup

1. Create and activate a virtual environment (`python -m venv .venv`).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `POST /orders` - create order
- `GET /orders` - list orders
- `GET /orders/{id}` - get order by id
- `PUT /orders/{id}` - update order
- `DELETE /orders/{id}` - delete order
