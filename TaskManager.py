import json
from datetime import datetime
from typing import List, Optional
from Task import Task

# Менеджер задач
class TaskManager:

    def __init__(self, storage_file: str = "tasks.json"):
        """При создании объекта класса автоматически создаёт список задач десериализацией json файла"""
        self.storage_file = storage_file
        self.tasks: List[Task] = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """Загрузка задач из Json файла с проверкой доступности файла"""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            raise SystemError("Ошибка в загрузке файла, файл не найден или повреждён")

    def save_tasks(self):
        """Сохранение задач в файл"""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str):
        """Добавление задачи с указанными значениями атрибутов"""
        datetime.strptime(due_date, "%d.%m.%Y")
        task_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(task_id, title, description, category, due_date, priority)
        if all(new_task != task for task in self.tasks): #проверка наличия задачи в списке по её сути(когда все поля одной задачи равны другой считаем что это таже задача)
            self.tasks.append(new_task)
            self.save_tasks()
        else:
            self.delete_task([task.id for task in self.tasks if task == new_task])
            self.tasks.append(new_task)
            print("Такая задача уже есть в списке, старая задача была переписана")

    def view_tasks(self, category: Optional[str] = None):
        """Вывод задач по выбраным категориям, в случае если категория не указывается выводятся все задачи"""
        filtered_tasks = self.tasks if not category else [task for task in self.tasks if task.category == category]
        for task in filtered_tasks:
            print(task.to_dict())

    def edit_task(self, task_id: int, **kwargs):
        """Редактирование задачи пользователем"""
        task = next((task for task in self.tasks if task.id == task_id), None)
        if not task:
            raise ValueError(f"Задача с ID {task_id} не найдена.")
        for key, value in kwargs.items():
            if hasattr(task, key) and value:
                setattr(task, key, value)
        self.save_tasks()

    def mark_completed(self, task_id: int):
        """Отметка о выполнении задачи"""
        self.edit_task(task_id, status="Выполнена")

    def delete_task(self, task_id: Optional[int] = None, category: Optional[str] = None):
        """ Удаление задач по id или по всей категории(если глобальный проект закрылся, например)"""
        if task_id:
            self.tasks = [task for task in self.tasks if task.id != task_id]
        elif category:
            self.tasks = [task for task in self.tasks if task.category != category]
        self.save_tasks()

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None, status: Optional[str] = None):
        """Поиск задач по категориям, ключевым словам, статусу выполнения"""
        results = self.tasks
        if keyword:
            results = [task for task in results if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        if category:
            results = [task for task in results if task.category == category]
        if status:
            results = [task for task in results if task.status == status]
        for task in results:
            print(task.to_dict())
        return results
