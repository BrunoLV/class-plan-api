#!/bin/sh

export FLASK_RUN_PORT=8080
export FLASK_ENV=development
export FLASK_APP=./src/app.py

export DB_CONNECTION_STRING=postgresql+psycopg2://root:root@localhost:5433/class_plan_db


flask run