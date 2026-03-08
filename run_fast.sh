#!/bin/bash

# activate virtual environment
echo "Activating virtual environment..."
source ./.venv/bin/activate

# run fastapi app
echo "Running FastAPI server..."
uvicorn fast:app --reload
