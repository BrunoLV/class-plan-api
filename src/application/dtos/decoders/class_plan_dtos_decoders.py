from datetime import date

from src.application.dtos.class_plan_dtos import ClassPlanDto, GroupDto, SubjectDto, TeacherDto


def to_class_plan_dto(json):
    return ClassPlanDto(
        teacher=TeacherDto(code=json["teacher"]["code"], name=json["teacher"]["name"]),
        school_class=GroupDto(code=json["school_class"]["code"], name=json["school_class"]["name"]),
        school_subject=SubjectDto(code=json["school_subject"]["code"], name=json["school_subject"]["name"]),
        contents=json["contents"],
        date=date.fromisoformat(json["date"]),
        evaluation=json["evaluation"],
        period=json["period"],
        materials=json["materials"],
        objectives=json["objectives"]
    )
