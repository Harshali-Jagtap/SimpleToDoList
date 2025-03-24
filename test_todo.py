# test_todo.py

from todo import ToDoList

#Add task
def test_add_task():
    todo = ToDoList()
    assert todo.add("Write report") is True
    assert "Write report" in todo.list_tasks()

#Add empty task
def test_add_empty_task():
    todo = ToDoList()
    assert todo.add("") is False

#Remove task
def test_remove_task():
    todo = ToDoList()
    todo.add("Study")
    assert todo.remove("Study") is True
    assert "Study" not in todo.list_tasks()

#Remove non existent task
def test_remove_nonexistent_task():
    todo = ToDoList()
    assert todo.remove("Nonexistent") is False

#List tasks returns correct order
def test_list_tasks_order():
    todo = ToDoList()
    todo.add("Task A")
    todo.add("Task B")
    todo.add("Task C")
    assert todo.list_tasks() == ["Task A", "Task B", "Task C"]

#Removing from an empty list
def test_remove_from_empty_list():
    todo = ToDoList()
    assert todo.remove("Anything") is False

#Case Sensitivity in Remove
def test_case_sensitive_remove():
    todo = ToDoList()
    todo.add("Task")
    assert todo.remove("task") is False
    assert "Task" in todo.list_tasks()

#Add Duplicate Task
def test_add_duplicate_task():
    todo = ToDoList()
    todo.add("Read")
    result = todo.add("Read")
    assert result is True
    assert todo.list_tasks().count("Read") == 2  # If duplicates are allowed

#Remove Only One Duplicate
def test_remove_one_of_duplicates():
    todo = ToDoList()
    todo.add("Email")
    todo.add("Email")
    todo.remove("Email")
    assert todo.list_tasks().count("Email") == 1
