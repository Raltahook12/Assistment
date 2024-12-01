from typing import Dict

# Модель задачи
class Task:
    def __init__(self, task_id: int, title: str, description: str, category: str, due_date: str, priority: str, status: str = "Не выполнена"):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __eq__(self, other):
        return all(self.__dict__[key] == other.__dict__[key] for key in self.__dict__.keys() if key != 'id') #равен другому обьекту тогда, когда значения атрибутов(кроме id) значениям аттрибута другого объекта
    def to_dict(self) -> Dict:
        return self.__dict__

    @staticmethod
    def from_dict(data: Dict):
        return Task(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
            status=data["status"],
        )
