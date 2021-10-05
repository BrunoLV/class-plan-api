import copy
from datetime import date
from enum import Enum

from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher


class PeriodEnum(Enum):
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"

    def __str__(self):
        return self.value.upper()


class ClassPlan:

    def __init__(self,
                 code,
                 teacher,
                 group,
                 subject,
                 period: PeriodEnum,
                 contents,
                 evaluation,
                 date,
                 materials=None,
                 goals=None):

        if goals is None:
            goals = []
        if materials is None:
            materials = []

        self.group = group
        self.code = code
        self.teacher = teacher
        self.subject = subject
        self.period = period
        self.contents = contents
        self.evaluation = evaluation
        self.date = date
        self.materials = materials
        self.goals = goals

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def teacher(self):
        return copy.deepcopy(self._teacher)

    @teacher.setter
    def teacher(self, value):

        if value is None or type(value) is not Teacher:
            raise ValueError('Teacher should be a object of Teacher type different than None.')

        self._teacher = value

    @property
    def group(self):
        return copy.deepcopy(self._group)

    @group.setter
    def group(self, value):

        if value is None or type(value) is not Group:
            raise ValueError('Group should be a object of SchoolClass type different than None.')

        self._group = value

    @property
    def subject(self):
        return copy.deepcopy(self._subject)

    @subject.setter
    def subject(self, value):

        if value is None or type(value) is not Subject:
            raise ValueError('Subject must not be a object of SchoolSubjects type different than None.')

        self._subject = value

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):

        if value is None or type(value) is not str or value == '':
            raise ValueError('Contents should be a non blank string.')

        self._contents = value

    @property
    def evaluation(self):
        return self._evaluation

    @evaluation.setter
    def evaluation(self, value):

        if value is None or type(value) is not str:
            raise ValueError('Evaluation should be a string.')

        self._evaluation = value

    @property
    def date(self):
        return copy.deepcopy(self._date)

    @date.setter
    def date(self, value):

        if value is None or type(value) is not date:
            raise ValueError('Date must be a date object different than None.')

        if value < date.today():
            raise ValueError('The date should be equal or greater than the current date')

        self._date = value

    @property
    def materials(self):
        return copy.deepcopy(self._materials)

    @materials.setter
    def materials(self, value):

        if value is None or type(value) is not list:
            raise ValueError('Materials should be a list.')

        self._materials = value

    @property
    def goals(self):
        return copy.deepcopy(self._goals)

    @goals.setter
    def goals(self, value):

        if value is None or type(value) is not list:
            raise ValueError('Goals should be a list.')

        self._goals = value

    def add_goal(self, objective):

        if objective is None or type(objective) is not str or objective == '':
            raise ValueError('Goal must be a non Blank string.')

        if self._goals is None:
            self._goals = []

        self._goals.append(objective)

    def remove_goal(self, objective):

        if objective in self._goals:
            self._goals.remove(objective)

    def add_material(self, material):

        if material is None or type(material) is not str or material == '':
            raise ValueError('Material must be a non Blank string.')

        if self._materials is None:
            self._materials = []

        self._materials.append(material)

    def remove_material(self, material):

        if material in self._materials:
            self._materials.remove(material)

    def update_state(self, data_to_update):

        return ClassPlan(
            code=self.code,
            teacher=copy.copy(data_to_update.teacher),
            group=copy.copy(data_to_update.group),
            subject=copy.copy(data_to_update.subject),
            date=copy.copy(data_to_update.date),
            period=data_to_update.period,
            contents=data_to_update.contents,
            evaluation=data_to_update.evaluation,
            goals=copy.copy(data_to_update.goals),
            materials=copy.copy(data_to_update.materials)
        )
