from src.domain.entities.class_plan import ClassPlan


class ClassPlanRepository():

    def save(self, class_plan: ClassPlan) -> None:
        pass

    def update(self, class_plan: ClassPlan) -> None:
        pass

    def delete(self, code: str) -> None:
        pass

    def find_by_code(self, code: str) -> ClassPlan:
        pass

    def list(self) -> []:
        pass
