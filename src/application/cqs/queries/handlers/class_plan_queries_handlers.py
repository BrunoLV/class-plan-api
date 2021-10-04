from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.entities.class_plan import ClassPlan
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository

eng = create_engine('postgresql+psycopg2://root:root@localhost:5433/class_plan_db')


class ClassPlanQueryHandler:

    @staticmethod
    def find_by_code(code: str) -> ClassPlan:
        session = ClassPlanQueryHandler.get_session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        class_plan = repository.find_by_code(code)
        return class_plan

    @staticmethod
    def find_all() -> []:
        session = ClassPlanQueryHandler.get_session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        plans = repository.list()
        return plans

    @staticmethod
    def get_session():
        maker = sessionmaker(bind=eng)
        session = maker()
        return session
