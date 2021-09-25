from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, DeleteClassPlanCommand, UpdateClassPlanCommand
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository

eng = create_engine('postgresql+psycopg2://root:root@localhost:5432/class_plan_db')


class ClassPlanCommandHandler():

    def handle_create_command(self, command: CreateClassPlanCommand) -> str:
        entity = command.to_entity()
        Session = sessionmaker(bind=eng)
        session = Session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.save(entity)
        session.commit()
        return entity.code

    def handle_update_command(self, command: UpdateClassPlanCommand) -> None:
        data_to_update = command.to_entity()
        Session = sessionmaker(bind=eng)
        session = Session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        entity = repository.find_by_code(command.code)
        updated_entity = entity.update_state(data_to_update)
        repository.update(updated_entity)
        session.commit()


    def handle_delete_command(self, command: DeleteClassPlanCommand) -> None:
        Session = sessionmaker(bind=eng)
        session = Session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.delete(command.code)
        session.commit()