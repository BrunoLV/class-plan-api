#!/bin/sh

export FLASK_CONFIG=development
export FLASK_APP=run.py

flask db migrate
flask db upgrade