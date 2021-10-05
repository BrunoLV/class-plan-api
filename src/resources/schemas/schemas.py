from marshmallow import Schema, fields


class TeacherSchema(Schema):
    code = fields.Str(metadata={"description": "Teacher's code"})
    name = fields.Str(metadata={"description": "Teacher's name"})


class SubjectSchema(Schema):
    code = fields.Str(metadata={"description": "Subject's code"})
    name = fields.Str(metadata={"description": "Subject's name"})


class GroupSchema(Schema):
    code = fields.Str(metadata={"description": "Group's code"})
    name = fields.Str(metadata={"description": "Group's name"})


class ClassPlanSchema(Schema):
    code = fields.Str(metadata={"description": "Class Plan's code"})
    group = fields.Nested(GroupSchema(), metadata={"description": "Class Group"})
    teacher = fields.Nested(TeacherSchema(), metadata={"description": "Class Plan's teacher"})
    subject = fields.Nested(SubjectSchema(), metadata={"description": "Class Group"})
    contents = fields.Str(metadata={"description": "Class contents"})
    evaluation = fields.Str(metadata={"description": "Class evaluation"})
    date = fields.Date(metadata={"description": "Class Date"})
    period = fields.Str(metadata={"description": "Class Period", "enum": ["FIRST", "SECOND", "THIRD", "FOURTH"]})
    materials = fields.List(fields.Str(), metadata={"description": "Necessary materials for the class"})
    goals = fields.List(fields.Str(), metadata={"description": "Goals planned for the class"})


class ClassPlanRequestSchema(Schema):
    teacher = fields.Nested(TeacherSchema(), metadata={"description": "Class Plan's teacher"})
    group = fields.Nested(GroupSchema(), metadata={"description": "Class Group"})
    subject = fields.Nested(SubjectSchema(), metadata={"description": "Class Subject"})
    contents = fields.Str(metadata={"description": "Class contents"})
    evaluation = fields.Str(metadata={"description": "Class evaluation"})
    date = fields.Date(metadata={"description": "Class Date"})
    period = fields.Str(metadata={"description": "Class Period", "enum": ["FIRST", "SECOND", "THIRD", "FOURTH"]})
    materials = fields.List(fields.Str(), metadata={"description": "Necessary materials for the class"})
    goals = fields.List(fields.Str(), metadata={"description": "Goals planned for the class"})
