from typing import List, Optional
from todo_app_with_i_t.models.task import Task
from todo_app_with_i_t.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def add_task(self, description: str) -> Task:
        if not description.strip():
            raise ValueError("Description cannot be empty")
        return self.repository.add(description)

    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all()

    def complete_task(self, task_id: int) -> Optional[Task]:
        task = self.repository.get(task_id)
        if task:
            task.status = "complete"
            self.repository.update(task)
            return task
        return None

    def update_task(self, task_id: int, new_description: str) -> Optional[Task]:
        if not new_description.strip():
            raise ValueError("Description cannot be empty")
        
        task = self.repository.get(task_id)
        if task:
            task.description = new_description
            self.repository.update(task)
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
