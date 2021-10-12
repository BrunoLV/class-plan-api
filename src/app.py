from flask import Flask
from flask_migrate import Migrate

from src.config.config import app_config
from src.documentation import documentations
from src.infrastructure.db.orm.orms import db
from src.resources import blueprints


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    with app.app_context():
        blueprints.init_blueprint_class_plan()
        documentations.init_documentation()

    migrate = Migrate(app, db)
    db.init_app(app)

    migrate.init_app(app, db)

    @app.errorhandler(422)
    def handler_error_422(error):
        return error.exc.messages, 422

    return app
