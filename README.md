# Student Grades API

A simple REST API built with Flask for managing students and their academic grades.

## Features

- **Welcome Message**: Basic sanity check at the root endpoint.
- **Student Management**: Create and retrieve student profiles.
- **Grade Tracking**: Add and associate grades with specific students.
- **In-Memory Storage**: Current implementation uses volatile memory for data persistence.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Setup

1.  **Virtual Environment**: Activate the pre-configured virtual environment.

    ```bash
    source .venv/bin/activate
    ```

2.  **Run the Server**: Use the provided shell script to start the Flask application in debug mode.
    ```bash
    ./run.sh
    ```
    The server will be available at `http://localhost:5000`.

## API Documentation

The API's endpoints and data structures are fully documented using the OpenAPI 3.0.3 specification in [openapi.yaml](file:///home/emmd/Workstation/school/student-grades/openapi.yaml).

### Summary of Endpoints

- `GET /`: Welcome message.
- `GET /students`: List all students and their recorded grades.
- `POST /students`: Create a new student (Requires: `name`).
- `GET /students/{id}`: Detailed view of a single student.
- `POST /student-grades`: Add a grade for a student (Requires: `student_id`, `subject`, `grade`).

## Project Structure

- `main.py`: The core Flask application logic.
- `openapi.yaml`: API documentation and schema definitions.
- `run.sh`: Helper script for environment setup and server execution.
