import copy
import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.application.dtos.encoders.class_plan_dtos_encoders import ClassPlanDtoJsonEncoder, GroupDtoJsonEncoder, \
    SubjectDtoJsonEncoder, TeacherDtoJsonEncoder, json_default
from src.domain.entities.class_plan import ClassPlan
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher


@dataclass
class TeacherDto():
    code: str
    name: str

    @staticmethod
    def from_entity(entity: Teacher):
        return TeacherDto(
            code=entity.code,
            name=entity.name
        )

    def to_entity(self):
        return Teacher(
            code=self.code,
            name=self.name
        )

    def to_json(self):
        return json.dumps(self, cls=TeacherDtoJsonEncoder, default=json_default)


@dataclass
class SubjectDto():
    code: str
    name: str

    @staticmethod
    def from_entity(entity: Subject):
        return SubjectDto(
            code=entity.code,
            name=entity.name
        )

    def to_entity(self):
        return Subject(
            code=self.code,
            name=self.name
        )

    def to_json(self):
        return json.dumps(self, cls=SubjectDtoJsonEncoder, default=json_default)


@dataclass
class GroupDto():
    code: str
    name: str

    @staticmethod
    def from_entity(entity: Group):
        return GroupDto(
            code=entity.code,
            name=entity.name
        )

    def to_entity(self):
        return Group(
            code=self.code,
            name=self.name
        )

    def to_json(self):
        return json.dumps(self, cls=GroupDtoJsonEncoder, default=json_default)


@dataclass
class ClassPlanDto():
    code: str
    teacher: TeacherDto
    group: GroupDto
    subject: SubjectDto
    period: str
    contents: str
    evaluation: str
    date: datetime.date
    materials: List
    goals: List

    @staticmethod
    def from_entity(entity: ClassPlan):
        return ClassPlanDto(
            code=entity.code,
            teacher=TeacherDto.from_entity(entity.teacher),
            group=GroupDto.from_entity(entity.group),
            subject=SubjectDto.from_entity(entity.subject),
            period=entity.period,
            contents=entity.contents,
            evaluation=entity.evaluation,
            date=copy.deepcopy(entity.date),
            materials=copy.deepcopy(entity.materials),
            goals=copy.deepcopy(entity.goals)
        )

    def to_json(self):
        return json.dumps(self, cls=ClassPlanDtoJsonEncoder, default=json_default, indent=4)
