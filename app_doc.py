import datetime
import uuid

from flask import make_response
from flask_openapi3 import OpenAPI
from flask_openapi3.models import Info, Tag

from src.infrastructure.openapi.specs import ClassPlan, ClassPlanPath, ClassPlanBody, ClassPlanListResponse

info = Info(title='Class Plan API', version='1.0.0')
app = OpenAPI(__name__, info=info)

class_plan_tag = Tag(name='Class Clan', description="Class Plan API operations")


@app.post('/class-plan/', tags=[class_plan_tag])
def create_class_plan(body: ClassPlanBody):
    """create class plan
    create a class plan in the system
    """

    response = make_response()
    response.status_code = 201
    response.headers['location'] = f'/class-plans/{uuid.uuid4()}'

    return response


@app.put('/class-api/<code>', tags=[class_plan_tag])
def update_class_plan(path: ClassPlanPath, body: ClassPlanBody):
    """update class plan
    update de class plan data in the system
    """

    response = make_response()
    response.status_code = 204

    return response


@app.delete('/class-api/<code>', tags=[class_plan_tag])
def delete_class_plan(path: ClassPlanPath):
    """delete class plan
    delete a class plan querying by code
    """

    response = make_response()
    response.status_code = 204

    return response


@app.get('/class-plan/<code>', tags=[class_plan_tag], responses={"200": ClassPlan})
def get_class_plan(path: ClassPlanPath):
    """get class
    get a class plan querying by code.
    """

    data = {
        'code': path.code,
        'teacher': {
            'code': '1',
            'name': 'Teste'
        },
        'group': {
            'code': '1',
            'name': 'Teste'
        },
        'subject': {
            'code': '1',
            'name': 'Teste'
        },
        'period': 'FIRST',
        'contents': 'Teste',
        'evaluation': 'Teste',
        'date': datetime.date.today().isoformat(),
        'materials': ['teste-1', 'teste-2'],
        'goals': ['teste-1', 'teste-2']
    }

    return data


@app.get('/class-plan/', tags=[class_plan_tag], responses={'200': ClassPlanListResponse})
def get_all_class_plan():
    """get all class plans
    get all class plans.
    """

    data = {
        'code': uuid.uuid4(),
        'teacher': {
            'code': '1',
            'name': 'Teste'
        },
        'group': {
            'code': '1',
            'name': 'Teste'
        },
        'subject': {
            'code': '1',
            'name': 'Teste'
        },
        'period': 'FIRST',
        'contents': 'Teste',
        'evaluation': 'Teste',
        'date': datetime.date.today().isoformat(),
        'materials': ['teste-1', 'teste-2'],
        'goals': ['teste-1', 'teste-2']
    }

    response = make_response()
    response.status_code = 204
    response.data = {
        'total': len(data),
        'list': data
    }

    return response


if __name__ == '__main__':
    app.run()
