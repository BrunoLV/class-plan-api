from sqlalchemy.orm import Query

from src.domain.entities.class_plan import ClassPlan
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.db.orm.class_plan_orms import ClassPlan as orm


class RelationalClassPlanRepository(ClassPlanRepository):

    def __init__(self, session):
        self._session = session

    def save(self, class_plan: ClassPlan) -> None:
        self._session.add(orm.from_entity(class_plan))

    def update(self, entity: ClassPlan) -> None:
        q: Query = self._session.query(orm).filter(orm.code == entity.code)
        if q.count() > 0:
            db: orm = q.one()
            db.update_with_entity_data(entity)

    def delete(self, code: str) -> None:
        q: Query = self._session.query(orm).filter(orm.code == code)
        if q.count():
            db = q.one()
            self._session.delete(db)

    def find_by_code(self, code: str) -> ClassPlan:
        q: Query = self._session.query(orm).filter(orm.code == code)
        if q.count() > 0:
            db: orm = q.one()
            return db.to_entity()
        return None

    def list(self) -> []:
        orms = self._session.query(orm).all()
        return list(map(lambda o: o.to_entity(), orms))
