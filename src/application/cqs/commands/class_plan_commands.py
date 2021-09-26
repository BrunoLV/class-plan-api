import uuid
from datetime import date

from src.domain.entities.class_plan import ClassPlan, PeriodEnum
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher


class CreateClassPlanCommand:
    teacher: Teacher
    group: Group
    subject: Subject
    period: PeriodEnum
    contents: str
    evaluation: str
    date: date
    materials: []
    goals: []

    def to_entity(self):
        entity = ClassPlan(
            code=str(uuid.uuid4()),
            teacher=self.teacher,
            subject=self.subject,
            group=self.group,
            period=self.period,
            date=self.date,
            contents=self.contents,
            evaluation=self.evaluation,
            materials=self.materials,
            goals=self.goals
        )
        return entity


class UpdateClassPlanCommand:
    code: str
    teacher: Teacher
    group: Group
    subject: Subject
    period: PeriodEnum
    contents: str
    evaluation: str
    date: date
    materials: []
    goals: []

    def to_entity(self):
        entity = ClassPlan(
            code=self.code,
            teacher=self.teacher,
            subject=self.subject,
            group=self.group,
            period=self.period,
            date=self.date,
            contents=self.contents,
            evaluation=self.evaluation,
            materials=self.materials,
            goals=self.goals
        )
        return entity


class DeleteClassPlanCommand:
    code: str
