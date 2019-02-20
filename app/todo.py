"""
Testes na prática

Live de Python #79 - Testes de unidade na prática

Homepage and documentation:


Copyright (c) 2018, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from .database import insert_task, select_task
from datetime import datetime
from itertools import count

# identificador é um generetor
identificador = count()

def process_date(string_date: str):
    """Processa a data para o formato correto."""
    return datetime.strptime(string_date, '%d/%m/%Y')

def nova_task(task_name: str, data: str):
    """insere uma nova task na lista de task."""

    global identificador
    
    task = {
        'id': next(identificador),
        'task_name': task_name,
        'date': process_date(data),
        'state': 'TODO'
    }
    result_db = insert_task(task)
    return task

def listar_task(task_name: str, state: str = ''):
    """lista as task."""
    return select_task(task_name, state)
