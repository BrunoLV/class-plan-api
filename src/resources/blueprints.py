from flask import Blueprint
from flask_restful import Api
from flask import current_app as app

from src.resources.class_plan import ClassPlanResource, ClassPlanCollectionResource


def init_blueprint_class_plan():
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    api.add_resource(ClassPlanResource, '/class-plans/<code>')
    api.add_resource(ClassPlanCollectionResource, '/class-plans/')
    app.register_blueprint(api_bp)