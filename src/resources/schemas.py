import typing

from marshmallow import Schema, fields, validate, types, ValidationError


class TeacherSchema(Schema):
    code = fields.Str(required=True, metadata={"description": "Teacher's code"},
                      validate=validate.Length(min=1, error="TESE"))
    name = fields.Str(required=True, metadata={"description": "Teacher's name"}, validate=validate.Length(min=3))


class SubjectSchema(Schema):
    code = fields.Str(required=True, metadata={"description": "Subject's code"}, validate=validate.Length(min=1))
    name = fields.Str(required=True, metadata={"description": "Subject's name"}, validate=validate.Length(min=3))


class GroupSchema(Schema):
    code = fields.Str(required=True, metadata={"description": "Group's code"}, validate=validate.Length(min=1))
    name = fields.Str(required=True, metadata={"description": "Group's name"}, validate=validate.Length(min=3))


class ClassPlanSchema(Schema):
    code = fields.Str(required=True, metadata={"description": "Class Plan's code"}, validate=validate.Length(min=1))
    group = fields.Nested(GroupSchema(), required=True, metadata={"description": "Class Group"})
    teacher = fields.Nested(TeacherSchema(), required=True, metadata={"description": "Class Plan's teacher"})
    subject = fields.Nested(SubjectSchema(), required=True, metadata={"description": "Class Group"})
    contents = fields.Str(required=True, metadata={"description": "Class contents"})
    evaluation = fields.Str(metadata={"description": "Class evaluation"})
    date = fields.Date(required=True, metadata={"description": "Class Date"})
    period = fields.Str(required=True,
                        metadata={"description": "Class Period", "enum": ["FIRST", "SECOND", "THIRD", "FOURTH"]})
    materials = fields.List(fields.Str(), metadata={"description": "Necessary materials for the class"})
    goals = fields.List(fields.Str(), metadata={"description": "Goals planned for the class"})

    def load(self, data: typing.Union[
        typing.Mapping[str, typing.Any],
        typing.Iterable[typing.Mapping[str, typing.Any]],
    ], *, many: typing.Optional[bool] = None,
             partial: typing.Optional[typing.Union[bool, types.StrSequenceOrSet]] = None,
             unknown: typing.Optional[str] = None):
        try:
            return super().load(data, many=many, partial=partial, unknown=unknown)
        except ValidationError as error:
            print(error)


class ClassPlanRequestSchema(Schema):
    group = fields.Nested(GroupSchema(), required=True, metadata={"description": "Class Group"})
    teacher = fields.Nested(TeacherSchema(), required=True, metadata={"description": "Class Plan's teacher"})
    subject = fields.Nested(SubjectSchema(), required=True, metadata={"description": "Class Group"})
    contents = fields.Str(required=True, metadata={"description": "Class contents"})
    evaluation = fields.Str(metadata={"description": "Class evaluation"})
    date = fields.Date(required=True, metadata={"description": "Class Date"})
    period = fields.Str(required=True,
                        metadata={"description": "Class Period", "enum": ["FIRST", "SECOND", "THIRD", "FOURTH"]})
    materials = fields.List(fields.Str(), metadata={"description": "Necessary materials for the class"})
    goals = fields.List(fields.Str(), metadata={"description": "Goals planned for the class"})
