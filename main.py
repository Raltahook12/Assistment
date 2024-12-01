from TaskManager import TaskManager
def main():
    manager = TaskManager()

    while True:
        print("\nМенеджер задач")
        print("1. Просмотр задач")
        print("2. Добавление задачи")
        print("3. Редактирование задачи")
        print("4. Отметить задачу выполненной")
        print("5. Удаление задачи")
        print("6. Поиск задач")
        print("7. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                category = input("Введите категорию (нажмите Enter для всех): ") or None
                manager.view_tasks(category)
            elif choice == "2":
                title = input("Название: ")
                description = input("Описание: ")
                category = input("Категория: ")
                due_date = input("Срок выполнения (DD.MM.YYYY): ")
                priority = input("Приоритет (низкий, средний, высокий): ")
                manager.add_task(title, description, category, due_date, priority)
            elif choice == "3":
                task_id = int(input("ID задачи: "))
                title = input("Новое название (оставьте пустым для пропуска): ")
                description = input("Новое описание (оставьте пустым для пропуска): ")
                category = input("Новая категория (оставьте пустым для пропуска): ")
                due_date = input("Новый срок выполнения (DD.MM.YYYY, оставьте пустым для пропуска): ")
                priority = input("Новый приоритет (низкий, средний, высокий, оставьте пустым для пропуска): ")
                manager.edit_task(task_id, title=title, description=description, category=category, due_date=due_date, priority=priority)
            elif choice == "4":
                task_id = int(input("ID задачи: "))
                manager.mark_completed(task_id)
            elif choice == "5":
                task_id = input("ID задачи (нажмите Enter для удаления по категории): ")
                category = None if task_id else input("Категория: ")
                manager.delete_task(int(task_id) if task_id else None, category)
            elif choice == "6":
                keyword = input("Ключевое слово: ") or None
                category = input("Категория: ") or None
                status = input("Статус (Выполнена/Не выполнена): ") or None
                manager.search_tasks(keyword, category, status)
            elif choice == "7":
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
