from src.application.cqs.commands.class_plan_commands import CreateClassPlanCommand, DeleteClassPlanCommand, \
    UpdateClassPlanCommand
from src.domain.repositories.class_plan_repository import ClassPlanRepository
from src.infrastructure.db.orm.orms import db
from src.infrastructure.repositories.class_plan_repositories import RelationalClassPlanRepository


class ClassPlanCommandHandler:

    @staticmethod
    def handle_create_command(command: CreateClassPlanCommand) -> str:
        entity = command.to_entity()
        session = db.session
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.save(entity)
        session.commit()
        return entity.code

    @staticmethod
    def handle_update_command(command: UpdateClassPlanCommand) -> None:
        data_to_update = command.to_entity()
        session = db.session
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        entity = repository.find_by_code(command.code)
        updated_entity = entity.update_state(data_to_update)
        repository.update(updated_entity)
        session.commit()

    @staticmethod
    def handle_delete_command(command: DeleteClassPlanCommand) -> None:
        session = db.session
        repository: ClassPlanRepository = RelationalClassPlanRepository(session)
        repository.delete(command.code)
        session.commit()
