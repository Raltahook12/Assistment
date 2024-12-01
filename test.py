import pytest
from TaskManager import TaskManager
from main import main
@pytest.fixture
def manager():
    return TaskManager(storage_file="tasks.json")

def test_add_task(manager):
    manager.add_task("Test Task", "Description", "Work", "10.10.2024", "High")
    assert manager.tasks[-1].title == "Test Task"

def test_edit_task(manager):
    manager.add_task("Test Task", "Description", "Work", "10.10.2024", "High")
    manager.edit_task(manager.tasks[-1].id, title="Updated Task")
    assert manager.tasks[-1].title == "Updated Task"

def test_mark_completed(manager):
    manager.add_task("Test Task", "Description", "Work", "10.10.2024", "High")
    manager.mark_completed(manager.tasks[-1].id)
    assert manager.tasks[-1].status == "Выполнена"

def test_delete_task(manager):
    manager.add_task("Task 1", "Description", "Work", "10.10.2024", "High")
    task_befor_delete = len(manager.tasks)
    manager.delete_task(manager.tasks[-1].id)
    assert len(manager.tasks) < task_befor_delete

def test_search_tasks(manager):
    manager.add_task("test search", "Description", "test", "10.10.2024", "High")
    results = manager.search_tasks(category="test")
    assert all('test' in result.category for result in results)


