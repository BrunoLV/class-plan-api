from datetime import date
from json.encoder import JSONEncoder


def json_default(value):
    if isinstance(value, date):
        return value.isoformat()
    else:
        return value.__dict__


class TeacherDtoJsonEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class GroupDtoJsonEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class SubjectDtoJsonEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class ClassPlanDtoJsonEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__
