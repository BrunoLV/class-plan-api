from flask_sqlalchemy import SQLAlchemy

from src.domain.entities.class_plan import ClassPlan as Entity, PeriodEnum
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher

db = SQLAlchemy()


class ClassPlan(db.Model):
    __tablename__ = 'tb_class_plan'

    id = db.Column('id', db.Integer, primary_key=True)
    code = db.Column('code', db.String)
    teacher_code = db.Column('teacher_code', db.String)
    teacher_name = db.Column('teacher_name', db.String)
    group_code = db.Column('group_code', db.String)
    group_name = db.Column('group_name', db.String)
    subject_code = db.Column('subject_code', db.String)
    subject_name = db.Column('subject_name', db.String)
    period = db.Column('period', db.Enum(PeriodEnum))
    date = db.Column('date', db.Date)
    contents = db.Column('contents', db.Text)
    evaluation = db.Column('evaluation', db.Text)
    goals = db.relationship('ClassPlanGoal', cascade='all, delete-orphan')
    materials = db.relationship('ClassPlanMaterial', cascade='all, delete-orphan')

    def to_entity(self):
        e = Entity(contents=self.contents,
                   evaluation=self.evaluation,
                   period=self.period,
                   date=self.date,
                   code=self.code,
                   teacher=Teacher(code=self.teacher_code, name=self.teacher_name),
                   group=Group(code=self.group_code, name=self.group_name),
                   subject=Subject(code=self.subject_code, name=self.subject_name),
                   goals=list(map(lambda o: o.description, self.goals)),
                   materials=list(map(lambda m: m.description, self.materials)))
        return e

    def update_with_entity_data(self, e):
        self.date = e.date
        self.period = e.period
        self.contents = e.contents
        self.evaluation = e.evaluation
        self.teacher_code = e.teacher.code
        self.teacher_name = e.teacher.name
        self.group_code = e.group.code
        self.group_name = e.group.name
        self.subject_code = e.subject.code
        self.subject_name = e.subject.name

        self.materials.clear()
        self.goals.clear()

        for o in e.goals:
            goal = ClassPlanGoal()
            goal.description = o
            self.goals.append(goal)

        for m in e.materials:
            material = ClassPlanMaterial()
            material.description = m
            self.materials.append(material)

    @staticmethod
    def from_entity(e: Entity):
        orm = ClassPlan()
        orm.code = e.code
        orm.contents = e.contents
        orm.evaluation = e.evaluation
        orm.period = e.period
        orm.date = e.date
        orm.teacher_code = e.teacher.code
        orm.teacher_name = e.teacher.name
        orm.group_code = e.group.code
        orm.group_name = e.group.name
        orm.subject_code = e.subject.code
        orm.subject_name = e.subject.name

        for o in e.goals:
            goal = ClassPlanGoal()
            goal.description = o
            orm.goals.append(goal)

        for m in e.materials:
            material = ClassPlanMaterial()
            material.description = m
            orm.materials.append(material)

        return orm


class ClassPlanGoal(db.Model):
    __tablename__ = 'tb_class_plan_goal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    class_plan_id = db.Column(db.Integer, db.ForeignKey('tb_class_plan.id'))


class ClassPlanMaterial(db.Model):
    __tablename__ = 'tb_class_plan_material'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    class_plan_id = db.Column(db.Integer, db.ForeignKey('tb_class_plan.id'))
