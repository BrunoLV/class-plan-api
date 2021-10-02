import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import List, Field

from enum import Enum


class PeriodEnum(str, Enum):
    FIRST = "FIRST"
    SECOND = "SECOND"
    THIRD = "THIRD"
    FOURTH = "FOURTH"


class ClassPlanPath(BaseModel):
    code: str = Field(description="Class Plan's code")


class Teacher(BaseModel):
    code: str = Field(description="Teacher's code")
    name: str = Field(description="Teacher's name")


class Subject(BaseModel):
    code: str = Field(description="Subject's code")
    name: str = Field(description="Subject's name")


class Group(BaseModel):
    code: str = Field(description="Group's code")
    name: str = Field(description="Group's name")


class ClassPlanBody(BaseModel):
    teacher: Teacher = Field(description="Responsible Teacher")
    group: Group = Field(description="Group of Students")
    subject: Subject = Field(description="Class Subject")
    period: PeriodEnum = Field(description="Period")
    contents: str = Field(description="Content which will be presented in the class")
    evaluation: str = Field(description="Teacher's evaluation about the class")
    date: datetime.date = Field(description="Class date")
    materials: List[str] = Field(description="List of necessary materials to do the class activities")
    goals: List[str] = Field(description="List of goals the should be achieved int the class")


class ClassPlan(BaseModel):
    code: str = Field(description="Class Plan's code")
    teacher: Teacher = Field(description="Responsible Teacher")
    group: Group = Field(description="Group of Students")
    subject: Subject = Field(description="Class Subject")
    period: PeriodEnum = Field(description="Period")
    contents: str = Field(description="Content which will be presented in the class")
    evaluation: str = Field(description="Teacher's evaluation about the class")
    date: datetime.date = Field(description="Class date")
    materials: List[str] = Field(description="List of necessary materials to do the class activities")
    goals: List[str] = Field(description="List of goals the should be achieved int the class")


class ClassPlanListResponse(BaseModel):
    total: int = Field(..., description="Total of class plans in system")
    list: Optional[List[ClassPlan]] = Field(..., description="list of class plans in system database")
