from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.domain.entities.class_plan import ClassPlan as entity, PeriodEnum
from src.domain.value_objects.group import Group
from src.domain.value_objects.subject import Subject
from src.domain.value_objects.teacher import Teacher

Base = declarative_base()


class ClassPlan(Base):
    __tablename__ = "tb_class_plan"

    id = Column('id', Integer, primary_key=True)
    code = Column('code', String)
    teacher_code = Column('teacher_code', String)
    teacher_name = Column('teacher_name', String)
    group_code = Column('group_code', String)
    group_name = Column('group_name', String)
    subject_code = Column('subject_code', String)
    subject_name = Column('subject_name', String)
    period = Column('period', Enum(PeriodEnum))
    date = Column('date', Date)
    contents = Column('contents', Text)
    evaluation = Column('evaluation', Text)
    goals = relationship("ClassPlanGoal", cascade="all, delete-orphan")
    materials = relationship("ClassPlanMaterial", cascade="all, delete-orphan")

    def to_entity(self):
        e = entity(contents=self.contents,
                   evaluation=self.evaluation,
                   period=self.evaluation,
                   date=self.date,
                   code=self.code,
                   teacher=Teacher(code=self.teacher_code, name=self.teacher_name),
                   group=Group(code=self.group_code, name=self.group_name),
                   subject=Subject(code=self.subject_code, name=self.subject_name),
                   goals=list(map(lambda o: o.description, self.goals)),
                   materials=list(map(lambda m: m.description, self.materials))
                   )
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
    def from_entity(e: entity):
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


class ClassPlanGoal(Base):
    __tablename__ = "tb_class_plan_goal"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    class_plan_id = Column(Integer, ForeignKey("tb_class_plan.id"))


class ClassPlanMaterial(Base):
    __tablename__ = "tb_class_plan_material"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    class_plan_id = Column(Integer, ForeignKey("tb_class_plan.id"))
