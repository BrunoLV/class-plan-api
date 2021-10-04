#!/bin/sh

export FLASK_RUN_PORT=8080
export FLASK_ENV=development
export FLASK_APP=./src/app.py
flask run