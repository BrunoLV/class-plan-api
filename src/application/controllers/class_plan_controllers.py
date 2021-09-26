from src.application.cqs.commands.handlers.class_plan_commands_handlers import ClassPlanCommandHandler
from src.application.cqs.queries.handlers.class_plan_queries_handlers import ClassPlanQueryHandler


class ClassPlanController:

    def __init__(self):
        self._command_handler = ClassPlanCommandHandler()
        self._query_handler = ClassPlanQueryHandler()

    def create(self, command):
        created_code = self._command_handler.handle_create_command(command)
        return created_code

    def list(self):
        entities = self._query_handler.find_all()
        return entities

    def update(self, command):
        self._command_handler.handle_update_command(command)

    def delete(self, command):
        self._command_handler.handle_delete_command(command)

    def get(self, code):
        entity = self._query_handler.find_by_code(code)
        return entity
