from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, DeleteClassPlanCommand, \
    UpdateClassPlanCommand
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository

eng = create_engine('postgresql+psycopg2://root:root@localhost:5432/class_plan_db')


class ClassPlanCommandHandler:

    @staticmethod
    def handle_create_command(command: CreateClassPlanCommand) -> str:
        entity = command.to_entity()
        session = ClassPlanCommandHandler.get_session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.save(entity)
        session.commit()
        return entity.code

    @staticmethod
    def handle_update_command(command: UpdateClassPlanCommand) -> None:
        data_to_update = command.to_entity()
        session = ClassPlanCommandHandler.get_session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        entity = repository.find_by_code(command.code)
        updated_entity = entity.update_state(data_to_update)
        repository.update(updated_entity)
        session.commit()

    @staticmethod
    def handle_delete_command(command: DeleteClassPlanCommand) -> None:
        session = ClassPlanCommandHandler.get_session()
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.delete(command.code)
        session.commit()

    @staticmethod
    def get_session():
        maker = sessionmaker(bind=eng)
        session = maker()
        return session
