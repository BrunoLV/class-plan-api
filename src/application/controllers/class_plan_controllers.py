import copy
import datetime
import json

import flask
from flask import request, Response
from flask_restful import Resource

from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, DeleteClassPlanCommand, \
    UpdateClassPlanCommand
from src.application.cqs.commands.handlers.class_plan_commands_handlers import ClassPlanCommandHandler
from src.application.cqs.queries.handlers.class_plan_queries_handlers import ClassPlanQueryHandler
from src.application.dtos.class_plan_dtos import ClassPlanDto
from src.application.dtos.encoders.class_plan_dtos_encoders import ClassPlanDtoJsonEncoder, json_default
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher


class ClassPlanCollectionController(Resource):

    def __init__(self):
        self._command_handler = ClassPlanCommandHandler()
        self._query_handler = ClassPlanQueryHandler()

    def post(self):
        req_payload = request.json

        command = CreateClassPlanCommand()
        command.teacher = Teacher(code=req_payload["teacher"]["code"], name=req_payload["teacher"]["name"])
        command.group = Group(code=req_payload["group"]["code"], name=req_payload["group"]["name"])
        command.subject = Subject(code=req_payload["subject"]["code"], name=req_payload["subject"]["name"])
        command.date = datetime.date.fromisoformat(req_payload["date"])
        command.period = req_payload["period"]
        command.contents = req_payload["contents"]
        command.evaluation = req_payload["evaluation"]
        command.materials = copy.deepcopy(req_payload["materials"])
        command.goals = copy.deepcopy(req_payload["goals"])

        created_code = self._command_handler.handle_create_command(command)

        response: Response = flask.make_response()
        response.status_code = 201
        response.headers['location'] = f'/class-plan/{created_code}'
        return response

    def get(self):

        entities = self._query_handler.find_all()

        response: Response = flask.make_response()
        if len(entities) == 0:
            response.status_code = 204
        else:
            dtos = []
            for entity in entities:
                dtos.append(ClassPlanDto.from_entity(entity))
            response.status_code = 200
            response.data = json.dumps(dtos, cls=ClassPlanDtoJsonEncoder, default=json_default, indent=4)
            response.headers['Content-Type'] = 'application/json'

        return response


class ClassPlanController(Resource):

    def __init__(self):
        self._command_handler = ClassPlanCommandHandler()
        self._query_handler = ClassPlanQueryHandler()

    def put(self, code):
        req_payload = request.json

        command = UpdateClassPlanCommand()

        command.code = code
        command.teacher = Teacher(code=req_payload["teacher"]["code"], name=req_payload["teacher"]["name"])
        command.group = Group(code=req_payload["group"]["code"], name=req_payload["group"]["name"])
        command.subject = Subject(code=req_payload["subject"]["code"], name=req_payload["subject"]["name"])
        command.date = datetime.date.fromisoformat(req_payload["date"])
        command.period = req_payload["period"]
        command.contents = req_payload["contents"]
        command.evaluation = req_payload["evaluation"]
        command.materials = copy.deepcopy(req_payload["materials"])
        command.goals = copy.deepcopy(req_payload["goals"])

        self._command_handler.handle_update_command(command)

        response: Response = flask.make_response()
        response.status_code = 204
        return response

    def delete(self, code):
        command = DeleteClassPlanCommand()
        command.code = code
        self._command_handler.handle_delete_command(command)
        response: Response = flask.make_response()
        response.status_code = 204
        return response

    def get(self, code):
        entity = self._query_handler.find_by_code(code)

        response: Response = flask.make_response()

        if entity is None:
            response.status_code = 404
        else:
            response.data = ClassPlanDto.from_entity(entity).to_json()
            response.status_code = 200
            response.headers['Content-Type'] = 'aplication/json'

        return response
