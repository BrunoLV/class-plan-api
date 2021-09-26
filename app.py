from flask import Flask

from src.infrastructure.blueprints.class_plan_blueprints import class_plan_blueprint

app = Flask(__name__)
app.register_blueprint(class_plan_blueprint)
