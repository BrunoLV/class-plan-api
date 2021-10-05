from sqlalchemy.orm import Query

from src.domain.entities.class_plan import ClassPlan
from src.domain.exceptions.domais_expections import EntityhNotFoundError
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.db.orm.orms import ClassPlan as Orm


class RelationalClassPlanRepository(ClassPlanRepository):

    def __init__(self, session):
        self._session = session

    def save(self, class_plan: ClassPlan):
        self._session.add(Orm.from_entity(class_plan))

    def update(self, entity: ClassPlan):
        q: Query = self._session.query(Orm).filter(Orm.code == entity.code)
        if q.count() > 0:
            db: Orm = q.one()
            db.update_with_entity_data(entity)
        else:
            raise EntityhNotFoundError('Entity not found')

    def delete(self, code: str):
        q: Query = self._session.query(Orm).filter(Orm.code == code)
        if q.count() > 0:
            db = q.one()
            self._session.delete(db)
        else:
            raise EntityhNotFoundError('Entity not found')

    def find_by_code(self, code: str):
        orm = Orm.query.filter_by(code=code).first()
        if orm is not None:
            return orm.to_entity()
        else:
            raise EntityhNotFoundError('Entity not found')

    def list(self):
        orm_list = Orm.query.all()
        return list(map(lambda o: o.to_entity(), orm_list))
