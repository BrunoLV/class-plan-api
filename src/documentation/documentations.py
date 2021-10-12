from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import current_app as app
from flask_apispec.extension import FlaskApiSpec

from src.resources.class_plan import ClassPlanResource, ClassPlanCollectionResource


def init_documentation():
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
