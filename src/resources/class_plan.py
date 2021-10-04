import copy
import json
from datetime import date

from flask import request, make_response
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource

from src.application.controllers.class_plan_controllers import ClassPlanController
from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, UpdateClassPlanCommand, \
    DeleteClassPlanCommand
from src.application.dtos.class_plan_dtos import ClassPlanDto
from src.application.dtos.encoders.class_plan_dtos_encoders import ClassPlanDtoJsonEncoder, json_default
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher
from src.infrastructure.openapi.specs import ClassPlanSchema, ClassPlanRequestSchema


class ClassPlanResource(MethodResource, Resource):

    def __init__(self):
        self.controller = ClassPlanController()

    @doc(description="Get a class plan by code", tags=["class-plan"])
    @marshal_with(ClassPlanSchema, code=200, description="Resource found")
    @marshal_with(None, code=404, description="Resource not found")
    def get(self, code):
        entity = self.controller.get(code)
        response = make_response()
        if entity is None:
            response.status_code = 404
        else:
            response.data = ClassPlanDto.from_entity(entity).to_json()
            response.status_code = 200
            response.headers['Content-Type'] = 'aplication/json'
        return response

    @doc(description="Update a class plan", tags=["class-plan"])
    @use_kwargs(ClassPlanRequestSchema)
    @marshal_with(None, code=204, description="Resource updated")
    def put(self, code):
        command = ClassPlanResource._fill_update_command(code, request.json)
        self.controller.update(command)
        response = make_response()
        response.status_code = 204
        return response

    @doc(description="Delete a class plan", tags=["class-plan"])
    @marshal_with(None, code=204, description="Resource removed")
    def delete(self, code):
        command = ClassPlanResource._fill_delete_command(code)
        self.controller.delete(command)
        response = make_response()
        response.status_code = 204
        return response

    @staticmethod
    def _fill_update_command(code, json_payload) -> UpdateClassPlanCommand:
        command = UpdateClassPlanCommand()
        command.code = code
        command.teacher = Teacher(code=json_payload['teacher']['code'], name=json_payload['teacher']['name'])
        command.group = Group(code=json_payload['group']['code'], name=json_payload['group']['name'])
        command.subject = Subject(code=json_payload['subject']['code'], name=json_payload['subject']['name'])
        command.date = date.fromisoformat(json_payload['date'])
        command.period = json_payload['period']
        command.contents = json_payload['contents']
        command.evaluation = json_payload['evaluation']
        command.materials = copy.copy(json_payload['materials'])
        command.goals = copy.copy(json_payload['goals'])
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
    def post(self):
        command = ClassPlanCollectionResource._fill_create_command(request.json)
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
        response = make_response()
        if len(entities) > 0:
            dtos = [ClassPlanDto.from_entity(e) for e in entities]
            response.status_code = 200
            response.data = json.dumps(dtos, cls=ClassPlanDtoJsonEncoder, default=json_default, indent=4)
            response.headers['Content-Type'] = 'application/json'
        else:
            response.status_code = 204
        return response

    @staticmethod
    def _fill_create_command(json_payload):
        command = CreateClassPlanCommand()
        command.teacher = Teacher(code=json_payload['teacher']['code'], name=json_payload['teacher']['name'])
        command.group = Group(code=json_payload['group']['code'], name=json_payload['group']['name'])
        command.subject = Subject(code=json_payload['subject']['code'], name=json_payload['subject']['name'])
        command.date = date.fromisoformat(json_payload['date'])
        command.period = json_payload['period']
        command.contents = json_payload['contents']
        command.evaluation = json_payload['evaluation']
        command.materials = copy.copy(json_payload['materials'])
        command.goals = copy.copy(json_payload['goals'])
        return command
