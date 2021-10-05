from src.domain.entities.class_plan import ClassPlan
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository


class ClassPlanQueryHandler:

    @staticmethod
    def find_by_code(code: str) -> ClassPlan:
        repository: ClassPlanRepository = RelationalClassPlanRepository(None)
        class_plan = repository.find_by_code(code)
        return class_plan

    @staticmethod
    def find_all() -> []:
        repository: ClassPlanRepository = RelationalClassPlanRepository(None)
        plans = repository.list()
        return plans
