"""
Testes na prática

Live de Python #79 - Testes de unidade na prática

Homepage and documentation:


Copyright (c) 2018, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

db = []

def insert_task(task: dict):
    """Insert task."""
    ...

def select_task(task_name: str, state: str):
    """Select task."""
    if not state:
        return [task for task in db if task_name == task['task_name']]
    return [
        task 
        for task in db 
        if task_name == task['task_name'] and state == task['state']
        # if state == task['state']
    ]
