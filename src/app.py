from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, Blueprint
from flask_apispec.extension import FlaskApiSpec
from flask_restful import Api

from src.resources.class_plan import ClassPlanResource, ClassPlanCollectionResource

app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ClassPlanResource, '/class-plans/<code>')
api.add_resource(ClassPlanCollectionResource, '/class-plans/')

app.register_blueprint(api_bp)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='class-plans',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

docs = FlaskApiSpec(app)
docs.register(ClassPlanResource, blueprint="api")
docs.register(ClassPlanCollectionResource, blueprint="api")
