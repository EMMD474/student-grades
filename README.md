# Student Grades API

Simple REST API project for managing students and grades, with two implementations:

- Flask app in `main.py`
- FastAPI app in `fast.py`

Data is stored in memory, so all changes reset when the server restarts.

## Prerequisites

- Python 3.10+
- `pip`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install flask fastapi "uvicorn[standard]" pydantic
```

## Run The API

### Flask (`main.py`)

```bash
source .venv/bin/activate
flask --app main --debug run
```

Default URL: `http://127.0.0.1:5000`

### FastAPI (`fast.py`)

```bash
source .venv/bin/activate
uvicorn fast:app --reload
```

Default URL: `http://127.0.0.1:8000`

## Endpoints

Common routes in both implementations:

- `GET /` - Welcome message.
- `GET /students` - List students.
- `GET /students/{student_id}` - Fetch a single student.
- `POST /students` - Create a student.
- `POST /student-grades` - Add a grade for a student.

Flask-only route:

- `PUT /student-grades/{student_id}`

## Example Requests

Create a student:

```bash
curl -X POST http://127.0.0.1:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice"}'
```

Add a grade:

```bash
curl -X POST http://127.0.0.1:5000/student-grades \
  -H "Content-Type: application/json" \
  -d '{"student_id":1,"subject":"Math","grade":92}'
```

## API Spec

OpenAPI spec file: [`openapi.yaml`](./openapi.yaml)

## Project Structure

- `main.py` - Flask implementation.
- `fast.py` - FastAPI implementation.
- `openapi.yaml` - OpenAPI 3.0 spec.
- `run.sh` - Flask helper script (currently references `test.py`; use the command above).
- `run_fast.sh` - FastAPI helper script.
