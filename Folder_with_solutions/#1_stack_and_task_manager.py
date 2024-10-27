class Stack:
    """Класс для реализации стека, работающего по принципу LIFO (Last In First Out)."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека. Возвращает None, если стек пуст."""
        return self.items.pop() if self.items else None

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

    def __str__(self):
        """Возвращает строковое представление стека."""
        return str(self.items)


class TaskManager:
    """Класс для управления задачами на основе стека."""

    def __init__(self):
        self.stack = Stack()

    def new_task(self, task: str, priority: int):
        """Добавляет новую задачу с заданным приоритетом."""
        self.stack.push((priority, task))

    def remove_task(self):
        """Удаляет последнюю добавленную задачу."""
        if not self.stack.is_empty():
            self.stack.pop()

    def __str__(self):
        """Возвращает строковое представление задач, отсортированных по приоритету."""
        tasks = sorted(self.stack.items, key=lambda x: x[0])
        output = {}
        for priority, task in tasks:
            if priority not in output:
                output[priority] = []
            output[priority].append(task)
        return '\n'.join(f"{p} {'; '.join(ts)}" for p, ts in output.items())


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)
