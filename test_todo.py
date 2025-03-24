from todo import ToDoList

def test_add_task():
    todo = ToDoList()
    assert todo.add("Write report") is True
    assert "Write report" in todo.list_tasks()

def test_add_empty_task():
    todo = ToDoList()
    assert todo.add("") is False

def test_remove_task():
    todo = ToDoList()
    todo.add("Study")
    assert todo.remove("Study") is True
    assert "Study" not in todo.list_tasks()

def test_remove_nonexistent_task():
    todo = ToDoList()
    assert todo.remove("Nonexistent") is False
