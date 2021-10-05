import os

from flask import Flask
from src.infrastructure.db.orm.orms import db
from src.resources import blueprints
from src.documentation import documentations

app = Flask(__name__)

with app.app_context():
    blueprints.init_blueprint_class_plan()
    documentations.init_documentation()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)
