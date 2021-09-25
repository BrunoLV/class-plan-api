from flask import Flask
from flask_restful import Api

from src.application.controllers.class_plan_controllers import ClassPlanController, ClassPlanCollectionController

app = Flask(__name__)
api = Api(app)

api.add_resource(ClassPlanController, '/class-plans/<code>')
api.add_resource(ClassPlanCollectionController, '/class-plans')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
