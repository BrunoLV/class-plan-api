from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.entities.class_plan import ClassPlan
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository

eng = create_engine('postgresql+psycopg2://root:root@localhost:5432/class_plan_db')


class ClassPlanQueryHandler():

    def find_by_code(self, code: str) -> ClassPlan:
        Session = sessionmaker(bind=eng)
        session = Session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        class_plan = repository.find_by_code(code)
        return class_plan

    def find_all(self) -> []:
        Session = sessionmaker(bind=eng)
        session = Session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        plans = repository.list()
        return plans