class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        if task:
            self.tasks.append(task)
            return True
        return False

    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self):
        return self.tasks
