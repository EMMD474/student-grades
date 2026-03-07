#!/bin/bash

# activate virtual environment
echo "Activating virtual environment..."
sleep 1
source ./.venv/bin/activate

# set environment variables
export FLASK_APP=test.py
export FLASK_DEBUG=1

# run flask app
echo "Running Flask server..."
flask run