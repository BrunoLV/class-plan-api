import copy
import json
from datetime import date

from flask import Blueprint, request, make_response, Response

from src.application.controllers.class_plan_controllers import ClassPlanController
from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, UpdateClassPlanCommand, \
    DeleteClassPlanCommand
from src.application.dtos.class_plan_dtos import ClassPlanDto
from src.application.dtos.encoders.class_plan_dtos_encoders import ClassPlanDtoJsonEncoder, json_default
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher

class_plan_blueprint = Blueprint('class_plan_blueprint', __name__, url_prefix='/class-plans')

class_plan_controller = ClassPlanController()


@class_plan_blueprint.route('/', methods=['POST'])
def create_class_plan() -> Response:
    command = _fill_create_command(request.json)
    created_code = class_plan_controller.create(command)
    response = make_response()
    response.status_code = 201
    response.headers['location'] = f'/class-plans/{created_code}'
    return response


@class_plan_blueprint.route('/<code>', methods=['PUT'])
def update_class_plan(code) -> Response:
    command = _fill_update_command(code, request.json)
    class_plan_controller.update(command)
    response = make_response()
    response.status_code = 204
    return response


@class_plan_blueprint.route('/<code>', methods=['DELETE'])
def delete_class_plan(code) -> Response:
    command = _fill_delete_command(code)
    class_plan_controller.delete(command)
    response = make_response()
    response.status_code = 204
    return response


@class_plan_blueprint.route('/<code>', methods=['GET'])
def get_class_plan(code) -> Response:
    entity = class_plan_controller.get(code)
    response = make_response()
    if entity is None:
        response.status_code = 404
    else:
        response.data = ClassPlanDto.from_entity(entity).to_json()
        response.status_code = 200
        response.headers['Content-Type'] = 'aplication/json'
    return response


@class_plan_blueprint.route("/", methods=['GET'])
def list_all_class_plans() -> Response:
    entities = class_plan_controller.list()
    response = make_response()
    if len(entities) > 0:
        dtos = [ClassPlanDto.from_entity(e) for e in entities]
        response.status_code = 200
        response.data = json.dumps(dtos, cls=ClassPlanDtoJsonEncoder, default=json_default, indent=4)
        response.headers['Content-Type'] = 'application/json'
    else:
        response.status_code = 204
    return response


def _fill_create_command(json_payload) -> CreateClassPlanCommand:
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


def _fill_delete_command(code) -> DeleteClassPlanCommand:
    command = DeleteClassPlanCommand()
    command.code = code
    return command
