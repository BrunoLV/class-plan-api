#!/bin/sh

export FLASK_RUN_PORT=8080
export DB_CONNECTION_STRING=postgresql+psycopg2://root:root@localhost:5433/class_plan_db
export FLASK_CONFIG=development
export FLASK_APP=run.py

flask run