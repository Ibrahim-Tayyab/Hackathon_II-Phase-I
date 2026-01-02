from typing import Dict, List, Optional
from todo_app_with_i_t.models.task import Task

class TaskRepository:
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    def update(self, task: Task) -> None:
        if task.id in self._tasks:
            self._tasks[task.id] = task

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
