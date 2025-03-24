# 📝 Simple To-Do List (Python) with GitHub Actions CI

This is a simple command-line To-Do List application written in Python, integrated with **GitHub Actions** to demonstrate **Continuous Integration (CI)** using automated testing via `pytest`.

---

## 🚀 Features

- Add tasks to a to-do list  
- Remove tasks from the list  
- View current tasks  
- Unit tested with `pytest`  
- Automated testing with **GitHub Actions**

---

## 📂 Project Structure

todo-app/
│
├── todo.py             # Main to-do app logic
├── test_todo.py        # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions workflow
├── requirements.txt    # Dependencies
└── README.md


---

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/SimpleToDoList.git
cd SimpleToDoList
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # For Windows PowerShell
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Tests
```bash
pytest
```
---
## GitHub Actions CI
```text
This project uses GitHub Actions to automatically:

Set up Python

Install dependencies

Run tests on every push and pull request

Check the .github/workflows/ci.yml file for the full configuration.
```
---
🙋‍♀️ Author
Harshali Jagtap - K00265900