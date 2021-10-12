#!/bin/sh

export FLASK_RUN_PORT=8080
export DB_CONNECTION_STRING=p--host=0.0.0.0ostgresql+psycopg2://root:root@db:5432/class_plan_db
export FLASK_CONFIG=development
export FLASK_APP=run.py

flask db migrate
flask db upgrade
flask run --host=0.0.0.0