import copy

from flask import make_response
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource, abort

from src.application.controllers.class_plan_controllers import ClassPlanController
from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, UpdateClassPlanCommand, \
    DeleteClassPlanCommand
from src.domain.exceptions.domais_expections import EntityhNotFoundError
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher
from src.resources.schemas.schemas import ClassPlanSchema, ClassPlanRequestSchema


class ClassPlanResource(MethodResource, Resource):

    def __init__(self):
        self.controller = ClassPlanController()

    @doc(description="Get a class plan by code", tags=["class-plan"])
    @marshal_with(ClassPlanSchema, code=200, description="Resource found")
    @marshal_with(None, code=404, description="Resource not found")
    def get(self, code):
        try:
            entity = self.controller.get(code)
            return entity, 200
        except EntityhNotFoundError:
            abort(404)

    @doc(description="Update a class plan", tags=["class-plan"])
    @use_kwargs(ClassPlanRequestSchema)
    @marshal_with(None, code=204, description="Resource updated")
    @marshal_with(None, code=404, description="Resource not found")
    def put(self, code, **kwargs):
        try:
            command = ClassPlanResource._fill_update_command(code, kwargs)
            self.controller.update(command)
            return '', 204
        except EntityhNotFoundError:
            abort(404)

    @doc(description="Delete a class plan", tags=["class-plan"])
    @marshal_with(None, code=204, description="Resource removed")
    @marshal_with(None, code=404, description="Resource not found")
    def delete(self, code):
        try:
            command = ClassPlanResource._fill_delete_command(code)
            self.controller.delete(command)
            return '', 204
        except EntityhNotFoundError:
            abort(404)

    @staticmethod
    def _fill_update_command(code, kwargs) -> UpdateClassPlanCommand:
        command = UpdateClassPlanCommand()
        command.code = code
        command.teacher = Teacher(code=kwargs['teacher']['code'], name=kwargs['teacher']['name'])
        command.group = Group(code=kwargs['group']['code'], name=kwargs['group']['name'])
        command.subject = Subject(code=kwargs['subject']['code'], name=kwargs['subject']['name'])
        command.date = kwargs['date']
        command.period = kwargs['period']
        command.contents = kwargs['contents']
        command.evaluation = kwargs['evaluation']
        command.materials = copy.copy(kwargs['materials'])
        command.goals = copy.copy(kwargs['goals'])
        return command

    @staticmethod
    def _fill_delete_command(code) -> DeleteClassPlanCommand:
        command = DeleteClassPlanCommand()
        command.code = code
        return command


class ClassPlanCollectionResource(MethodResource, Resource):

    def __init__(self):
        self.controller = ClassPlanController()

    @doc(description="Create a class plan", tags=["class-plan"])
    @use_kwargs(ClassPlanRequestSchema)
    @marshal_with(None, code=201, description="Resource created")
    def post(self, **kwargs):
        command = ClassPlanCollectionResource._fill_create_command(kwargs)
        created_code = self.controller.create(command)
        response = make_response()
        response.status_code = 201
        response.headers['location'] = f'/class-plans/{created_code}'
        return response

    @doc(description="Get all class plans", tags=["class-plan"])
    @marshal_with(ClassPlanSchema(many=True), code=200, description="Resources found")
    @marshal_with(None, code=204, description="Nothing to present")
    def get(self):
        entities = self.controller.list()
        if len(entities) > 0:
            return entities, 200
        else:
            return '', 204

    @staticmethod
    def _fill_create_command(kwargs):
        command = CreateClassPlanCommand()
        command.teacher = Teacher(code=kwargs['teacher']['code'], name=kwargs['teacher']['name'])
        command.group = Group(code=kwargs['group']['code'], name=kwargs['group']['name'])
        command.subject = Subject(code=kwargs['subject']['code'], name=kwargs['subject']['name'])
        command.date = kwargs['date']
        command.period = kwargs['period']
        command.contents = kwargs['contents']
        command.evaluation = kwargs['evaluation']
        command.materials = copy.copy(kwargs['materials'])
        command.goals = copy.copy(kwargs['goals'])
        return command
